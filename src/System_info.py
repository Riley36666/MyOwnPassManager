import platform
import socket
import uuid
import subprocess


def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except Exception:
        return None

def get_pc_info():
    info = {}


    info["OS"] = platform.system()
    info["OS Release"] = platform.release()
    info["OS Version"] = platform.version()
    info["Architecture"] = platform.machine()
    info["Processor"] = platform.processor()
    info["Python Version"] = platform.python_version()

    # Host info
    info["Hostname"] = socket.gethostname()
    info["IP Address"] = socket.gethostbyname(socket.gethostname())
    info["MAC Address"] = ':'.join(
        f"{(uuid.getnode() >> i) & 0xff:02x}"
        for i in range(0, 48, 8)
    )

    return info

def getMACaddress():
    mac = uuid.getnode()
    mac_address = ':'.join(f'{(mac >> ele) & 0xff:02x}' for ele in range(40, -1, -8))
    return mac_address

#print(getMACaddress())