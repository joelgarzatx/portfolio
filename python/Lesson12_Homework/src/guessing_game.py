import random

secret = random.randint(1,99)
usertry = 0

while usertry < 5:
    uin = int(input("Guess a number: "))
    usertry += 1
    if uin == secret:
        print("Correct! Well done, the number was", secret)
        break
    elif usertry == 5:
        print("Sorry, the number was", secret)

    elif uin < secret:
        print("Guess higher")
    elif uin > secret:
        print("Guess lower")
    