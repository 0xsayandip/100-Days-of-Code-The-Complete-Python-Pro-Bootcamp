import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


letter=1
symbol=1
number=1
password=""
for i in range(1,nr_letters+nr_numbers+nr_symbols+1):
  r=random.randint(1,3)


  if r==1 and letter<=nr_letters:
    random_letter=letters[random.randint(0,len(letters)-1)]
    password=password+random_letter
    letter+=1
    print(password)


  if r==2 and symbol<=nr_symbols:
    random_symbol=symbols[random.randint(0,len(symbols)-1)]
    password=password+random_symbol
    symbol+=1
    print(password)


  if r==3 and number<=nr_numbers:
    random_number=numbers[random.randint(0,len(numbers)-1)]
    password=password+random_number
    number+=1
    print(password)




print(password)

