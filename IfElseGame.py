import random
print("Guess a number")
h = random.randint(1, 20)
while (True):
    inp = int(input())
    if (inp < h):
        print("Wrong guess, try a greater number")
    elif (inp > h):
        print("Wrong guess, try a smaller number")
    else:
        print("Congrats, you have guessed it right.")
        break
