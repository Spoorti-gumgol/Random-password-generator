import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))

#Hard level:
pas = ""
password = []
hard_password = ""
tot = nr_letters + nr_numbers + nr_symbols
for pl in range(0, nr_letters):
    let = random.choice(letters)
    password.append(let)
    pas = pas + let
    
#print(pas)
for ps in range(0, nr_symbols):
    sym = random.choice(symbols)
    password.append(sym)
    pas = pas + sym

#print(pas)
for pn in range(0, nr_numbers):
    num = random.choice(numbers)
    password.append(num)
    pas = pas + num

#print(f"Your random password generated is: {pas}")
for passw in range(0, tot):
    hp = random.choice(password)
    hard_password += hp

print(f"Your random password generated is: {hard_password}")





