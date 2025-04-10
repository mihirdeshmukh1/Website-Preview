import subprocess
import threading
import os


def start_web_server():
    """Start the Python HTTP server"""
    print("Starting web server on port 8000...")
    subprocess.run(['python', '-m', 'http.server', '8000'])


def start_sync_service():
    """Start the git sync service"""
    print("Starting git sync service...")
    subprocess.run(['python', 'sync_updates.py'])


def main():
    # Start web server in a thread
    server_thread = threading.Thread(target=start_web_server)
    server_thread.daemon = True
    server_thread.start()

    # Start sync service in the main thread
    start_sync_service()


if __name__ == "__main__":
    main()
