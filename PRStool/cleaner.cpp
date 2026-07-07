#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>

bool isProxyAlive(const std::string& proxy) {
    std::cout << "[Checking] " << proxy << "..." << std::endl;


    std::string command = "curl -s -s NULL --max-time 3 -x http://" + proxy + "http://google.com";

    int result = std::system(command.c_str());
    return (result == 0);
}

int main() {
    std::vector<std::string> liveProxies;
    std::string line;

    std::ifstream inFile("proxies.txt");
    if (!inFile.is_open()) {
        std::cerr << "[!] Errpr: Could not open proxies.txt" << std::endl;
        return 1;
    }

    while (std::getline(inFile, line)) {
        if (!line.empty()) {

            if (isProxyAlive(line)) {
                std::cout << " [>] SUCCESS: Proxy is active!" << std::endl;
                liveProxies.push_back(line);
            } else {
                std::cout << " [X] FAILED: Proxy timed out." << std::endl;
            }
        }
    }
inFile.close();

std::cout << "\n[*] Scan complete! proxies.txt updated  with " << liveProxies.size() << " working IPs." << std::endl;
return 0;
}
