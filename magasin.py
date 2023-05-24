from ordinateur import Ordinateur

class Magasin:
    def __init__(self):
        self.ordinateurs = []

    def ajouter_ordinateur(self):
        marque = input("Marque : ")
        modele = input("Modèle : ")
        stock = int(input("Stock : "))

        ordinateur = Ordinateur(marque, modele, stock)
        self.ordinateurs.append(ordinateur)

        print("\nNouvel ordinateur ajouté avec succès !")

    def consulter_details(self):
        if not self.ordinateurs:
            print("\nAucun ordinateur n'est disponible dans le magasin.")
            return

        print("\nListe des ordinateurs disponibles :")
        for i, ordinateur in enumerate(self.ordinateurs, start=1):
            print(f"{i}. {ordinateur.marque} {ordinateur.modele} (Stock : {ordinateur.stock})")

        choix = int(input("\nEntrez le numéro de l'ordinateur à consulter : "))

        if choix < 1 or choix > len(self.ordinateurs):
            print("\nNuméro d'ordinateur invalide.")
            return

        ordinateur = self.ordinateurs[choix - 1]
        print("\nDétails de l'ordinateur :")
        print(f"Marque : {ordinateur.marque}")
        print(f"Modèle : {ordinateur.modele}")
        print(f"Stock : {ordinateur.stock}")

        print("\nDétails consultés avec succès !")

    def mettre_a_jour_stock(self):
        if not self.ordinateurs:
            print("\nAucun ordinateur n'est disponible dans le magasin.")
            return

        print("\nListe des ordinateurs disponibles :")
        for i, ordinateur in enumerate(self.ordinateurs, start=1):
            print(f"{i}. {ordinateur.marque} {ordinateur.modele} (Stock : {ordinateur.stock})")

        choix = int(input("\nEntrez le numéro de l'ordinateur à mettre à jour : "))

        if choix < 1 or choix > len(self.ordinateurs):
            print("\nNuméro d'ordinateur invalide.")
            return

        nouveau_stock = int(input("Nouveau stock : "))

        ordinateur = self.ordinateurs[choix - 1]
        ordinateur.stock = nouveau_stock

        print("\nStock mis à jour avec succès !")
