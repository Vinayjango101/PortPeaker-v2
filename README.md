# 🚀 PortPeaker v2  Release Notes
Version: 2.0
Release Date: (18 July 2025)
Author: Vinayjango101

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Windows_logo_-_2012.svg/2048px-Windows_logo_-_2012.svg.png" alt="Alt Text" width="50" height="50">
Windows Build in action 

for windows i have used ``pyinstaller --onefile PortPeaker-v2.py``
the prebuild binary (.exe) is given below to download !

![Animation](https://github.com/user-attachments/assets/6efb640a-ebb3-44fb-b2c2-cf3d142df899)

# Overview
PortPeaker v2 is a significant upgrade from the original PortPeaker port scanner and banner grabber. Designed to be simple yet powerful, this new version leverages Python’s socket programming alongside colorful terminal output to provide clear, user-friendly port scanning and banner grabbing for common TCP services.

<img width="1210" height="581" alt="Screenshot 2025-07-30 162514" src="https://github.com/user-attachments/assets/4ee10a79-15c1-4db1-8fe1-800d2d3384eb" />

# Key Improvements in PortPeaker v2
## 1. Improved Code Structure & Reliability
Redesigned with Python's with statement for socket handling, ensuring safe and automatic resource management (no need for manual socket closing).

Enhanced exception handling to catch a broader range of errors cleanly, making scans more stable.

Uniform timeout handling for all ports, improving scan consistency.

## 2. Enhanced User Experience
Integrated Colorama library for colored, easy-to-read console output:

Cyan prompt for IP/host input

Green for successful open ports and banner grabs

Red for closed ports, timeouts, and errors

Clean and informative status messages that improve clarity during scans.

## 3. Efficient Banner Grabbing
Attempts to receive and decode service banners from open ports.

Gracefully handles ports that don’t respond or close connections abruptly.

Provides clear placeholders for missing or unreadable banners.

## 4. Simplified & Readable Code
Well-commented code for easy understanding and future customization.

Consistent indentation and style for maintainability.

# Dependencies

PortPeaker v2 requires the following dependency:

- [`colorama`](https://pypi.org/project/colorama/) — used for colored terminal output.

You can install it easily via pip:

```bash
pip install colorama
```

# Future Roadmap (Coming Soon)
- Custom port range scanning
- Multi-threaded scanning for speed improvements
- Export scan results to files (CSV/JSON)
- Service identification and fingerprinting
