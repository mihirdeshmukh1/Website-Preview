import os
import subprocess
import time
import hashlib


def get_file_hash(file_path):
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash


def commit_and_push_changes(file_path):
    try:
        subprocess.run(['git', 'add', file_path], check=True)

        commit_message = f"Auto-update generated website: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        subprocess.run(['git', 'push'], check=True)

        print(f"Successfully committed and pushed changes to {file_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error in git operations: {e}")
        return False


def monitor_file_changes(file_path, check_interval=2):
    print(f"Monitoring {file_path} for changes...")
    last_hash = get_file_hash(file_path)

    while True:
        time.sleep(check_interval)
        current_hash = get_file_hash(file_path)

        if last_hash is None and current_hash is not None:
            print(f"File {file_path} created")
            commit_and_push_changes(file_path)
            last_hash = current_hash
            continue

        if current_hash != last_hash:
            print(f"Change detected in {file_path}")
            commit_and_push_changes(file_path)
            last_hash = current_hash


if __name__ == "__main__":
    target_file = "generated_website16.html"

    monitor_file_changes(target_file)
