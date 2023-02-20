import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

path = "../Python challenges/"
pathf = '../Python challenges/Filefind2.py'
size = os.path.getsize(pathf)

print("Size (In bytes) of '%s':" % pathf, size)
print(os.listdir(path))

for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    # print(filepath)
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        print(filename)

pathbname = os.path.basename(filename)

print(pathbname)
# TODO: Use the glob.glob() function to obtain the list of filenames

# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that do not have a size of zero

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
