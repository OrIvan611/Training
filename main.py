from words import words
import random

word = random.choice(words).upper()
word_letters = set(word)
used_letters = []
lives = 10
BLANK = '_'
word_board = [BLANK for letter in word]
letters_not_guess_yet = len(word_letters)

while letters_not_guess_yet > 0 and lives > 0:
    print(word_board)
    print(f'You have {lives} lives. \n letters you used: {used_letters}')

    user_letter = input('Guess a letter: ').upper()
    if user_letter in used_letters:
        print('You already guess this letter. Please try again')
        continue

    word_board = [user_letter if user_letter == letter
                  else letter if letter in used_letters
                  else BLANK for letter in word]

    used_letters.append(user_letter)

    if user_letter in word:
        letters_not_guess_yet -= 1
    else:
        lives -= 1

if letters_not_guess_yet == 0:
    print('You win! Good job!')

else:
    print('Game over.. You lost :( ')

