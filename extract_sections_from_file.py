#!/usr/bin/env python

"""
Python 3.

Read a text file and copy the contents between two tags.
In this example the tags are START and END.
"""

import os
import re

with open(os.getcwd() + '/___sample-file.txt', \
          encoding="utf8") as infile, \
     open(os.getcwd() + '/___delete_me___.txt', 'w', encoding="utf8") as outfile:
    copy = False
    for line in infile:        
        if re.match("^START", line):
            # start the copy
            copy = True            
        elif line.strip() == "END":
            # we've found an empty line, so we stop the copy
            copy = False
        elif copy:
            outfile.write(line)
