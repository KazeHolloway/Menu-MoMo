#On import os, puis on déclare une variable 'clear' qui va receive value,
#this last will let us clear console
import os
clear = lambda: os.system('cls')

theCode= "*105#" ; momo=0
#On définit la fonction main pour gérer TOUT le programme
def main():
    bon=True
    while bon:
        momo= input("Veuillez saisir le code momo (*105#): ")
        if momo != theCode:
            print("Le code saisi est erroné")
        else:
            operations()
            bon= False

#On définit la fonction operations pour gérer la liste des options disponibles
def operations():
    clear()
    print("Voici les différentes options disponibles:\n")
    print("1) Envoi de l'argent\n2) Paiement Facture\n3) Achat de crédit et Forfaits\n4) Epargne et prets\n5) Mon Compte\n6) Payer avec MoMo\n7) Banques\n8) GIMACPAY\n\n#) Annuler\n")
    choix=input("Veuillez effectuer votre choix: ")
    clear()

    match choix:
        case "1":
            print("\nENVOI D'ARGENT")
            envoi()

        case "2":
            print("\nPAIEMENT FACTURE")
            paiement()

        case "3":
            print("\nACHAT DE CREDIT ET FORFAITS")
            achat()

        case "4":
            print("\nEPARGNE ET PRETS")
            epargne()

        case "5": 
            print("\nMON COMPTE")
            compte()

        case "6": 
            print("\nPAYER AVEC MoMo")
            payer()
        case "7": 
            print("\nBANQUES")
            bank()

        case "8": 
            print("\nSERVICES GIMACPAY")
            gimacpay()
        
        case "#":
            print("Fermeture du programme...")
            quit()

        case _:
            print("Vous avez sélectionné une mauvaise touche. Veuillez réessayer\n")
            operations()

#On définit les différentes fonctions pour gérer les diverses options
def envoi():
    bon=True
    while bon:
        print("Voici les différentes options disponibles:\n")
        print("1) Abonne Mobile Money\n2) Non abonné MoMo\n3) Favoris\n4) Annuler l'envoi\n0) Retour\n")
        choix=input("Veuillez effectuer votre choix: ")
        clear()
        #bon
        match choix:
            case "1": print("\nAbonne Mobile Money")
            case "2": print("\nNon abonné MoMo")
            case "3": print("\nFavoris")
            case "4": print("\nAnnuler l'envoi")
            case "0": 
                print("\nRetour au menu précédent...\n")
                operations()
            case _:
                print("Vous avez sélectionné une mauvaise touche. Veuillez réessayer\n")
                envoi()

        bon= False

def paiement():
    bon=True
    while bon:
        print("Voici les différentes options disponibles:\n")
        print("1) Electricité\n2) Frais scolaires\n3) Paiement\n4) Service TV\n5) Service Internet\n6) Service Publics\n7) Assurances\n8) Mémoriser carte\n9) Supprimer carte\n10) Facture Postpayée MTN\n0) Retour\n")
        choix=int(input("Veuillez effectuer votre choix: "))
        clear()
        
        match choix:
            case "1": print("\nElectricité")
            case "2": print("\nFrais scolaires")
            case "3": print("\nPaiement")
            case "4": print("\nService TV")
            case "5": print("\nService Internet")
            case "6": print("\nService Publics")
            case "7": print("\nAssurances")
            case "8": print("\nMémoriser carte")
            case "9": print("\nSupprimer carte")
            case "10": print("\nFacture Postpayée MTN")
            case "0": 
                print("\nRetour au menu précédent...\n")
                operations()
            case _:
                print("Vous avez sélectionné une mauvaise touche. Veuillez réessayer\n")
                envoi()
 
        bon= False

def achat():
    bon = True
    while bon:
        print("Voici les différentes options disponibles:\n")
        print("1) Achat Credit pour mon numero\n2) Achat Credit pour autrui\n3) Achat Forfait pour mon numero\n4) Achat Forfait pour autrui\n0) Retour\n")
        choix=int(input("Veuillez effectuer votre choix: "))
        clear()
        if choix== 0:
            print("Retour au menu précédent...\n")
            operations()
        bon= False

def epargne():
    bon = True
    while bon:
        print("Voici les différentes options disponibles:\n")
        print("1) Avance avec MoMo\n0) Retour\n")
        choix=int(input("Veuillez effectuer votre choix: "))
        clear()
        if choix== 0:
            print("Retour au menu précédent...\n")
            operations()
        bon= False

def compte():
    bon=True
    while bon:
        print("Voici les différentes options disponibles:\n")
        print("1) Mes validations\n2) Solde\n3) Mini Releve\n4) Favoris\n5) Changer de compte PIN\n6) Reinitialiser code PIN\n7) Changer de langue\n8) Termes et Conditions MoMo\n9) Voir Mon IBAN\n10) Service Client\n0) Retour\n")
        choix=int(input("Veuillez effectuer votre choix: "))
        clear()
        if choix== 0:
            print("Retour au menu précédent...\n")
            operations()
        bon= False

#Revoir la fonction 6: Payer
def payer():
    input("Entrer Code Marchant\n")
    print("Annuler\t\tEnvoyer")

def bank():
    bon=True
    while bon:
        print("Voici les différentes options disponibles:\n")
        print("1) Retrait espèces distributeur auto\n2) Retrait de mon compte bancaire\n3) Transfert vers compte bancaire\n4) Transfert vers la banque\n5) Solde compte bancaire\n6) Mini Relevé bancaire\n0) Retour\n")
        choix=int(input("Veuillez effectuer votre choix: "))
        clear()
        if choix== 0:
            print("Retour au menu précédent...\n")
            operations()
        bon= False

def gimacpay():
    bon=True
    while bon:
        print("Voici les différentes options disponibles:\n")
        print("1) Transfert\n2) Paiement\n3) Mise a disposition GAB\n0) Retour\n")
        choix=int(input("Veuillez effectuer votre choix: "))
        clear()
        if choix== 0:
            print("Retour au menu précédent...\n")
            operations()
        bon= False


#On appelle la fonction main pour lancer le programme
if __name__ == "__main__":
    main()