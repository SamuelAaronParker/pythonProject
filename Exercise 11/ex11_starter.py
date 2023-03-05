#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
#Task 1
BelgiumHyphens = '-' * len(Belgium)
print(BelgiumHyphens)

#Task 2
BelgiumColons = Belgium.replace(",",":")
print(BelgiumColons)

#Task 3

BelgiumList = Belgium.split(",")
# BelgiumPop = int(BelgiumList[1]) + int(BelgiumList[3])
print(f"Pop= {int(BelgiumList[1]) + int(BelgiumList[3])}")

