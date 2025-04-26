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
Note: You must have Python 3 installed.

Usage
To start the tool, run the following command:

bash
Copy
Edit
python main.py
You will be prompted to:

Select target protocol (http/https)

Enter target IP or domain

(Optional) Set a custom port

Choose number of attack threads

Example:
text
Copy
Edit
Target Protocol (http/https): https
Target IP or Domain: example.com
Target Port (leave empty for default): 443
Number of Threads: 50
Disclaimer
This tool is meant for educational and authorized testing only.
Do not use ADOS to attack systems you do not own or have explicit permission to test.
The developer assumes no responsibility for misuse of this tool.

Created with ❤️ by Achmed Hibatillah
