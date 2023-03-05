PelOpen = open('pelican.txt', mode='w', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)
with open('pelican.txt', 'a') as pelican:
    pelican.write('A wonderful bird is the pelican,\nHis bill holds more than his belican.\n')
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
with open('pelican.txt', 'a') as pelican:
    pelican.writelines(lines)
