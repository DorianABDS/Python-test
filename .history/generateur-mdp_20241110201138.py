import random

password_length = random.randint(8,12)
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password = "".join(random.choices(password_chars, k=password_length))

print("Ton nouveau mot de passe est :",class color:
    password = '\033[92m',"et contient" ,password_length,"caractères")
print("Enregistre le bien !")

class color:
    password = '\033[92m'