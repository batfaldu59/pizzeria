def afficher(collection, nb_demander_pizza=-1):
    collection_pizza = collection
    if not nb_demander_pizza == -1:
        collection_pizza = collection[:nb_demander_pizza]

    nb_pizza = len(collection_pizza)
    if nb_pizza == 0:
        print("AUCUNE PIZZAS")
        return

    print(f"---- LISTE DES PIZZAS ({nb_pizza}) ----")
    for pizza in collection_pizza:
        print(pizza)
    print()
    print(f"Première pizza: {collection_pizza[0]}")
    print(f"Dernière pizza: {collection_pizza[-1]}")


def ajouter_pizza_utilisateur(collection):
    pizza_utilisateur = input("Pizza à ajouter: ")
    if pizza_utilisateur.lower() in collection:
        print("ERREUR: la pizza existe déja!")
    else:
        collection.append(pizza_utilisateur)


pizzas = ["Orientale", "Americaine", "Hawai", "Calzone"]
ajouter_pizza_utilisateur(pizzas)
afficher(pizzas, 3)