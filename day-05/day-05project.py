import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [
    "!","@","#","$","%","^","&","*","(",")","-","_","=","+",
    "[","]","{","}",";",":","'",",","<",">","/","?","|","`","~"
]
print("Welcome to the py password generator !")
nr_letters = int(input("How many letters you want in your password? \n"))
nr_symbols = int(input("How many symbols you want in your password? \n "))
nr_numbers = int(input("How many numbers you want in your password? \n"))

password = ""
#Easy level
for char in range(0,nr_letters):
    password += random.choice(letters)
for char in range(0,nr_symbols):
    password += random.choice(symbols)
for char in range(0,nr_numbers):
    password += random.choice(numbers)
print(password)

#hard level
# to mix the letters ,symbols and numbers in password we use list . first store everything in list then use the shuffle operations
list_password = []
for char in range(0,nr_letters):
    list_password.append(random.choice(letters))
for char in range(0,nr_symbols):
    list_password.append(random.choice(symbols))
for char in range(0,nr_numbers):
    list_password.append(random.choice(numbers))
#print(list_password)
random.shuffle(list_password)
#print(list_password)

final_password = ""
for char in list_password:
    final_password += char

print(final_password)

