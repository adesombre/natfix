import datetime,sys
import utils
from utils import existing_country


def register():
    print("Processus d'inscription")
    name = None
    while name is None:
        name = input("Entrer votre nom :")
        if name.strip() == "":
            print("l'email ne peut pas etre vide")
            name = None
    email = None
    while email is None:
        email = input("Entrer votre mail :").lower()

        if email.strip() == "" or utils.is_a_valid_email(email) == False:
            print("l'email ne peut pas etre vide et  invalide")
            email = None
        if email in utils.existing_email_adresses:
            print("cette adresse mail existe deja!!")
            email = None
    birth_year = None
    while birth_year is None:
        birth_year = input("Entrer votre annee de naissance :")
        if not birth_year.isdigit():
            print("entrer une annee correct")
            birth_year = None
    age = datetime.datetime.now().year - int(birth_year)

    country = None
    while country is None:
        country = input("Entrer votre pay :")
        if country.strip() == "" or country not in existing_country:
            print("le pay ne peut pas etre vide le pay n'existe pas")
            country = None
    subscription = None
    while subscription is None:
        subscription = input(
            "Entrer votre type d'abonnement 1 (regional) 2(internationale) :"
        )
        if subscription not in ("1", "2"):
            print("entre 1 ou 2 rien d'autre")
            subscription = None
    password = None
    while password is None:
        password = input("Entrer votre mot de passe (min 8 caracteres ) :")
        if len(password) < 8 or password.strip() == "":
            print("veuiller avoir plus de 8 caracteres por votre mot de passe")
            password = None
    print(f"{name=}, {email=},{age=} ans ,{country=} , {subscription=} ,{password=}")
    utils.user = {
        "name": name,
        "email": email,
        "age": age,
        "country": country,
        "subscription": int(subscription),
        "password": password,
    }
    return utils.user

# with open("user.txt", "w") as fichier:
#     fichier.write(utils.user)


def authenticate():
    print("processus d'authentification")
