PelOpen = open('pelican.txt', mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)
PelOpen2 = open('pelican.txt', mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)
PelRead = PelOpen.read()
PelLine = PelOpen2.readlines()
print(PelRead)
print('The file type is', type(PelRead), "\n")
print(PelLine)
print('There are', len(PelLine), 'items in the list\n')
for i in PelLine:
    print(i.rstrip("\n"))


