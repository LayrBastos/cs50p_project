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

# project.py
`select_level(n)` returns the number of max guesses the user will have according to the difficulty option chosen (1 for easy or 2 for hard)

## Vídeo Demo: <https://youtu.be/9VCx4lmRiy0>