import os
import signal
import subprocess

def kill_processes_by_user(username):
    try:
        # Get the list of processes for the given user
        result = subprocess.run(['pgrep', '-u', username], stdout=subprocess.PIPE, text=True)
        pids = result.stdout.split()

        # Kill each process
        for pid in pids:
            os.kill(int(pid), signal.SIGKILL)
        print(f"All processes for user '{username}' have been killed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user = input("Enter the username: ")
    kill_processes_by_user(user)