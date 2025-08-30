import random
ran = random.randint(1,25)
attempts=0
while True:
    guess = int(input("enter your guessing number from (1 to 25):  "))
    if ran < guess:
        print(f"less than you think bro!!\n{ran}")
        attempts+=1
        continue
    elif ran>guess:
        print(f"greater than you think bro!!\n{ran}")
        attempts+=1
        continue
    else:
        print(f"you get it you \n wonnn broo\n{ran}")
        attempts+=1
        break

print(f"You got it in {attempts} attempts 🎉")
    