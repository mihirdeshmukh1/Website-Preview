import subprocess
import time
import os


def pull_updates():
    try:
        print("Pulling latest changes from repository...")
        subprocess.run(['git', 'pull'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error pulling updates: {e}")
        return False


def main():
    interval = 30

    print(
        f"Starting repository sync service. Will pull every {interval} seconds.")

    while True:
        pull_updates()
        time.sleep(interval)


if __name__ == "__main__":
    main()
