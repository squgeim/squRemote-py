#!/usr/bin/python

import defns
from evdev import UInput,  UInputError as err

def simulate(val):
  x={"play":"Play-Pause","stop":"Stop","prev":"Previous",
    "next":"Next","slft":"Seek-Left","srht":"Seek-Right",
    "vup":"Volume-Up","vdwn":"Volume-Down","ejct":"Eject-Disk"}
  if val[-1]=='0':call(x[val[:-1]],True)
  else: call(x[val])

def call(k,conf=False):
  if conf:
    keys=defns._k[k]
  else:
    keys=defns.default[k]
  try:
    ui = UInput()
    for key in keys:
      ui.write(defns.k["EV_KEY"], defns.k["KEY_"+key.upper()], 1)
    defns._k[k].reverse()
    for key in keys:
      ui.write(defns.k["EV_KEY"], defns.k["KEY_"+key.upper()], 0) 
    ui.syn()
    ui.close()
  except err:
    print "Not enough permissions. Are you root?"
