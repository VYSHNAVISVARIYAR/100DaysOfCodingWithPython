import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','#', '$', '%', '&','*', '@','^']
numbers = ["1","2","3","4","5","6","7","8","9","0"]

num_letters = int(input("How many letters would you like to include in your password?"))
num_symbols = int(input("How many symbols would you like to include?"))
n_numbers = int(input("How many numbers would you like to include?"))

password_list = []
for char in range(0,num_letters):
    password_list += random.choice(letters)
for char in range(0,num_symbols):
    password_list += random.choice(symbols)
for char in range(0,n_numbers):
    password_list += random.choice(numbers)
# print(password_list)

random.shuffle(password_list)
# print(password_list)

#to convert it to a string
password = ""  
for char in password_list:
    password += char
print("Your password is:",password)