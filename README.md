# compactfetch
![Written on Python](https://img.shields.io/badge/Written%20on-Python-informational?logo=python&style=flat&logoColor=f1ff85&color=f1ff85&labelColor=0062ff)
![Version 1.0](https://img.shields.io/badge/Version-1.0-informational?logo=&style=flat&logoColor=2b2b2b&color=2b2b2b&labelColor=00ff4c)<br>
Smallest ever fetch, that can exist, written in Python
<img height="100%" src="./screenshots/fastfetch_and_compactfetch.png">
## Using
### Method 1. Installing it
```
git clone https://github.com/msh356/compactfetch
cd compactfetch
chmod +x main.py
```
and run it:
```
./main.py
```
or add to /usr/local/bin (where all user programs stored):
```
chmod +x topath.sh
sudo ./topath.sh
```
### Method 2. Using without install
Compactfetch can work anywhere from one Python file, so we can use it without installing:
```
curl -s https://raw.githubusercontent.com/msh356/compactfetch/refs/heads/master/main.py | python3 -
```
This command will get last compactfetch commit and run it.
## Settings
You can open source code (if you installing) and search for SETTINGS SECTION. There is three variables:
```
OVERRIDE_DISTRO = None
OUTPUT = "\033[1mDistro: \033[0m" + get_distro()
ALLOW_KITTY_IMAGES = False
```

Let's see every parameter
### OVERRIDE_DISTRO
Used for testing distro logos. Possible values:
- None: no overriding distro
- Distro name (str): behave as if OVERRIDE_DISTRO is your distro

### OUTPUT
Used for customizing string after distro logo

### ALLOW_KITTY_IMAGES
Used for PNG logos. Possible values:
- False: print ASCII logos
- True: print kitty logos (in normal terminals will be an empty string)

## Credits
Terminal logos by <a target="_blank" href="https://icons8.com">Icons8</a>
