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
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        print(filename)

pathbname = os.path.basename(pathf) #using this to remove file path
print(pathf)
print(pathbname)
