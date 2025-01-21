name= input("What is your name? ")
print("Hello", name)
age = input("How old are you? ")
try:
    #Another way to format print is via f-strings
    print(f"{name},you were born in {2024-int(age)}")
    division=int(age)/1
except ValueError:
    print(f"The value you typed was {age}")
    print("Age must be a valid number")
except ZeroDivisionError:
    print("You can't divide by zero")
except: #All other types of errors
    print("No idea what else can go wrong, but just in case")
else: #In case for no exception happened
    print("Thanks for being a good sport and not trying to crash the app")
print("thanks for playing")