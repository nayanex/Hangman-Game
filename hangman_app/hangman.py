import random

WORDS = ["3dhubs", "marvin", "print", "filament", "order", "layer"]
MAX_ERRORS = 5


class HangmanGame:
    def __init__(self):
        self.missed_characters = ''
        self.correct_characters = ''
        self.secret_word = get_random_word(WORDS)
        self.is_game_over = False
        self.is_game_won = False
        self.alpha_numeric_list = "0123456789abcdefghijklmnopqrstuvwxyz"
        self.hangman = len(self.missed_characters)
        self.cells = generate_board(self.secret_word, self.correct_characters)
        self.is_game_done = self.is_game_won or self.is_game_over
        self.invalid_guess_msg = ""


def get_random_word(word_list):
    """
    Generate a random string.

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

    Returns:
        True: if valid character is guessed
        String: Error message otherwise
    """
    guess = guess.lower()
    if len(guess) != 1:
        return (False, "Please enter a single Character.")
    elif guess in already_guessed:
        return (False, "You've already guessed that character. Choose again.")
    elif guess not in '0123456789abcdefghijklmnopqrstuvwxyz':
        return (False, "Please enter an alphanumeric character.")
    else:
        return (True, "")


def generate_board(secret_word, correct_characters):
    """
    Generate game board.

    Keyword arguments:
        secret_word -- word to be guessed
        correct_characters -- correct characters guessed so far

    Returns:
        string: set of correct guesses and blank spaces
    """
    cells = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_characters:
            cells = cells[:i] + secret_word[i] + cells[i+1:]

    return cells


def is_game_won(secret_word, correct_characters):
    """
    Check if game is finished.

    Keyword arguments:
        secret_word -- word to be guessed
        correct_characters -- correct characters guessed so far

    Returns:
        boolean: True if game is finished, False otherwise
    """
    for i in range(len(secret_word)):
        if secret_word[i] not in correct_characters:
            return False
    return True


def is_game_over(missed_characters):
    """
    Check if game is over/lost.

    Keyword arguments:
        missed_characters -- wrong guesses

    Returns:
        boolean: True if game is over, False otherwise
    """
    if len(missed_characters) == MAX_ERRORS:
        return True
    return False
