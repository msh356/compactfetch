#!/bin/python3
import platform

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
            return "N/A"
    else:
        return override_distro

OVERRIDE_DISTRO = None
OUTPUT = "\033[1mDistro: \033[0m" + get_distro()

logos = {
    # --SPECIAL LOGOS--
    "N/A": "\033[38;2;180;180;180mN",
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

print("\033[1m" + logos[get_distro()] + "\033[0m " + OUTPUT)
