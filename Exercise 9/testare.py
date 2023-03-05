# name = input("Tell me your name: ")
# age = input("and your age: ")
# print(name, "you are",age)

# calc the area of a circle

# radius = input("Enter the radius of your circle(m): ")
# area = 3.142*int(radius)**2
# print("the area of your circle is:", area)
# num1 = 3.14256789
# num2 = 10.2903948

#  print("num1 is",num1, "and num2 is",num2)

# Format method
#  print("num1 is {0:.3f} and num2 is {1:.3f}".format(num1, num2))

#  using f-strings
# print(f"num1 is {num1:.4f} and num2 is {num2:.4f}")

# age = int(input("Enter your age: "))
# if age < 10:
#     print("Your too young to continue")
# elif age < 40:
#     print("Your an oldy")
# else:
#     print("you are closer to death than the rest")


#Operators
# <, >, ==, !=, =>, =<
# meaty = input("Do you eat meat? (y/n):")
#
# if meaty == "y":
#     print("Here is the meat menu")
# else:
#     print("Here is the veg menu")

# ninjas = ["Ryu","Crystal", "yoshi", "Ken"]
#
# # for ninja in ninjas:
# #     print(ninja)
#
# # for ninja in ninjas[1:3]:
# #     print(ninja)
#
# for ninja in ninjas:
#     if ninja == "yoshi":
#         print(f"{ninja} - black belt")
#         break
#     else:
#         print(ninja)

# age = 25
# num = 0
#
# while num < age:
#     if num == 0:
#         num += 1
#         continue
#     if num % 2 == 0:
#         print(num)
#     if num > 10:
#         break
#     num +=1

# for n in range(5):
#     print(n)
# for n in range(3,10):
#     print(n)
# for n in range(0,20,4):
#     print(n)
# burgers = ["beef", "chicken", "veg", "supreme", "double"]

# for n in range(len(burgers)):
#     print(n,burgers[n])

# for n in range(len(burgers) -1, -1, -1):
#     print (n, burgers[n])

# def greet(name = "ryu", time = "morning"):
#     print(f"Good {time} {name}, hope you are well")
# # name = input("enter your name: ")
# # time = input("enter the time of day: ")
#
# greet(name="sam")

# def area(radius):
#     return 3.142 * radius * radius
# def vol(area, length):
#     print(area * length)
# radius = int(input("Enter a radius: "))
# area(radius)
# length = int(input("Enter a length: "))
#
# vol(area(radius), length)

my_name = "ryu"

def print_name():
    my_name = "Sam"
    print("the name ins the the function is", my_name)
print_name()
print("outside the func the name is", my_name)