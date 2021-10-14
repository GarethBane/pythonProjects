import random # Imports the random module to allow to select a random word from the word list
imported_list = open("word_list.txt") # Imports the word_list text files containing random words and assign it to a vairable
list_of_words = [] # Container to hold the word list
hidden_word = [] # Container to hold the chosen hidden word
# The for loop takes the words from imported_list and adds them to a list type container for later use.
# Using the randint() function imported from random module, a word is randomly selected from list_of_words.
# It is then converted to upper case through the .upper() method and assigned to word_to_guess
# hidden_word, is used to hold the *'s and will be updates with the correct letters as and when they are found
for word in imported_list:
    list_of_words += word.split()
word_to_guess = list_of_words[random.randint(0,len(list_of_words))].upper()
hidden_word = ["*" for i in range(len(word_to_guess))]
player_attempt = 7
count = 0 # This is used later to compare the number of characters revealed vs the number of characters to get right.
print(
    """
    +================================+
    |   Welcome to my game of....    |
    |           HANGMAN              |
    +================================+
    """)
# Whilst player attempt is above 0, default set to 7 as above, and the count is not equal to the length of the word to guess
# The game will keep playing. One of Two conditions must me met to end this loop, Player has guess all the correct character, count goes up with each correct choice,
# or player runs out of attempts, a player will lose an attempt with each incorrect choice.
while player_attempt > 0 and count != len(word_to_guess):
    print("Word to guess", " - ", "You have", player_attempt, "attempts") # Indicates how many attempts the player has left
    print(" ".join(hidden_word)) # Will convert and display the hidden_word list as a string with any characters that have been correctly guessed
    player_guess = (input("\nPlease enter your next guess: ")).upper()# Prompts the player to enter a character, the input is converted to upper case to ensure correct comparison later on
    if player_guess.isalpha(): # Checks if the player input is an alphabetic character
        if len(player_guess) != 1: # checks if the player has entered more than one character
            print("\nPlease enter only one character!")
        elif player_guess in hidden_word: # Checks and prompts the player if they have played that letter
            print("\nOops you've already tried that!")
        elif player_guess in word_to_guess:# Checks if the player guess is in the word to guess
            for chr in range(len(word_to_guess)): # Iterates through the word_to_guess comparing player_guess with each letter
                if player_guess == word_to_guess[chr]: # If a match add it to hidden_word, by removing a star and adding the correct letter,
                    hidden_word[chr] = word_to_guess[chr].upper() # To keep consistency and avoid errors all characters are converted to upper case
                    count += 1 # Each time the player gets a right answer increment the count, once it matches the word to guess the player has won
        else: # IF the player gets it wrong displayer a message a take a "life" from player_attempt
            print("\n             Wrong")
            player_attempt -= 1
    else:# Display a message if the player enters a none alphabetic character
        print("\nTry again with a valid letter!")

# if player has won display congratulation if not you lose
if count == len(word_to_guess): # The player has won if the count number matches the character length of the word to guess
    print(
        """
        +===========================+
        | Congratulations you win!! |
        +===========================+
        """)
    print("The hidden word was:", "".join(hidden_word))
else:
    print(
        """
        +============================+
        |          You lose          |
        +============================+
        """)
    print("The hidden word was:", "".join(word_to_guess))

