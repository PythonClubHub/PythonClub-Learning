# It's not finished   ... work in progress...
# Take a look if you want and make suggestions

from tkinter import *
import os
import sys
from tkinter import messagebox
#import git

Value = 0
git_dir = ""


def MessageBox():
    import tkinter.messagebox
    tkinter.messagebox.showinfo(title="!", message="Error, directory does not exist")

def ask_directory():
    import tkinter.filedialog as fd
    root = Tk()
    root.withdraw()

    
    currdir = os.getcwd()
    path = fd.askdirectory(parent=root, initialdir=currdir, title="Please select a directory")
    if not path:
        messagebox.showerror("Status","Folder not Selected")
        sys.exit("File not selected")

    return path

def isDir(filename):
    # Verify if source file is a directory

    new_directory = os.path.join(directory, filename)   # Getting source directory path


    isdir_ = os.path.isdir(new_directory)               # Verify if file is a directory (True or False)
    
    if isdir_:
        print("Inside source folder")
        for filename in os.listdir(new_directory):      # For each file in source directory
            if filename[:5] == "meta-":                 # Verify if "meta-" file exist
                directory_pull = os.path.join(new_directory, filename) # From this path we need to make git pull
                #print("Inside meta folder")
                #g = git.cmd.Git(git_dir)
                #g.pull()
                #print("I've made a git pull from", git_dir)
                #print("")


directory = os.path.join(r"", ask_directory())
print("Your directory: ",directory)

for filename in os.listdir(directory):
    if filename == "source":
        Value = 1
        isDir(filename)

if Value == 0:
    MessageBox()

