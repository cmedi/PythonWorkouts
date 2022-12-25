import os

def check_reboot():
    '''returns True if the computer has a pending reboot'''
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)
main()