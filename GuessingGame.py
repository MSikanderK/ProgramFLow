import random

highest = 1000
answer = random.randint(1,highest)
# print(answer)
guess = 0 #forst number so its foin
print("Please guess a number between 1 and {}:".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("Goodbye")
        break
    if guess == answer:
        print("Well Done!")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else: #>answer
            print("please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("well done!")
        # else:
        #     print("Your are wrong")
        #



