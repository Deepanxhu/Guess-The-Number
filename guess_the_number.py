import random

target = random.randint(1,100)

while True:
    userChoice = int(input("Guess the Number: "))
    if(userChoice == target):
        print("Correct Guess !!")
        break
    elif(userChoice > target):
        print("Your Number is too big, Take a smaller guess...")
    else:
        print("Your Number is too small, Take a bigger guess...")

print("-----GAME OVER-----")