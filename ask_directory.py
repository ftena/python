# Python 3
# Ask for a output directory tkinter, the standard Python interface
# to the Tk GUI toolkit.

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory(title='Choose output folder')

print ("dir path: " + directory)
