import random

print("Can you beat the computer? Let's find out!")
print("You will be asked to select a word: rock, paper, or scissors. Type the word but don't use capitals.")
print("Let's begin!")

while True:
    #create a list of play options
    RPS = ["Rock", "Paper", "Scissors"]
    player = input("rock, paper, or scissors?")
    computer = random.choice(RPS)
    
    if (computer=="paper" and player == "rock") or (computer=="rock" and player == "scissors") or (computer=="scissors" and player == "paper"):
        print("You chose: ", player)
        print("Computer chose: ", computer)
        print("Bad luck, computer wins!")
        
    #same for other two outcomes? what are they?
    
    #error case
 