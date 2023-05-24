from magasin import Magasin

def main():
    magasin = Magasin()

    while True:
        print("\nGestion du Magasin d'Ordinateurs")
        print("1. Ajouter un nouvel ordinateur")
        print("2. Consulter les détails d'un ordinateur")
        print("3. Mettre à jour les stocks")
        print("4. Quitter")
        choix = int(input("Entrez votre choix : "))

        if choix == 1:
            mot_de_passe = input("\nEntrez le mot de passe administrateur : ")
            if mot_de_passe == "0000":
                magasin.ajouter_ordinateur()
            else:
                print("\nMot de passe administrateur incorrect. Opération annulée.")
        elif choix == 2:
            magasin.consulter_details()
        elif choix == 3:
            mot_de_passe = input("\nEntrez le mot de passe administrateur : ")
            if mot_de_passe == "0000":
                magasin.mettre_a_jour_stock()
            else:
                print("\nMot de passe administrateur incorrect. Opération annulée.")
        elif choix == 4:
            print("\nAu revoir !")
            break
        else:
            print("\nChoix invalide. Veuillez réessayer.")

if __name__ == '__main__':
    main()
