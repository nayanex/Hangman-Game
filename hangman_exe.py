import random

words = ["3dhubs", "marvin", "print", "filament", "order", "layer"]

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


def get_random_word(wordList):
    """
    Returns a random string.

    Keyword arguments:
        wordList -- given list of words

    Returns:
        string: random word
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


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
    print('Missed characters:', end=' ')
    for character in missed_characters:
        print(character, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_characters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for characters in blanks:
        print(characters, end=' ')
    print()


def get_guess(already_guessed):
    """
    Assures that player entered a valid character.

    Keyword arguments:
        already_guessed -- previously typed characters
    """
    while True:
        print('Guess a Character.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single characters.')
        elif guess in already_guessed:
            print('You have already guessed that characters. Choose again.')
        elif guess not in '0123456789abcdefghijklmnopqrstuvwxyz':
            print('Please enter an alphanumeric character.')
        else:
            return guess


def play_again():
    """
    Ask if user wants to play again.

    Returns:
        True: if the player wants another round.
        False: Otherwise.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missed_characters = ''
correct_characters = ''
secret_word = get_random_word(words)
game_is_finished = False

while True:
    display_board(missed_characters, correct_characters, secret_word)

    guess = get_guess(missed_characters + correct_characters)
    if guess in secret_word:
        correct_characters = correct_characters + guess
        found_all_characters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_characters:
                found_all_characters = False
                break
        if found_all_characters:
            print('Yes! The secret word is "' + secret_word +
                  '"! You have won!')
            game_is_finished = True
    else:
        missed_characters = missed_characters + guess

        if len(missed_characters) == len(HANGMAN_PICS) - 1:
            display_board(missed_characters, correct_characters, secret_word)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missed_characters)) + ' missed guesses and ' +
                  str(len(correct_characters)) + ' correct guesses,' +
                  'the word was "' + secret_word + '"')
            game_is_finished = True

    if game_is_finished:
        if play_again():
            missed_characters = ''
            correct_characters = ''
            game_is_finished = False
            secret_word = get_random_word(words)
        else:
            break
