#!/usr/bin/python

#import defns
from k import keys
from evdev import UInput,  UInputError as err
from evdev.ecodes import ecodes

def simulate(val):
  '''
  The simulate function is the function that processes the input received.
  It splits the input seperated by + and sends the list to call function.
  '''
  vals=val.split('+')
  for v in vals:
    if v not in keys.keys():
      return 0
  call(vals)

def call(vals):
  '''
  The call function receives a list of keys to be pressed and loops over
  them switching them to pressed state, then loops over the reversed list
  unpressing them. That way it can process key combinations.
  '''
  try:
    ui = UInput()
    for k in vals:
      ui.write(ecodes["EV_KEY"], ecodes["KEY_"+keys[k]], 1)
    vals.reverse()
    for k in vals:
      ui.write(ecodes["EV_KEY"], ecodes["KEY_"+keys[k]], 0)
    ui.syn()
    ui.close()
  except err:
    print "Not enough permissions. Are you root?"
    #tkMessageBox.showerror("Permissions Needed","Not enough permissions, are you root?")
    #sys.exit(1)

if __name__ == '__main__':
  print "This is a module for the squRemote app. It is not meant to be executed independently."
