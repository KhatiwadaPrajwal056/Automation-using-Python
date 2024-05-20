# data types in python

# varibles
# particular name given to specify memory Location

# int_var = 6
# float_var =10.5
# str_var = "Python"
# bool = False
# # print(type(bool))
# # basic opeations 
# # total_sum = int_var + float_var
# # print(total_sum)
# # print(type(total_sum))
# # print(str_var+" Tutorial")

# # taking user input

# name = input("Enter your name: ") # input returns us a str )data type
# age = int(input("ENter your age: ")) 
# print(name)
# # change huna lai re assign garnuu parcha
# print(type(name))
# Your name is prajwal khatiwada

# print("Hi ",name, "your are",age,"years old")


# String::: 
# Formatted string::
# print(f"Hi {name} you are {age} years old")

# input , data types, str, formatted strings.
'''

commment # 
paragraph type  sfjkasbfsbbaf '''

# Control structures:: 
# 1. conditional statements
# 2. Loops (break and continue)

# 1. conditional statements : if, elif and else
# Checking a particular condition to perform certain task.

# num = 2
# # equal to ;;; ==
# # not equal ;;; !=
# # less than equal :: <=
# if num > 1000:
#     print("Yes it is Greater: ")
# elif num == 1000:
#     print("Yes it is")
# else:
#     print("Default one")

#loops: for loop , while loop
# repeatedly hune kura
# For loop : 


# for(i=0;i<5;i++){ i value ranges from 0 1 2 3 4
#     print(i);
#     i++;
# }
# in python number range kasari kaam garcha ::
# range function::
# range(5) 0 1 2 3 4 

# for i in range(5): 
#     print(i)

# while loop:
# num = 10
# while num > 5:
#     print(num)
#     num -= 1  # or num = num -1
#     10, 9
#     9,8
#     8,7
#     7,6
#     6,

# continue and break in loops::
## continue:: 
# for i in range(10): 
#     if i == 2:
#         continue # skips the rest of the loop when i == 2
#     # 2 le garda output audaina rey
#     if i == 7:
#         break # exits the loop
#     print(i) # 0 1 3 4 5 6   

# function in python: 
# for a operaion we make functions::

# function defining:
# create a function:: 
# def greeting(name):
#     print(f"Hello {name}")


# # function calling::
# # bolaunet or excute the function
# # input_name = input("ENter your name: ")
# # greeting(input_name)


# def addition(x,y):
#     sum = x+y
#     print(sum)
# num1 = int(input("Enter a first number:"))
# num2 =int(input("Enter a second number:"))
# addition(num1,num2)

# Data structures in python :: List , dictionary and tuple
# list1 = [1,2,3.4,2.4,True,"prajwal"]
# print(list1)

name = ["Prajwal","Rakesh","Gaurav",5,5.5,True]
# name.append("Mango")
# print(name)

# we can use loops in list 
# print(name[2:9])

# use list and for loop to make the square of the numner
# square_num = [i**2 for i in range(10)]
# print(square_num)

# tuples :
# my_tuple = (1,2,3,4,"etrr",True)

# print(my_tuple[0])

# dictionary::

my_dictionary = {
    "Name" : "Prajwal",
    "Fruit" : "Mango",
    "City" : "Dhapakhel",
    # "Name" : "hari" # this gets overrides in the dictionary

}
# for items, value in my_dictionary.items():
#     print(f"{items}:{value}")
# my_dictionary["Education"] = "COmputer Engineering"
# print(my_dictionary)

# my_dictionary = {
#     "Name" : "Prajwal",
#     "Fruit" : "Mango",
#     "Address" : {
#         "Country" : "Nepal",
#         "City" : "Ktm",
#         "District" : "Sunsari"
#     },
#     # "Name" : "hari" # this gets overrides in the dictionary

# }
# print(my_dictionary["Address"].keys())

# loop in dictionary :


# Error haldling:: try catch throw
# try:
#     num = int(input("Enter a number: "))
#     print(num)
# except ValueError:
#     print("You entered the different value: ")

# diving two numbers::
# x/y

# user y = 0???? math error??
# x = 10
# y = 0
# try:
#     print(x/y)
# except ZeroDivisionError:
#     print("Undefined or denominator cannot be zero")

# we have lots of file.
# txt. exe. py. anthing

# performing different opeartions in files..
# read write 
# modes in file handling::
# read (r) : opens a file for reading. FIle must exits
# write(w): opnes file for writing. creats if doesnot exists.
# binary read(rb): reads in binary format, file nust exist. decode
# binary write(wb): opnes file for binary writing. creats if doesnot exists. encode
import os
# traditional wway
# with open("example.txt","w") as file:
#     file.write("hello there")

# with open("/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/Automation-using-Python/python basics/example.txt","r") as file:
#     content = file.read()
#     print(content)

# with open("/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/Automation-using-Python/python basics/binary.bin","wb") as file:
#     msg="Hello this is binary file"
#     # file.write(b.msg) # or
#     file.write(msg.encode())
















# list in loop wala

# list indexing

# key value pair 

# os ko functionality.
# 