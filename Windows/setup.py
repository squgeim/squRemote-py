#!/usr/bin/python

import sys
from cx_Freeze import setup,Executable

base=None

setup(name="squRemote",
version="0.1",
description="my app",
executables=[Executable("squRemote.py",base=base)])
