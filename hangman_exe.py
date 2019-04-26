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


def getRandomWord(wordList):
    """
    Returns a random string.

    Keyword arguments:
        wordList -- given list of words

    Returns:
        string: random word
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedCharacters, correctCharacters, secretWord):
    """
    Display Game board to the user.

    Keyword arguments:
        missedCharacters -- wrong user choices
        correctCharacters -- correct user choices
        secretWord -- word to be guessed
    """
    print(HANGMAN_PICS[len(missedCharacters)])
    print()
    print('Missed Characters:', end=' ')
    for Characters in missedCharacters:
        print(Characters, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctCharacters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for Characters in blanks:
        print(Characters, end=' ')
    print()


def getGuess(alreadyGuessed):
    """
    Assures that player entered a valid character.

    Keyword arguments:
        alreadyGuessed -- previously typed characters
    """
    while True:
        print('Guess a Character.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single Characters.')
        elif guess in alreadyGuessed:
            print('You have already guessed that Characters. Choose again.')
        elif guess not in '0123456789abcdefghijklmnopqrstuvwxyz':
            print('Please enter an alphanumeric character.')
        else:
            return guess


def playAgain():
    """
    Ask if user wants to play again.

    Returns:
        True: if the player wants another round.
        False: Otherwise.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedCharacters = ''
correctCharacters = ''
secretWord = getRandomWord(words)
gameIsFinished = False

while True:
    displayBoard(missedCharacters, correctCharacters, secretWord)

    guess = getGuess(missedCharacters + correctCharacters)
    if guess in secretWord:
        correctCharacters = correctCharacters + guess
        foundAllCharacters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctCharacters:
                foundAllCharacters = False
                break
        if foundAllCharacters:
            print('Yes! The secret word is "' + secretWord +
                  '"! You have won!')
            gameIsFinished = True
    else:
        missedCharacters = missedCharacters + guess

        if len(missedCharacters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedCharacters, correctCharacters, secretWord)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missedCharacters)) + ' missed guesses and ' +
                  str(len(correctCharacters)) + ' correct guesses,' +
                  'the word was "' + secretWord + '"')
            gameIsFinished = True

    if gameIsFinished:
        if playAgain():
            missedCharacters = ''
            correctCharacters = ''
            gameIsFinished = False
            secretWord = getRandomWord(words)
        else:
            break
