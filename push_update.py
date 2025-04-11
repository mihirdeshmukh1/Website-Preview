import subprocess
import os
import datetime


def push_generated_html():
    os.chdir(os.path.dirname(__file__))
    subprocess.run(["git", "add", "generated/generated_website16.html"])
    commit_msg = f"Auto update: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    subprocess.run(["git", "push"])


if __name__ == "__main__":
    push_generated_html()
