import random
imported_list = open("word_list.txt")
list_of_words = []
hidden_word = []
# wrong_letters = []
for word in imported_list:
    list_of_words += word.split()
word_to_guess = list_of_words[random.randint(0,len(list_of_words))].upper()
hidden_word = ["*" for i in range(len(word_to_guess))]
player_attempt = 7
count = 0
print(
    """
    +================================+
    |   Welcome to my game of....    |
    |           HANGMAN              |
    +================================+
    """)

while player_attempt > 0 and count != len(word_to_guess):
    # print("\nWrong letters",wrong_letters)
    print("Word to guess", " - ", "You have", player_attempt, "attempts")
    print(hidden_word)
    player_guess = (input("\nPlease enter your next guess: ")).upper()
    if player_guess.isalpha():
        if len(player_guess) != 1:
            print("\nPlease enter only one character!")
        elif player_guess in hidden_word:
            print("\nOops you've already tried that!")
        elif player_guess in word_to_guess:
            for chr in range(len(word_to_guess)):
                if player_guess == word_to_guess[chr]:
                    hidden_word[chr] = word_to_guess[chr].upper()
                    count += 1
        else:
            print("\n           Wrong")
            player_attempt -= 1
            # wrong_letters.append(player_guess)
    else:
        print("\nTry again with a valid letter!")

if count == len(word_to_guess):
    print(
        """
        +===========================+
        | Congratulations you win!! |
        +===========================+
        """)
else:
    print(
        """
        +============================+
        |          You lose          |
        +============================+
        """)
    print("The hidden word was:", word_to_guess)