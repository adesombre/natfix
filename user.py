import datetime, csv
import utils
from utils import existing_country



existing_users = []
user={}
with open('user.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        existing_users.append(
            {
                'name': row[0],
                'email':row[1],
                'age': row[2],
                'pay': row[3],
                'subscription': row[4],
                'password': row[5],
            })
print(existing_users )
existing_email_adresses = set()
for user in existing_users:
    existing_email_adresses.add(user['email'])

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
        if email in existing_email_adresses:
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
    user = {
        "name": name,
        "email": email,
        "age": age,
        "country": country,
        "subscription": int(subscription),
        "password": password,
    }
    with open("user.csv", "a") as f:
        writer=csv.writer(f)
        writer.writerow([name,email,age,country,subscription,password])
    return user


#     fichier.write(utils.use

def authenticate():
    print("processus d'authentification")
    email = None
    while email is None:
        email = input("Entrer votre mail :").lower()

        if email.strip() == "" or utils.is_a_valid_email(email) == False:
            print("l'email ne peut pas etre vide et  invalide")
            email = None
            continue
        if email not in existing_email_adresses:
            print("cette adresse mail n\'existe pas!!")
            email = None

    password = None
    while password is None:
        password = input("Entrer votre mot de passe (min 8 caracteres ) :")
        if len(password) < 8 or password.strip() == "":
            print("veuiller avoir plus de 8 caracteres por votre mot de passe")
            password = None
