import random

name = input("Entrer le nomb de joueur : ")
print("salut " + name, ", es-tu prêt à risquer t'a vie pour un simple pari ?")
print("\n")
print("---------------------------------------------------------------------")
print("Bienvenue dans la roulette russe !")
print("Ton but est de survivre à travers un chargeur de 1911.. bonne chance !")

liste = ["C'estait Pas loin !", "Arg.. presque", "Ouf moins une !", "Haha la prochaine est pour toi", "essaie encore ?", "Ça sent le plomb .."]
random_index = random.randint(0,len(liste)-1)

print("letters"[random_index])

number = random.randint(1,10)
guess = int("guess")


while guess != number:
    guess = input("Tire une balle : ")

    if number < guess:
        print("reaction")
    elif number > guess:
        print("reaction")
    else:
        guess != number
        print("WASTED...")