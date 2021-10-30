#!/usr/bin/env python

"""
Python 3.

Read a text file replace " by '
"""

import os

double_quote = "\""

with open(os.getcwd() + '/___sample-file.txt', \
          encoding="utf8") as infile, \
     open(os.getcwd() + '/___delete_me___.txt', 'w', encoding="utf8") as outfile:
    for line in infile:
        outfile.write(line.replace(double_quote, "'"))
