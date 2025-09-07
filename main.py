import random
import json
import os

def load_score():
    """
    Charge le meilleur score depuis le fichier JSON.

    Returns
    -------
    int | None
        Le meilleur score enregistré (nombre minimal de tentatives),
        ou None si aucun score n'est encore sauvegardé.
    """
    if os.path.exists("best_score.json"):
        with open("best_score.json", "r") as f:
            data = json.load(f)
            return data.get("best_score", None)
    return None

def save_score(score):
    """
    Sauvegarde le meilleur score dans un fichier JSON.

    Parameters
    ----------
    score : int
        Le score du joueur (nombre de tentatives pour trouver le bon nombre).
    """
    with open("best_score.json", "w") as f:
        json.dump({"best_score": score}, f)

while True:
    # Ask the player to choose the maximum number (range) for the game
    try:
        max_number = int(input("Choissisez la plage du juste prix"))
    except ValueError:
        print("Saisie invalide, 100 est la valeur par défaut")
        max_number = 100

    secret_number = random.randint(1, max_number)
    maximum_guesses = 10
    guess_counter = 0
    has_guessed = False

    best_score = load_score()
    if best_score:
        print(f"Votre record est : {best_score} tentatives")
    else:
        print("Votre record n'est pas enregistré")

    print(f"Un nombre secret a été choisi entre 1 et {max_number}. À vous de jouer !")

    while guess_counter < maximum_guesses:
        try:
            user_guess = int(input(f"Devine le nombre entre 1 et {max_number}: "))
            guess_counter += 1
        except ValueError:
            print("Entrez un nombre valide")
            continue

        if user_guess == secret_number:
            print(f" Vous avez trouvé en {guess_counter} tentatives. Félicitations !")
            has_guessed = True

            if best_score is None or guess_counter < best_score:
                save_score(guess_counter)
            break

        elif user_guess > secret_number:
            print("C'est moins !")

        elif user_guess < secret_number:
            print("C'est plus !")

    if not has_guessed:
        print(f" Vous avez atteint {maximum_guesses} tentatives. Le nombre était {secret_number}.")

    # Ask the players if they want to replay
    replay = input("Voulez-vous rejouer ? (Y/N): ").lower()

    if replay != "y":
        print("Merci d'avoir joué, à bientôt ")
        break
