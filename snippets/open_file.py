#!/usr/bin/env python

"""
Python 3.

Ask for a filename using tkinter, the standard Python interface
to the Tk GUI toolkit.
"""

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

print ("file path: " + file)
