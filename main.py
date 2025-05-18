#!/bin/python3
import platform
from base64 import standard_b64encode
import sys

def get_distro():
    if not OVERRIDE_DISTRO:
        if platform.system() == "Linux":
            try:
                with open("/etc/os-release") as f:
                    os_release = f.read()
                    if "ubuntu" in os_release.lower():
                        return "Ubuntu"
                    elif "debian" in os_release.lower():
                        return "Debian"
                    elif "arch" in os_release.lower():
                        return "Arch Linux"
                    elif "fedora" in os_release.lower():
                        return "Fedora"
                    elif "centos" in os_release.lower():
                        return "CentOS"
                    elif "gentoo" in os_release.lower():
                        return "Gentoo"
                    elif "slackware" in os_release.lower(): # I'm not sure, if Slackware supports /etc/os-release
                        return "Slackware"
                    else:
                        return "Linux"
            except FileNotFoundError:
                return "Linux"
        elif platform.system() == "Windows":
            return "Windows"
        elif platform.system() == "Darwin":
            if platform.mac_ver()[0].startswith("10."):
                return "Mac OS X"
            else:
                return "Mac OS"
        else:
            return "Unknown"
    else:
        return OVERRIDE_DISTRO

# --------SETTINGS SECTION--------
OVERRIDE_DISTRO = None
OUTPUT = "\033[1mDistro: \033[0m" + get_distro()
ALLOW_KITTY_IMAGES = False
# ------END SETINGS SECTION-------

logos = {
    # --SPECIAL LOGOS--
    "Unknown": "\033[38;2;180;180;180mN",
    # --LINUX LOGOS--
    "Linux": "\033[38;2;245;192;33mL",
    "Fedora": "\033[38;2;81;162;218mF",
    "Ubuntu": "\033[38;2;233;84;32mU",
    "Debian": "\033[38;2;168;0;48mD",
    "Arch Linux": "\033[38;2;15;148;210mA",
    "Gentoo": "\033[38;2;221;218;235mG",
    "CentOS": "\033[38;2;161;79;140mC",
    "Slackware": "\033[38;2;255;255;255mS",
    # --WINDOWS LOGOS--
    "Windows": "\033[38;2;0;103;184mW",
    # --APPLE LOGOS--
    "Mac OS": "\033[38;2;220;220;200mM",
    "Mac OS X": "\033[38;2;168;0;48mX"
}

def serialize_gr_command(**cmd):
    payload = cmd.pop('payload', None)
    cmd = ','.join(f'{k}={v}' for k, v in cmd.items())
    ans = []
    w = ans.append
    w(b'\033_G'), w(cmd.encode('ascii'))
    if payload:
        w(b';')
        w(payload)
    w(b'\033\\')
    return b''.join(ans)

def write_chunked(**cmd):
    data = standard_b64encode(cmd.pop('data'))
    while data:
        chunk, data = data[:4096], data[4096:]
        m = 1 if data else 0
        sys.stdout.buffer.write(serialize_gr_command(payload=chunk, m=m,
                                                    **cmd))
        sys.stdout.flush()
        cmd.clear()

if ALLOW_KITTY_IMAGES:
    try:
        with open("logos/" + get_distro() + ".png", "rb") as f:
            write_chunked(a='T', f=100, s=16, v=16, data=f.read())
        print(" " + OUTPUT)
    except FileNotFoundError:
        print("\033[0;91m[!]\033[0m no icon for your distro found. but you can suggest icon, making an issue on our GitHub! https://github.com/msh356/compactfetch/issues/new")
        print("\033[1m" + logos[get_distro()] + "\033[0m " + OUTPUT)
else:
    print("\033[1m" + logos[get_distro()] + "\033[0m " + OUTPUT)
