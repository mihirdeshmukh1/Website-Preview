import subprocess
import threading
import os


def start_web_server():
    print("Starting web server on port 8000...")
    subprocess.run(['python', '-m', 'http.server', '8000'])


def start_sync_service():
    print("Starting git sync service...")
    subprocess.run(['python', 'sync_updates.py'])


def main():
    server_thread = threading.Thread(target=start_web_server)
    server_thread.daemon = True
    server_thread.start()

    start_sync_service()


if __name__ == "__main__":
    main()
