import random
# Rock Paper Scissors
# for this type picture visit ASCII art website on Google 🔻
# Rock
rock = """ rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """ paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """ scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list1 = [rock, paper, scissors]
user_choice = int(input("enter your choice 0 for rock, 1 for paper, 2 for scissors\n"))
computer_choice = random.randint(0, 2)
print("computer choice number ; ",computer_choice)

if user_choice < 0 and user_choice > 3:
    print(f"Invalid choice by user! computer choice is {computer_choice} so computer win!")
else:
    if user_choice == computer_choice:
        print("user_choice=",list1[user_choice])
        print("computer_choice=",list1[computer_choice])
        print("it's a draw!")

    elif user_choice > computer_choice:
        print("user_choice=",list1[user_choice])
        print("computer_choice=",list1[computer_choice])
        print("user's win!")

    elif user_choice < computer_choice:
        print("user_choice=", list1[user_choice])
        print("computer_choice=", list1[computer_choice])
        print("computer's win!")

    elif user_choice == 0 and computer_choice == 2:
        print("user_choice=", list1[user_choice])
        print("computer_choice=", list1[computer_choice])
        print("user's win!")


