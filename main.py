import random

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

rps = [rock, paper, scissors]

player = int(input("Type 0 for rock, Type 1 for paper or Type 2 for scissors?\n "))


computer = random.randint(0, 2)

print("Computer choise: ")
if player >= 5 or player < 0 :
  print("You typed an invalid number, you lose!")
elif player == 0 and computer == 2 :
  print(rps[computer])
  print(rps[player])
  print("You win!")
elif computer == 0 and player == 2 :
  print(rps[computer])
  print(rps[player])
  print("You lose")
elif computer > player:
  print(rps[computer])
  print(rps[player])
  print("You lose")
elif player > computer:
  print(rps[computer])
  print(rps[player])
  print("You win!") 
elif computer == player :
  print(rps[computer])
  print(rps[player])
  print("It's a draw")
  
  