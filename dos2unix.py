# a script for execute files in a folder
import sys
import os
def dos2unix(path):
    if os.path.isdir(path):
        fns = [os.path.join(path, fn) for fn in os.listdir(path)]
        for fn in fns:
            dos2unix(fn)
    else:
        print("dos2unix %s" %path)
        os.system("dos2unix %s" %path)
dos2unix("./")
