import os

def inspect_process(pid):
    status_file = f"/proc/{pid}/status"
    exe_file = f"/proc/{pid}/exe"
    fd_dir = f"/proc/{pid}/fd"
    try:
        with open(status_file, "r") as f:
            lines = f.read().splitlines()
            name = [line.split()[1] for line in lines if line.startswith("Name:")][0]
            state = [line.split()[1] for line in lines if line.startswith("State:")][0]
            vm_size = [line.split()[1] for line in lines if line.startswith("VmSize:")][0]
            print(f"Process Name : {name}")
            print(f"Process State: {state}")
            print(f"Memory Usage : {vm_size} kB")
        exe_path = os.readlink(exe_file)
        print(f"Executable : {exe_path}")
    except FileNotFoundError:
        print("Executable : Not available")
    try:
        fds = os.listdir(fd_dir)
        print("Open FDs :")
        for fd in fds:
            try:
                target = os.readlink(f"/proc/{pid}/fd/{fd}")
                print(f"  FD {fd} -> {target}")
            except OSError:
                print(f"  FD {fd} -> [Unavailable]")
    except FileNotFoundError:
        print("Open FDs : Not available")

if __name__ == "__main__":
    pid_str = input("Enter PID to inspect : ")
    if not pid_str.isdigit():
        print("Invalid PID")
    else:
        inspect_process(int(pid_str))