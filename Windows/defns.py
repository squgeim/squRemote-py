#!/usr/bin/python

import config
from subprocess import check_output
from evdev import ecodes as e
from copy import deepcopy

k=e.ecodes
conf=config.conf
default={"Play-Pause":["playpause"],"Stop":["stopcd"],"Previous":["previoussong"],
    "Next":["nextsong"],"Seek-Left":["rewind"],"Seek-Right":["fastforward"],
    "Volume-Up":["volumeup"],"Volume-Down":["volumedown"],"Eject-Disk":["ejectcd"]}
_k=deepcopy(default)

for a in conf.keys():
  for s in conf[a]:
    d='KEY_'+s.upper()
    if d in k.keys():
      _k[a]=conf[a]
    else:
      _k[a]=default[a]
      

IP_ADDRESS = check_output("ifconfig wlan0 | grep \"inet addr\" | awk '{print $2}' | awk -F: '{print $2}'",shell=True)
PORT=9999
