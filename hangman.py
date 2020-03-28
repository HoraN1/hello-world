# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list


def choose_word(word_list):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    """
    # FILL IN YOUR CODE HERE...
    num_correct = 0
    for index in range(len(secret_word)):
        if secret_word[index] in letters_guessed:
            num_correct += 1
    if num_correct == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    # FILL IN YOUR CODE HERE...
    word_guessing = ''
    for index in range(len(secret_word)):
        if secret_word[index] in letters_guessed:
            word_guessing += secret_word[index]
        else:
            word_guessing += '_'
    return word_guessing


def get_available_letters(letters_guessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE...
    letter_remaining = list(string.ascii_lowercase)
    for letter in letters_guessed:
        if letter in letter_remaining:
            letter_remaining.remove(letter)
    return ''.join(letter_remaining)


def hangman(secret_word):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE... 
    letters_guessed = ''
    get_available_letters(letters_guessed)
    num_guess = 0
    guess_round = len(secret_word) + 4
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    while 1 <= guess_round <= (len(secret_word) + 4):
        # show how many rounds remaining
        print("-------------")
        print("You have", guess_round, "guesses left.")
        # show the letters remaining
        get_available_letters(letters_guessed)
        print("Available letters:", get_available_letters(letters_guessed))
        # request the user to input a guess
        print("Please guess a letter:", end='')
        guess = input()
        if guess in string.ascii_lowercase and len(guess) == 1:
            # if user re-enter guessed letter, ask to enter again, and no rounds deduction
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
            # continue guessing
            else:
                letters_guessed += guess.lower()
                # guess right
                if guess in secret_word:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                    num_guess += 1
                # guess wrongly
                else:
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                guess_round -= 1
            # all the letters are right
            if is_word_guessed(secret_word, letters_guessed):
                print("-------------")
                print("Congratulations, you won!")
                break        
            # run out of rounds
            if guess_round == 0:
                print("-------------")
                print("Sorry, you ran out of guesses. The word was", secret_word, ".")
                break
        else:
            print("PLease enter an alphabet letter!")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


generated_word = choose_word(wordlist).lower()
hangman(generated_word)
