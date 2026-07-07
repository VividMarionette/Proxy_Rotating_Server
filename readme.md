# 🔄 Proxy Rotating Server

## Overview

This project was created as a networking learning project to better understand how proxy routing, socket programming, TCP connections, and multithreading work.

The repository contains two applications:

- A **Python Proxy Rotator**
- A **C++ Proxy Checker**

Together they demonstrate how a client request can be routed through available proxies while learning network communication, debugging, and troubleshooting.

---

# Features

## Python Proxy Rotator

- Reads proxy servers from `proxies.txt`
- Randomly selects a proxy
- Creates a local proxy server
- Accepts multiple client connections
- Uses multithreading
- Handles timeout and connection errors
- Demonstrates TCP socket communication

---

## C++ Proxy Checker

- Reads proxy addresses from `proxies.txt`
- Tests whether proxies respond
- Displays working and failed proxies
- Stores successful proxies for later use
- Demonstrates file handling and networking concepts

---

# Technologies Used

- Python 3
- C++
- TCP Sockets
- Threads
- File Handling
- Networking
- Proxy Concepts

---

# Project Structure

```
Proxy_Rotating_Server/
│
├── proxy_rotator.py
├── proxy_checker.cpp
├── proxies.txt
└── README.md
```

---

# How It Works

### Step 1

The C++ application reads every proxy stored inside `proxies.txt`.

It attempts to connect to each proxy and determines whether it responds within the configured timeout period.

---

### Step 2

The Python application loads the available proxies from the same file.

Whenever a client connects to the local server, one proxy is randomly selected and the connection is forwarded through it.

Each client is handled inside its own thread, allowing multiple connections to be processed independently.

---

# Skills Practised

Throughout this project I learnt:

- TCP socket programming
- Network communication
- Proxy concepts
- Python threading
- File management
- C++ vectors
- Error handling
- Debugging
- Network troubleshooting
- Reading configuration files

---

# Challenges

The most difficult part of this project was troubleshooting network timeouts.

Many proxy servers became unavailable, responded slowly, or were incompatible with the connection method being tested.

This project taught me that networking problems are not always caused by programming mistakes.

Sometimes the code is correct while the network environment is the limiting factor.

Learning how to identify that difference became one of the biggest lessons from this project.

---

# Future Improvements

Possible improvements include:

- Better logging
- Automatic removal of unavailable proxies
- Configurable timeout values
- Improved proxy validation
- Performance optimisation
- Additional protocol support
- Better error reporting

---

# Purpose

This repository was built as part of my programming and networking journey while learning:

- Python
- C++
- Windows
- Linux
- Networking
- Help Desk
- Cybersecurity Fundamentals

The goal is not simply to create projects, but to understand how systems communicate and strengthen my troubleshooting skills through practical development.

---

Student Developer

Currently building projects in:

- Python
- C++
- PowerShell
- Windows Administration
- Networking
- Linux
- Cybersecurity

Every project in this repository represents another step in my journey toward becoming an IT Support / Help Desk professional while continuing to grow my cybersecurity knowledge.
