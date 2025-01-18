import re

existing_email_adresses = {"alain@sfr.fr", "franck@free.fr"}
existing_country = [
    "Italie",
    "Angleterre",
    "Espagne",
    "Albanie",
    "Allemagne",
    "Andorre",
    "Arménie",
    "Autriche",
    "Bosnie-Herzégovine",
    "Bulgarie",
    "Chypre",
    "Croatie",
    "Danemark",
    "Finlande",
    "France",
    "Géorgie",
    "Grèce",
    "Hongrie",
    "Italie",
    "Lettonie",
    "Liechtenstein",
    "Lituanie",
    "Luxembourg",
    "Moldavie",
    "Monténégro",
    "Norvège",
    "Pays-Bas",
    "Roumanie",
    "Royaume-Uni",
    "Saint-Marin",
    "Serbie",
    "Slovénie",
    "Suisse",
    "Tchéquie",
    "Turquie",
]
user = {}


def is_a_valid_email(email):
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email) is None:
        return False
    else:
        return True


if __name__ == "__main__":
    print(is_a_valid_email("alain"))
