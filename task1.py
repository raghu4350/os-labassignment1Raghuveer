import os
import sys

def main():
    try:
        N = int(input("Enter the number of child processes: "))
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)
    print(f"Parent process PID: {os.getpid()}, creating {N} child processes...")
    for i in range(N):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1}: PID - {os.getpid()}, Parent PID - {os.getppid()}, Message - Hello from child {i+1}")
            os._exit(0)
    for i in range(N):
        pid, status = os.wait()
        print(f"Parent: Child with PID = {pid} finished with status {status}")

if __name__ == "__main__":
    main()