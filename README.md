# Python Network Scanner

A Python-based TCP network port scanner developed as a practical learning project in Python, networking, and cybersecurity.

## Overview

This project is a simple TCP network scanner that allows a user to enter a target IP address or hostname and specify TCP ports to check.

The program attempts to establish TCP connections to the selected ports and reports whether each port is open or closed. Scan results can also be saved to a file for later review.

## Features

- Target IP address or hostname input
- Multiple TCP port selection
- TCP socket-based scanning
- Open/closed port detection
- Input validation
- Exception handling
- Scan result display
- Saving scan results to a file

## Technologies Used

- Python 3
- `socket` module
- TCP/IP networking concepts
- File handling
- Exception handling

## How It Works

The scanner follows this basic process:

1. Accepts a target IP address or hostname.
2. Accepts a list of TCP ports from the user.
3. Converts the selected port values into integers.
4. Attempts a TCP connection to each selected port.
5. Determines whether the connection succeeds or fails.
6. Displays the result for each port.
7. Saves the scan results to a file.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/alphakhan00/network-scanner.git
