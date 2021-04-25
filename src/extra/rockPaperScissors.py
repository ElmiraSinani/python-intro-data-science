import random

options = ["Rock", "Paper", "Scissors"]

attempts = 0
playerScore = 0
compScore = 0
maxAttempts = 3  #don't count tie an wrong typed options
while attempts<maxAttempts:
    inputedOption = input("Please type one of this options: Rock, Paper or Scissors\n")
    randomNum = random.randint(0, 2)
    randomOption = options[randomNum]
    attempts += 1
    if inputedOption == randomOption:
        print("Tie! Equal options. Try again.")
        attempts -= 1
    elif inputedOption == 'Rock':
        if randomOption == 'Paper':
            print("You win!", "Random Option was ", randomOption)
            playerScore += 1
        else:
            print("You lose!", "Random Option was ", randomOption)
            compScore += 1
    elif inputedOption == 'Paper':
        if randomOption == 'Rock':
            print("You win!", "Random Option was ", randomOption)
            playerScore += 1
        else:
            print("You lose!", "Random Option was ", randomOption)
            compScore += 1
    elif inputedOption == 'Scissors':
        if randomOption == 'Paper':
            print("You win!", "Random Option was ", randomOption)
            playerScore += 1
        else:
            print("You lose!", "Random Option was ", randomOption)
            compScore += 1
    else:
        print("Wrong option. Please input your option again")
        attempts -= 1

print("\n\nScore-> You: ", playerScore, "; Comp: ", compScore)

