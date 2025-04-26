# ADOS - Achmed's Denial of Service Tool

**ADOS** (Achmed's Denial of Service) is a lightweight and easy-to-use DoS attack simulation tool built with Python. It allows you to stress-test your own servers by sending a high volume of HTTP requests using multi-threading techniques.

> **Warning:** This tool is intended for educational purposes and authorized testing only. Unauthorized attacks are illegal.

## Features
- Multi-threaded HTTP request flood
- Real-time live reporting (success/failure rates, response times)
- Customizable target protocol (HTTP/HTTPS) and port
- Graceful shutdown with a full final report
- Lightweight and dependency-friendly (only `requests` needed)

## Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/ados.git
cd ados
pip install -r requirements.txt
```

> **Note:** You must have Python 3 installed.

## Usage
To start the tool, run the following command:

```bash
python main.py
```

You will be prompted to:
1. Select target protocol (http/https)
2. Enter target IP or domain
3. (Optional) Set a custom port
4. Choose the number of attack threads

## Disclaimer
This tool is meant for authorized testing only. Do not use ADOS to attack systems you do not own or have explicit permission to test.

The developer assumes no responsibility for misuse of this tool.
___
Created with ❤️ by Achmed Hibatillah
