#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


let=""
#generic meathod where picking first n numbers
#for i in range(0,nr_letters):
  #let=let+letters[i]

  #random way
for i in range(0,nr_letters):
  let=let+random.choice(letters)


num=""
for i in range(0,nr_numbers):
  num=num+ random.choice(letters)


sym=""
for i in range(0,nr_symbols):
  sym=sym+random.choice(symbols)
let=let+sym+num
#print(let)
l=list(let)
random.shuffle(l)
result="".join(l)
print(f"Your password is {result}")
