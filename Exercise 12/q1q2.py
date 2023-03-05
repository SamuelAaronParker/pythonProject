# Question 1
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += [
    'Oke']  # if we don't add the [] the add will treat the Oke as a sequence and add each individual letter to the list
cheese += ['Nacho Cheese', 'Halloumi']
print(cheese)

# Question 2
tup = 'Hello'
tup2 = 'Hello',
tup3 = 'Hello', 'World'
print(len(tup))  # printing the first tup counts the letters within hello with the len function
print(len(tup2))  # printing the second tup counts the tuple items. By adding the "," turns the array into a tuple
print(len(tup3))  # We can see this is a tuple by adding multiple items to the tuple and getting a count of two items