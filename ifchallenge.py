name = input("What is your name? ")

age = int(input("How old are you? "))

if 18 <= age <= 30:
    print("Welcome to the 18-30 holdiay {}".format(name))
else:
    print("Fuck off!")