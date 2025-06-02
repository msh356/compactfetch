#!/bin/bash
if [ $EUID -ne 0 ]; then
	echo "[!] Please, run as root"
	exit 1
fi
chmod +x main.py
cp main.py /usr/local/bin/compactfetch
echo "[*] Now you can run compactfetch from terminal, just"
echo "[*] entering compactfetch in terminal. Restart your"
echo "[*] shell to effect changes, and check if"
echo "[*] /usr/local/bin is being in your \$PATH. Enjoy!"
