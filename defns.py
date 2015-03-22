#!/usr/bin/python

from k import k as keys
from subprocess import check_output
from evdev import ecodes as e

k=e.ecodes

IP_ADDRESS = check_output("ifconfig wlan0 | grep \"inet addr\" | awk '{print $2}' | awk -F: '{print $2}'",shell=True)
PORT=9999
