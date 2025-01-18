from secrets import choice
import sys
import user


def display_main_title():
    TITLE_WIDTH = 80

    print(
        "#" * TITLE_WIDTH,
        f'###{"Bienvenue sur Natflix":^{TITLE_WIDTH - 6}}###',
        "#" * TITLE_WIDTH,
        sep="\n",
    )


def display_home_menu_and_retrieve_user_choice():
    choice_is_valid = False
    while not choice_is_valid:
        print(
            "Menu d'acceuil",
            "1 - S'inscrire",
            "2 - S'authentifier",
            "3 - Quitter l'application ",
            sep="\n",
        )
        choice = input("Veuillez entrer votre choix : ")
        # print(f'Choix : {choice=}')

        choice_is_valid = choice in ("1", "2", "3")
        if not choice_is_valid:
            print("Votre choix n'est pas dans la liste des options, Veuillez réessayer")
    return choice


def main():
    display_main_title()
    choice = display_home_menu_and_retrieve_user_choice()
    if choice == "1":
        user.register()
    elif choice == "2":
        user.authenticate()
    elif choice == "3":
        sys.exit("Bye bye !")


if __name__ == "__main__":
    main()
