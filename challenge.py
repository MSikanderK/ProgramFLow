choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below: ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
    choice = input()



# menu = ["Learn Python", "Learn Java", "Go swimming", "Have Dinner", "Go to bed"]
#
# chosen_menu = ""
# while chosen_menu not in menu:
#     print(menu)
#     chosen_menu = input("Please choose your option from the list below: ")
#     if chosen_menu.casefold() == "exit":
#         print("Goodbye")
#         break
# else:
#     print("You have chosen to {}".format(chosen_menu))