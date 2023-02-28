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
user_choice=int(input("What do you choose?Type 0 for rock,1 for paper,2 for scissors."))


computer_choice=random.randint(0,2)
print(f"computer chose {computer_choice}")
if user_choice==0 and computer_choice==2:
  print("you win")
elif computer_choice>user_choice:
  print("You lose")
elif computer_choice==user_choice:
  print("its a draw")
elif computer_choice==0 and user_choice==2:
   print("you lose")
elif user_choice>computer_choice:
  print("you win")
  

        
    