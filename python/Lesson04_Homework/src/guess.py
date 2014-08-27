# The fun part here was matching the output, and not printing the hint to guess higher or lower on the fifth try.
secret = 12
usertry = 0

while True:
    uin = int(input("Guess a number: "))
    usertry += 1
    if uin == secret:
        print("Correct! Well done, the number was", secret)
        break
    elif usertry == 5:
        print("Sorry, the number was", secret)
        break
    elif uin < secret:
        print("Guess higher")
    elif uin > secret:
        print("Guess lower")
    
    
