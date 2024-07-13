import random

my_list = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]
userChoice = int(
    input("Take your choice, '0 for rock, 1 for paper and 2 for scissors': "))
if (userChoice > 2):
    print("invalid choose upto 2")
randomNumber = random.randint(0, 2)
computerChoice = my_list[randomNumber]
if userChoice < 3 and userChoice >= 0:
    print(f"your choice is\n {my_list[userChoice]}")
print(f"computer choice is \n {computerChoice}")
if userChoice > 3 or userChoice < 0:
    print("input the valid number")
elif userChoice == 0 and randomNumber == 2:
    print("you won")
elif randomNumber == 0 and userChoice == 2:
    print("you lose")
elif randomNumber > userChoice:
    print("you lose ")
elif userChoice > randomNumber:
    print("you won")
elif userChoice == randomNumber:
    print("you made a boo-boo")
else:
    print("enter the valid statement")