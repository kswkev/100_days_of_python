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

#Write your code below this line 👇
import random

rock_outcomes = ["Draw", "You loose, paper beats rock", "You win, rock beats scissors"]
paper_outcomes = ["You win, paper beats rock", "Draw", "You loose, scissors beats paper"]
scissors_outcomes = ["You loose, rock beats scissors", "You win, scissors beats paper", "Draw"]

outcomes = [rock_outcomes, paper_outcomes, scissors_outcomes]

display = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

print(display[user_choice])

print("Computer chose:")

print(display[computer_choice])

print(outcomes[user_choice][computer_choice])