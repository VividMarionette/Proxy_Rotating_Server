# 🔄 Rotating Proxy Server (Python)

## Overview

The Rotating Proxy Server is a Python networking project built to explore TCP socket programming, multithreading, proxy concepts, and client-server communication.

The application creates a local server that accepts client connections and attempts to forward traffic using a randomly selected proxy from a list stored in `proxies.txt`.

This project was developed as part of my networking and Python learning journey while strengthening my troubleshooting and debugging skills.

---

# Features

- Reads proxy addresses from `proxies.txt`
- Randomly selects a proxy for each connection
- Creates a local TCP server
- Accepts multiple client connections
- Uses multithreading for concurrent connections
- Demonstrates socket programming
- Handles connection failures and timeout errors
- Displays real-time console output

---

# Technologies Used

- Python 3
- Socket Programming
- Threading
- File Handling
- Random Module
- TCP Networking

---

# Project Structure

```
Proxy_Rotating_Server/
│
├── rotating_proxy.py
├── proxies.txt
└── README.md
```

---

# Requirements

Python 3.x

No external libraries are required.

The project uses only Python's built-in modules:

- socket
- threading
- random

---

# How It Works

### Step 1

The application starts a local TCP server.

```
127.0.0.1:8888
```

---

### Step 2

When a client connects, the program loads every proxy stored inside `proxies.txt`.

---

### Step 3

A proxy is randomly selected.

---

### Step 4

The application attempts to establish a TCP connection using the selected proxy.

---

### Step 5

Traffic is forwarded between the client and the selected proxy while the connection remains active.

---

### Step 6

If the connection fails or times out, the program catches the exception and displays an error message.

---

# Running the Program

Clone the repository.

Place your proxy list inside:

```
proxies.txt
```

Run the application:

```bash
python rotating_proxy.py
```

The server will start listening on:

```
127.0.0.1:8888
```

---

# Example Output

```
[*] Rotating Proxy active http://127.0.0.1:8888

[<>] Routing request via random IP:
103.81.19.162:6666

[!] Proxy connection failed or timed out.
```

---

# Skills Practised

This project helped me develop experience with:

- Python
- TCP sockets
- Client-server communication
- Multithreading
- File handling
- Network programming
- Exception handling
- Debugging
- Network troubleshooting

---

# Challenges

The most difficult part of this project was troubleshooting timeout issues.

Many proxy servers were unavailable, slow, or no longer responding.

Working through these problems taught me an important lesson:

> Correct code does not always guarantee a successful network connection.

Sometimes the issue is caused by the network environment rather than the application itself.

Learning to identify the difference became one of the biggest lessons from this project.

---

# Future Improvements

Possible future improvements include:

- Better logging
- Configurable server settings
- Improved timeout handling
- Automatic proxy validation
- Support for additional proxy protocols
- Performance optimisation
- More informative console output

---

# Learning Objectives

The purpose of this project was to gain practical experience with:

- Python networking
- Socket programming
- TCP communication
- Multithreading
- Debugging
- Troubleshooting
- Network fundamentals

---

# Author

**Kat**

Student Developer

Currently learning:

- Python
- C++
- PowerShell
- Windows Administration
- Linux
- Networking
- Help Desk
- Cybersecurity

Building projects every day to strengthen my programming, troubleshooting, and networking skills while working toward an entry-level IT Support / Help Desk career.
