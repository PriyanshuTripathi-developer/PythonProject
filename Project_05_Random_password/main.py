import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()][}[{]];',./:"

lenght_password =int(input("Enter the lenght of the password: "))

a = "".join(random.sample(password , lenght_password))

print(f"Your passsword is: {a}")