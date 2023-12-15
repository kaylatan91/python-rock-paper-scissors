# Rock, Paper, Scissors Design
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Game Logic

# Random generator
import random

# RULES:
    # Rock wins against scissors
    # Scissors wins against paper
    # Paper wins against rock
print("Welcome to Rock, Paper, Scissors!")

# Prompt for player
# Turning the input into an integer
game_images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number. You lose :(")
else:
  print(game_images[player_choice])

# Random generator for computer player
random_choice = random.randint(0, 2)
print("Computer chose: \n")
print(game_images[random_choice])

if player_choice == 0 and random_choice == 2:
    print("You won!")
elif random_choice == 0 and player_choice == 2:
    print("You lose :(")
elif random_choice > player_choice:
    print("You lose :(")
elif player_choice > random_choice:
    print("You win!")
elif player_choice == random_choice:
    print("It's a draw!")

