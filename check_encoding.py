#!/usr/bin/env python

"""
Python 3.

Check file encoding.
"""

import sys
import os

try:
  with open(os.getcwd() + '/___sample-file.txt', \
            encoding="utf8") as infile:
    for line in infile:
      print (line)
except UnicodeDecodeError:
  print("Error opening " + os.getcwd() + '/___sample-file.txt' \
        + ". Check encoding.")
  sys.exit(1)
