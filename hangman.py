# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import this
import warnings

from numpy import true_divide

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list Sof valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ''
    for i in secret_word:
      if i in letters_guessed:
        word = word + i
      
    if word == secret_word:
      return True
    else:
      return False 

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ''
    for i in range(0, len(secret_word)):
      if secret_word[i] in letters_guessed:
        guessed_word = guessed_word + secret_word[i]
      else:
        guessed_word = guessed_word + '_'
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available = ''
    unavailable = ''
    alphabet = string.ascii_lowercase
    for i in range(0, len(alphabet)):
      if alphabet[i] in letters_guessed:
        unavailable = unavailable + alphabet[i]
      else:
        available = available + alphabet[i]
    return available

def unique_letters(secret_word):
  '''
  secret_word: string, the secrete word to guess
  return: integer, the number of unique letters in the secret_word
  '''
  uniques = []
  for letter in secret_word:
    if letter not in uniques:
      uniques = uniques + [letter]
  return len(uniques)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', str(len(secret_word)), ' letters long.')
    print('-------------')
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    alphabet = string.ascii_lowercase
    vowels = ['a', 'e', 'i', 'o', 'u']
    while not guesses_remaining <= 0:
      print("You have ", guesses_remaining, "guesses left.")
      print("Available letters: ", get_available_letters(letters_guessed))
      guess = input("Please guess a letter: ")
      if guess in alphabet:
        if guess in letters_guessed:
          warnings_remaining -= 1
          if warnings_remaining < 0:
            guesses_remaining -= 1
            letters_guessed.append(guess)
            print("Oops! You have already guessed that letter. You have no warnings left. So, you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
          elif warnings_remaining == 0:
            letters_guessed.append(guess)
            print("Oops! You have already guessed that letter. You have 0 warnings left: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
          else:
            letters_guessed.append(guess)
            print("Oops! You have already guessed that letter. You have ", warnings_remaining, " warnings left: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
        else:
          if guess in secret_word: 
            letters_guessed.append(guess)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
            if is_word_guessed(secret_word, letters_guessed):
              print("Congratulations, you won! Your total score is: ", guesses_remaining*unique_letters(secret_word)) # change scoring calculation 
              break   
          else:
            if guess in vowels:
              guesses_remaining -= 2
            else:
              guesses_remaining -= 1
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
      else:
        warnings_remaining -= 1
        if warnings_remaining < 0:
          guesses_remaining -= 1
          print("Oops! That is not a valid letter. You have no warnings left. So, you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
          print('-------------')
        elif warnings_remaining == 0:
          warnings_remaining = warnings_remaining - 1
          print("Oops! That is not a valid letter. You have 0 warnings left: ", get_guessed_word(secret_word, letters_guessed))
          print('-------------')
        else:
          print("Oops! That is not a valid letter. You have ", warnings_remaining, " warnings left: ", get_guessed_word(secret_word, letters_guessed))
          print('-------------')
    if guesses_remaining <= 0:
      print("Sorry, you ran out of guesses. The word was ", secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.strip()
    if len(my_word) != len(other_word):
      return False
    
    # Copy and pasted code from the github user rawnoob25. However, I learned a new way of solving a problem. 
    
    # In my previous approach, the main problem I ran into was returning False for letters that were already in my_word. So, I thought I would create a list of boolean values that outputted True or false depending on a couple of conditions such as whether the letter in my_word matched or did not match in other_word, when the letter in my_word was '_', as well as whether the letter has already been checked previously. Then from that list of booleans, if there was a False value in that list, I would return False. 

    # Problems I didn't consider, because programs run lines sequentially, it never got to the condition where letters in both my_word and other_word was the same but the letters have already been checked beforehand. Instead, the function would output True because there was an initial condition that returned True of the letter in my_word and other_word have the same letter. So, it never got to the conditioned I just mentioned.

    # This approach, we start by assuming that my_word would be a valid input. So, we end the function by returning True if my_word is able to not successfully fall into a condition that returns a False. Here, we don't need to keep track of a list of booleans like my initial approach nor a list of characters already checked. Cleverly, if we were checking the character "_" in my_word with the corresponding character in other_word, we would check if the corresponding character already exist in my_word.

    i = 0
    while(i < len(my_word)):
        if not (my_word[i] == "_"):
            if my_word[i]!=other_word[i]:
                return False
        else: 
            if other_word[i] in my_word:
                return False
        i+=1
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
    Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = ''
    for word in wordlist:
        if len(word) == len(my_word):
            if match_with_gaps(my_word, word):
              possible_matches = possible_matches + ' ' + word
    
    if len(possible_matches) != 0:
      print(possible_matches[1:])
    else:
      print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', str(len(secret_word)), ' letters long.')
    print('-------------')
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    alphabet = string.ascii_lowercase
    vowels = ['a', 'e', 'i', 'o', 'u']
    while not guesses_remaining <= 0:
      print("You have ", guesses_remaining, "guesses left.")
      print("Available letters: ", get_available_letters(letters_guessed))
      guess = input("Please guess a letter: ")
      if guess in alphabet:
        if guess in letters_guessed:
          warnings_remaining -= 1
          if warnings_remaining < 0:
            guesses_remaining -= 1
            letters_guessed.append(guess)
            print("Oops! You have already guessed that letter. You have no warnings left. So, you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
          elif warnings_remaining == 0:
            letters_guessed.append(guess)
            print("Oops! You have already guessed that letter. You have 0 warnings left: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
          else:
            letters_guessed.append(guess)
            print("Oops! You have already guessed that letter. You have ", warnings_remaining, " warnings left: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
        else:
          if guess in secret_word: 
            letters_guessed.append(guess)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
            if is_word_guessed(secret_word, letters_guessed):
              print("Congratulations, you won! Your total score is: ", guesses_remaining*unique_letters(secret_word)) # change scoring calculation 
              break   
          else:
            if guess in vowels:
              guesses_remaining -= 2
            else:
              guesses_remaining -= 1
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
      else:
        warnings_remaining -= 1
        if warnings_remaining < 0:
          guesses_remaining -= 1
          print("Oops! That is not a valid letter. You have no warnings left. So, you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
          print('-------------')
        elif guess == "*":
          show_possible_matches(get_guessed_word(secret_word, letters_guessed))
          print('-------------')
        elif warnings_remaining == 0:
          warnings_remaining = warnings_remaining - 1
          print("Oops! That is not a valid letter. You have 0 warnings left: ", get_guessed_word(secret_word, letters_guessed))
          print('-------------')
        else:
          print("Oops! That is not a valid letter. You have ", warnings_remaining, " warnings left: ", get_guessed_word(secret_word, letters_guessed))
          print('-------------')
    if guesses_remaining <= 0:
      print("Sorry, you ran out of guesses. The word was ", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
