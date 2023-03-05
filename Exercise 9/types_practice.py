fname = "Sam"  # variable with a first name
sname = "Parker"  # variable with a second name
print(fname, "", sname)  # combines the two variables with an added space
namel = []  #creates a list
namel.append(fname+" "+sname)  # adds both name variables to the list "namel"
print(namel)  # prints the list
named = dict(First=fname, Last=sname)  # creates a variable for a dictionary
print(named)  # prints new created lists with "fname + sname"
named.pop("First")  # removes the first name from the dict
print(named)
