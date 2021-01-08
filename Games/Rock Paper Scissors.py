
import random

input("Welcome to Rock, Paper, Scissors! Press Enter to start.")
print()
choices = ["rock", "paper", "scissors"]

while True:
  random_index = random.randint(0,2)
  cpu_choice = choices[random_index]

  user_choice = input("Rock, Paper, or Scissors? ").lower()
  while user_choice not in choices:
    user_choice = input("That is not a choice. Please try again: ").lower()
  
  print()
  print("Your choice:", user_choice)
  print("Computer's choice:", cpu_choice)
  print()

  if user_choice == 'rock':
    if cpu_choice == 'rock':
      print("It's a tie!")
    elif cpu_choice == 'scissors':
      print("You win!")
      
    elif cpu_choice == 'paper':
      print("You lose!")
      
  elif user_choice == 'paper':
    if cpu_choice == 'paper':
      print("It's a tie!")
    elif cpu_choice == 'rock':
      print("You win!")
      
    elif cpu_choice == 'scissors':
      print("You lose!")
      
  elif user_choice == 'scissors':
    if cpu_choice == 'scissors':
      print("It's a tie!")
    elif cpu_choice == 'paper':
      print("You win!")
      
    elif cpu_choice == 'rock':
      print("You lose!")

  repeat = input("Play again? (Y/N) ").lower()
  while repeat not in ['y', 'n']:
    repeat = input("That is not a valid choice. Please try again: ").lower()
  
  if repeat == 'n':
    break
