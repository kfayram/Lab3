#RPS.py
#Name: Kyle Fayram
#Date: 2/8/25
#Assignment: Lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playAgain = "Y"
  while playAgain == "Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.

    #Randomly choose the computer between 'R', 'P', or 'S'  
    computer = random.choice(["Rock", "Paper", "Scissors"])
    #Prompt the user for their RPS selection
    player = input("Pick your weapon (Rock, Paper, Scissors): ")
    #Determine winner and state what happened to the user
    if computer == "Rock":
      print("Computer chose Rock")
    elif computer == "Paper":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")

    if player == "Rock":
      print("Player chose Rock")
    elif player == "Paper":
      print("Player chose Paper")
    else:
      print("Player chose Scissors")\
      
    if player == "Rock" and computer == "Rock":
      print("Tie!")
      ties = ties + 1
    if player == "Rock" and computer == "Paper":
      print("Computer wins.")
      losses = losses + 1
    if player == "Rock" and computer == "Scissors":
      print("You win!")
      wins = wins + 1

    if player == "Paper" and computer == "Rock":
      print("You win!")
      wins = wins + 1
    if player == "Paper" and computer == "Paper":
      print("Tie!")
      ties = ties + 1
    if player == "Paper" and computer == "Scissors":
      print("Computer wins.")
      losses = losses + 1

    if player == "Scissors" and computer == "Rock":
      print("Computer wins.")
      losses = losses + 1
    if player == "Scissors" and computer == "Paper":
      print("You win!")
      wins = wins + 1
    if player == "Scissors" and computer == "Scissors":
      print("Tie!")
      ties = ties + 1

    #Ask the user if they would like to play again.
    playAgain = input("Play again? (Y/N): ")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
