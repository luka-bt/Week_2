name = input("Hello, what is your name? ")

print("Hello " + name)
ques = input("Do you want to know the date " + name + "? ")

from datetime import date
now = date.today()

if ques == "yes":
    print(now)

if ques == "no":
    print("Okay, Have a good day")