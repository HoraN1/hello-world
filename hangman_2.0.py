# Write your code here
import random

words_list = ['python', 'java', 'kotlin', 'javascript']


def game_initialize():
    """
    Initialize the game by generating the answer and hint
    """

    word_generated = random.choice(words_list)
    length = len(word_generated)
    hint = "-" * length

    return word_generated, hint


def update_hint(word, hint_old, letter):
    """
    After every input, update the hint.
    """
    hint_new = list(hint_old)
    for index, word_letter in enumerate(word):
        if letter == word_letter:
            hint_new[index] = letter
        else:
            continue
    hint = "".join(hint_new)
    return hint


def letter_pass(letter):
    """
    To test if the user input letter is suitable. 3 situations:lower alphabet; single input
    """
    if len(letter) == 1:
        if letter.isalpha() and letter.islower():
            checked = True
        else:
            print("It is not an ASCII lowercase letter")
            checked = False
    else:
        print("You should print a single letter")
        checked = False

    return checked


def in_game():
    """
    The main game process
    """
    answer, hint = game_initialize()
    tries = 8
    letter_guessed = []
    wrong_times = 0

    while wrong_times < tries:
        print()
        print(hint)
        letter_input = input("Input a letter: ")

        if letter_pass(letter_input):
            if letter_input not in letter_guessed:
                letter_guessed.append(letter_input)
                if letter_input not in answer:
                    print("No such letter in the word")
                    wrong_times += 1
            else:
                print("You already typed this letter")
                continue

        hint = update_hint(answer, hint, letter_input)

        if hint == answer:
            print("You guessed the word!\n" + hint + "\nYou survived!")
            break

        if wrong_times == tries:
            print("You are hanged!")


print("H A N G M A N")
game_begin = True

while game_begin:
    game_status = input('Type "play" to play the game, "exit" to quit: ')
    if game_status == "play":
        in_game()
    elif game_status == "exit":
        game_begin = False
        break
