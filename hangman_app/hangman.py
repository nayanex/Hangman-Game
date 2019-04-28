from hangman_app.utils import generate_board, get_random_word, WORDS


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
