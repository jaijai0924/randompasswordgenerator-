#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letters_lenght = len(letters)
numbers_length = len(numbers)
symbols_length = len(symbols)
#create a letters list to contain the random values going in 

#This picks a random choice up top 

#Password list that the symbols/numbers/letters will go into
password = []
#For loop that only loops up to the amount of letters/numbers/symbols I want 
for i in range(0,nr_letters):
  #This is what gives me the random choice picks a number between 0 and the list - 1 
  random_choice = random.randint(0,letters_lenght-1)
  chosen_letter = letters[random_choice]
  password += chosen_letter

for i in range(0,nr_symbols):
  random_choice = random.randint(0,symbols_length-1)
  chosen_symbol = symbols[random_choice]
  password += chosen_symbol

for i in range(0,nr_numbers):
  random_choice = random.randint(0,numbers_length-1)
  chosen_number = numbers[random_choice]
  password += chosen_number

random_password = ''.join(random.sample(password,len(password)))

####random.choice????
###random.shuffle

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#This takes my letter password list and joins them together 
print(''.join(password))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password = ''.join(random.sample(password,len(password)))

print(random_password)
