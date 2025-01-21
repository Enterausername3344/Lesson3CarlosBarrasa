#Randomizing
from random import choice
#Virtual Bartender
drinks = ["Vodka", "Whiskey", "Gin", "Tequila", "Rum", "Rakia", "Sake"]
print("Welcome to the virtual pub")
name = input("I am the virtual bartender, What is your name?" )
try:
    age=input(f"How old are you, {name}" )
    age= int(age) #try to convert to a number
    if age >=21:
        legal=True
    elif age < 16:
        legal = False
    else:
        country= input(f"Based on your age, I need to ask Where you are from, {name}?" )
        legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and country != "USA":
        legal = True
    elif age>= 16 and country == "Luxembourg":
        legal = True
    if age >120 or age < 5:
        print("Please do not lie to the virtual Bartender")
    elif legal:
        print("You are allowed to drink")
        print(f"Here is a {choice(drinks)} for you")
    else:
        print(f"Dear {name}, unfortunately I am not allowed to serve you")
except ValueError:
    print( "Please give a valid age")