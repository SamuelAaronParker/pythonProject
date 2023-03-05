#!usr/bin/python

# Example Python Script

import sys  # imports the sys module in Python provides various functs and vari that are used to manip different parts
argc = len(sys.argv)

if argc > 1:  # if agrgc comes to move than 1 this will print out "Too many args"
    print("Too many args")
else:
    where = "world"  # creates a variable str for "where" to "world"
    print("Hello", where)  # prints Hello world

print("Goodbye from " +
      sys.argv[0])  # will say goodbye from your location. As this is local it will show the file address

print(argc)
