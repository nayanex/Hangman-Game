import random

WORDS = ["3dhubs", "marvin", "print", "filament", "order", "layer"]

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
+---+
O   |
|   |
    |
   ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']


def get_random_word(word_list):
    """
    Returns a random string.

    Keyword arguments:
        word_list -- given list of words

    Returns:
        string: random word
    """
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def is_valid_guess(already_guessed, guess):
    """
    Assures that player entered a valid character.

    Keyword arguments:
        already_guessed -- previously typed characters
    """
    guess = guess.lower()
    if len(guess) != 1:
        return 'Please enter a single Character.'
    elif guess in already_guessed:
        return 'You have already guessed that Characters. Choose again.'
    elif guess not in '0123456789abcdefghijklmnopqrstuvwxyz':
        return 'Please enter an alphanumeric character.'
    else:
        return True


def generate_board(secret_word, correct_characters):
    cells = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_characters:
            cells = cells[:i] + secret_word[i] + cells[i+1:]

    return cells


def is_game_finished(secret_word, correct_characters):
    for i in range(len(secret_word)):
        if secret_word[i] not in correct_characters:
            return False
    return True


def is_game_over(missed_characters):
    if len(missed_characters) == len(HANGMAN_PICS) - 1:
        return True
