import random

randomNum = random.randint(1, 10)
playerName = input("Please Enter You Name. \n")
print('Hi '+ playerName+ '. I am Picking a number between 1 and 10. Let\'s see from how many attempts you can guess it.\nYou have only 3 attempts :)')

attempts = 0
while attempts<3:
    pickedNum = int(input())
    attempts += 1
    if pickedNum < randomNum:
        print("Sorry:( Your guess is low from my picked number")
    elif pickedNum > randomNum:
        print("Sorry:( Your guess is high from my picked number")
    elif pickedNum == randomNum:
        print('Congratulations! You guessed the number in ' + str(attempts) + ' attempts!')
        break

if pickedNum != randomNum:
    print('Sorry you did not guess the number. The number was ' + str(pickedNum))