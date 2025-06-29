import pokebase as pb
from pokemon import Pokemon
import random
import sys


def select_level(n):
    """
    Parameters:
    n (int): Level to play (1 for Easy or 2 for Hard)

    Returns:
    int: Number of guesses according to the chosen level
    """
    if n == 1:
        return 20
    elif n == 2:
        return 10


def height(h):
    """Converts the Pokémon's height to meters or centimeters (if less than 1 m)

    Parameters:
    h (float): The height to be converted

    Returns:
    str: Converted height with its unit beside
    """
    if h < 10:
        return f"{h * 10}cm"
    else:
        return f"{h / 10}m"


def weight(w):
    """Converts the Pokémon's weight to kilograms

    Parameters:
    w (float): The weight to be converted

    Returns:
    str: Converted weight with its unit beside
    """
    w /= 10
    return f"{round(w, 1)}kg"


def main():
    pokemon_id = random.randint(1, 150)
    pk = pb.pokemon(pokemon_id)
    species = pb.pokemon_species(pokemon_id)

    hidden = Pokemon(pk.name,
                     species.color.name,
                     pk.height,
                     pk.weight,
                     pk.types[0].type.name)

    while True:
        level = input("Select level:\n(1) - Easy\n(2) - Hard\n>>> ")
        try:
            level = int(level)
            break
        except ValueError:
            print("Invalid Input.")

    guesses = 0
    max_guesses = select_level(level)

    while guesses < max_guesses:
        if guesses > 0:
            print(f"Guesses: {guesses}\n")
            print("+-" * 20)
        guess = input("Guess who I am: ").lower()
        try:
            guessed_pokemon = pb.pokemon(guess)
            guessed_species = pb.pokemon_species(guess)
            pkmn = Pokemon(guessed_pokemon.name,
                           guessed_species.color.name,
                           guessed_pokemon.height,
                           guessed_pokemon.weight,
                           guessed_pokemon.types[0].type.name)
        except AttributeError:
            print(f"{guess}...? I don't know that pokemon... Check the spelling and try again.")
            continue
        else:
            guesses += 1

        if hidden.check_guess(pkmn):
            print(f"You're right!! I am {pkmn.name}!!!")
            print(f"You found me with {guesses} guesses")
            sys.exit("Thanks for playing.")
        else:
            print(f"{pkmn.name} is {height(pkmn.height)} tall and weighs {weight(pkmn.weight)}. So...")
            if hidden.is_taller_than(pkmn):
                print("I am taller and", end=' ')
            else:
                print("I am shorter and", end=' ')
            if hidden.is_heavier_than(pkmn):
                print(f"heavier than {pkmn.name}")
            else:
                print(f"lighter than {pkmn.name}")
            if not hidden.type_revealed:
                hidden.compare_types(pkmn)
            if not hidden.color_revealed:
                hidden.compare_colors(pkmn)
    print(f"You've lost... I'm {hidden.name}")


if __name__ == "__main__":
    main()
