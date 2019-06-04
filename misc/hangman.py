# Hangman Game
#
# Credit to Michael Dawson's "Python Programming for the Absolute Beginner 3rd Edition"
#
# The classic game of Hangman.  The computer picks a random word
# and the player wrong to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

# imports
from sys import exit
from random import randint

# constants
HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   |
     |   |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |
    ----------
    """)

MAX_WRONG = len(HANGMAN)-1
WORDS = ("OCTOPUS", "NEMO", "STARFISH", "ORCA")  # Change these as you please


# initialize variables
word = WORDS[randint(0,len(WORDS)-1)] # pick random word to be guessed
so_far = "-" * len(word)      # one dash for each letter in word to be guessed
wrong = 0                     # number of wrong guesses player has made
used = []                     # letters already guessed


print("Welcome to Hangman.  Good luck!")
print(HANGMAN[wrong])

# Ask for a guess while the game is not yet over

while wrong != MAX_WRONG and '-' in so_far:

    guess = input("\n\nEnter your guess: ").upper()
    
    # only accept one character guesses, no symbols and numbers
    if len(guess) == 1 and guess.isalpha() == True:
        
        if guess in used:
            print(f"You have guessed '{guess}' before.")
        else:
            used.append(guess)          
            if guess in word:

                # find all positions that match guess and
                # substitute that .. but convert 
                # string to list first to do this                
                lword = list(word)
                l_so_far = list(so_far)

                matched_indices = [i for i, j in enumerate(lword) if j == guess]
                for index in matched_indices:
                    l_so_far[index] = guess
                so_far = "".join(l_so_far)
            else:
                wrong +=1

        print(HANGMAN[wrong])
        print(f"You have {MAX_WRONG-wrong} guesses left!")
        print("\nYou've used the following letters:\n", used)
        print("\nSo far, the word is:\n", so_far)
    else:
        print("Guess ONE (1) LETTER only, and no symbols or numbers")

# Inform if the user won or lose

print("\nThe word was", word)

if "-" in so_far:
    print("You lost!")
else:
    print("You won!")

input("\n\nPress the enter key to exit.")

