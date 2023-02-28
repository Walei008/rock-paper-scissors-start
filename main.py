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
choice=input("What do you choose?Type 0 for rock,1 for paper,2 for scissors")
separate_choice=choice.split(",")
choice_num=len(choice)
random_choice=random.randint(0,2)
if random_choice==0:
  print("i choose rock ")
  if random_choice==1:
    print("i choose paper")
else:print("i choose scissors")

