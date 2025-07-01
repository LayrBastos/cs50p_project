# Who's that Pokémon?! -  Guessing Game
CS50p Final Project for obtainment of Harvard's CS50p Certificate.

## Prerequisites:
- pokebase

`pip install pokebase`

## How the game works:
This is a guessing game in which the player must discover who is the misterious Pokémon based on the given hints.

When the game starts, the player must choose the difficulty level, and there will be 20 guesses on easy mode or 10 guesses on hard mode.

After making a guess, the hidden Pokémon will compare it's height and weight with the guessed Pokémon.
If the guessed Pokémon and the hidden one share the same Pokémon type, this information will be given as a hint. The same applies to the case when both Pokémons have the same main colour.

The game ends with a victory if the player discovers **WHO'S THAT POKÉMON** or with a game over if the player reaches the maximum number of guesses based on the chosen level.

### project.py
Function `select_level(n)` returns *int* - the number of max guesses the user will have according to the difficulty option chosen (1 for easy or 2 for hard)

Function `play_again()` returns *bool* - True if the player wants to play again (Y) or False if the player doesn't want to play again (N)

Function `height(h)` returns *str* - a formated string to convert the height of the Pokémon to meters (if more than 1m) or to centimeters (if less than 1m)

Function `weight(w)` returns *str* - a formated string to convert the Pokémon's weight to kilograms rounded to one decimal

`main()`:
The game will sort a Pokémon number (1 to 150) with `random.randint()` and that Pokémon number will be used to get a Pokémon and it's species attributes from **pokeapi**.

Then the Pokemon *class* will be instanciated at `hidden`.

After that, the player will choose the game difficulty to be passed as a parameter to function `select_level(n)`.

Now, acccording to the max guesses number set by the level, the player will start guessing Pokémons until he wins or loses...

Just like before, a Pokemon *class* will be instanciated at `pkmn`.

Then the functions from `pokemon.Pokemon` will compare if the guessed Pokémon (`pkmn`) is the same as the hidden one (`hidden`).

If yes, the game ends with a win... 
If not, the other functions from `pokemon.Pokemon` will compare the Pokémon height (`hidden.is_taller_than(pkmn)`) and weight (`hidden.is_heavier_than(pkmn)`).
And will also check if the hidden Pokémon's type (`hidden.type_revealed`) and color (`hidden.color_revealed`) were already revealed, so the hidden Pokémon can give a hint...

After all that, the loop restarts until the player guesses correctly or hits the max number of guesses.

### pokemon.py
`Pokemon` class gets initialized with it's given name, color, height, weight and type.
Also it's `color_revealed` and `type_revealed` attributes gets initialized as `False`, so it can be tracked if the player already knows it and the Pokémon won't give unnecessary hints.

Function `check_guess(self, other)` will compare the guessed name with the hidden Pokémon's name, so we can tell if the player won or not.

Functions `is_taller_than(self, other)` and `is_heavier_than(self, other)` will compare the Pokémons height and weight to also give hints based on that.

Functions `compare_types(self, other)` and `compare_colors(self, other)` will also check for color and types matches to give hints.

## Vídeo Demo: <https://youtu.be/9VCx4lmRiy0>