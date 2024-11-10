import random

# Mot de passe généré automatiquement entre 8 et 12 caractère
password_length = random.randint(8,12)
# Ensemble de tous les caractères pouvant se trouver dans le mot de passe
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
# Le mot de passe est généré aléatoirement
password = "".join(random.choices(password_chars, k=password_length))

# texte de mise en page 
print("Le nouveau mot de passe sera généré entre 8 et 12 caractère. Ni plus, ni moins ! ")
print("--------------------------------------------------------------------------------------")
print("Le mot de passe est :",password)
print("Il contient" ,password_length,"caractères... Enregistre le bien !")