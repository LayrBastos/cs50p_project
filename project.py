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
    

def play_again():
    while True:
        restart = input("Play Again?:\n(Y) - YES\n(N) - NO\n>>>").lower()
        if restart in ('y', 'n'):
            return restart == 'y'


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
    play_game = True
    while play_game:
        pokemon_id = random.randint(1, 150)
        pk = pb.pokemon('pikachu') # substitute 'pokemon_id' for 'pikachu' when recording the presentation video
        species = pb.pokemon_species('pikachu') # substitute 'pokemon_id' for 'pikachu' when recording the presentation video
        hidden = Pokemon(pk.name,
                         species.color.name,
                         pk.height,
                         pk.weight,
                         pk.types[0].type.name)
        # Level Selection
        while True:
            level = input("Select level:\n(1) - Easy\n(2) - Hard\n>>> ")
            if level in ('1', '2'):
                level = int(level)
                break
            else:
                print("Invalid Input.")

        guesses = 0
        max_guesses = select_level(level)

        while guesses < max_guesses:
            win = False
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
                win = True
                break      
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
        if win:
            print(f"You're right!! I am {pkmn.name}!!!")
            print(f"You found me with {guesses} guesses")
        else:
            print(f"You lost... I'm {hidden.name}")

        play_game = play_again()

    sys.exit("Thanks for playing!!! :)")


if __name__ == "__main__":
    main()
