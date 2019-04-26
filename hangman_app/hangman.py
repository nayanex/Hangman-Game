from hangman_app.utils import generate_board, get_random_word, HANGMAN_PICS,\
    WORDS


class HangmanGame:
    def __init__(self):
        self.missed_characters = ''
        self.correct_characters = ''
        self.secret_word = get_random_word(WORDS)
        self.game_is_finished = False
        self.alpha_numeric_list = "0123456789abcdefghijklmnopqrstuvwxyz"
        self.hangman = len(self.missed_characters)
        self.cells = generate_board(self.secret_word, self.correct_characters)


def display_board(missed_characters, correct_characters, secret_word):
    """
    Display Game board to the user.

    Keyword arguments:
        missed_characters -- wrong user choices
        correct_characters -- correct user choices
        secret_word -- word to be guessed
    """
    print(HANGMAN_PICS[len(missed_characters)])
    print()
    print('Missed Characters:', end=' ')
    for characters in missed_characters:
        print(characters, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_characters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for characters in blanks:
        print(characters, end=' ')
    print()


def play_again():
    """
    Ask if user wants to play again.

    Returns:
        True: if the player wants another round.
        False: Otherwise.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
