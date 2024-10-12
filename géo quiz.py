S = "sahara"
A = "asie"
O = "océan pacifique"
G = "groenland"
T = "tokyo"

while True:
    start = input("Nous allons tester tes connaissances en géographie, es-tu prêt ? :").strip().lower()
    faux = "Faux, la réponse est:"
    vrai = "Bien joué!"

    # Lancer le quiz uniquement si la réponse est "oui"
    if start == "oui":
        print("Commençons le quiz.")

        # question 1
        désert = input("Quel est le plus grand désert chaud du monde ? :").strip().lower()
        if S in désert:
            print(vrai)
        else:
            print(faux + " Le Sahara")

        # question 2
        continent = input("Quel est le plus grand continent du monde ? :").strip().lower()
        if A in continent:
            print(vrai)
        else:
            print(faux + " l'Asie")

        # question 3
        océan = input("Quel est le plus grand océan du monde ? :").strip().lower()
        if O in océan:
            print(vrai)
        else:
            print(faux + " l'océan pacifique")

        # question 4
        ile = input("Quelle est la plus grande île du monde ? :").strip().lower()
        if G in ile:
            print(vrai)
        else:
            print(faux + " le Groenland")

        # question 5
        capitale = input("Quelle est la capitale du Japon ? :").strip().lower()
        if T in capitale:
            print(vrai)
        else:
            print(faux + " Tokyo")

        # Demander si l'utilisateur veut rejouer
        rejouer = input("Veux-tu rejouer ? (oui/non) :").strip().lower()
        if rejouer != "oui":
            print("Au revoir !")
            break
    else:
        print("Tu n'as pas répondu 'oui'.")
