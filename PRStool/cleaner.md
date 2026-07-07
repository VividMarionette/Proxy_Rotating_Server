# Build Instructions

Compile the source code into an executable using g++:

```bash
g++ cleaner.cpp -o cleaner.exe
```

If you want extra compiler warnings enabled:

```bash
g++ cleaner.cpp -Wall -Wextra -o cleaner.exe
```

---

# Running the Program

After compiling, run:

```bash
cleaner.exe
```

or from PowerShell:

```powershell
.\cleaner.exe
```

The program will automatically read:

```
proxies.txt
```

Make sure `proxies.txt` is located in the same folder as `cleaner.exe`.

Example folder structure:

```
Proxy_Cleaner/
│
├── cleaner.cpp
├── cleaner.exe
├── proxies.txt
└── README.md
```
