#!/usr/bin/python

import sys
from cx_Freeze import setup,Executable


base=None
if sys.platform == "win32":
  base = "Win32GUI"

setup(name="squRemote",
  version="0.3",
  #options={"build-exe": build_options},
  description="squRemote - PC Driver",
  executables=[Executable("squRemote.py",base=base,icon="squRemote.ico")])
