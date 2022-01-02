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

#Write your code below this line 👇

User_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
counter=0
print("\n Your Choice is:\n")
if User_input==0:
  print(rock)
elif User_input==1:
  print(paper)
elif User_input==2:
  print(scissors)
else:
  print("Wrong Start Again")
  counter=1


if counter==0 :
  liss=[0,1,2]
  random_ch=random.randint(0,2)
  comp_input=liss[random_ch]

  print("\n Computer Choice is:\n")
  if comp_input==0:
    print(rock)
  elif comp_input==1:
    print(paper)
  elif comp_input==2:
    print(scissors)


  if comp_input ==  User_input:
    print("Its a Draw✌️")
  elif comp_input==0 and User_input==1:
    print("You Won!!😍")
  elif comp_input==0 and User_input==2:
    print("You Lost!!😞")
  elif comp_input==1 and User_input==0:
    print("You Lost!!😞")
  elif comp_input==1 and User_input==2:
    print("You Won!!😍")
  elif comp_input==2 and User_input== 0:
    print("You Won!!😍")
  elif comp_input==2 and User_input==1:
    print("You Lost!!😞")
