""" this is a  program that asks the user to enter their name and
their age.
Printing out a message addressed to them that tells them
the year that they will turn 100 years old"""

import datetime


def User():
    name = input("Give me your name: ")
    age = int(input("give me your age: "))
    p = (datetime.datetime.now())
    if age < 100:
        years_left = int(100)-int(age)
        print("hello {} you will turn 100 after {} from {}".format(name, years_left, p))
    elif age == 100:
        print("you are ok! enjoy your live bonus")
    else:
        print("Error!!")
User()






