import socket
import threading
import random

def get_random_proxy():
    try:
        with open("proxies.txt", "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        if not proxies:
            return None
        return random.choice(proxies)
    except FileNotFoundError:
        print("[!] Error: proxies.txt file not found!")
        return None
def handle_client(client_socket):
    try:
        
        request = client_socket.recv(4096)       
        if not request:
            return
        
        proxy_target = get_random_proxy()
        if not proxy_target:
            print("[!] No proxies available. Closing connection.")
            return

        proxy_host, proxy_port = proxy_target.split(":")
        proxy_port = int(proxy_port)

        print(f"[<>] Routing request via random IP: {proxy_host}:{proxy_port}")

        outbound_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        outbound_socket.connect((proxy_host, proxy_port))

        outbound_socket.sendall(request)

        client_socket.settimeout(5.0)

        while True:
            data = outbound_socket.recv(4096)
            if len(data) > 0:
                client_socket.send(data)
            else:
                break
    
    except Exception as e:
        print(f"[! Proxy leg failed or time out: {e}")    
    finally:
        client_socket.close()
        
def start_rotator():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8888))
    server.listen(10)
    print("[*] Rotating Proxy active http://127.0.0.1:8888")
    
    while True:
        client_sock, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_sock,))
        thread.start()
        
if __name__ == "__main__":
    start_rotator()                
