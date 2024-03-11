import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Create blanks
wrong_letters = []
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    # if repeated correct guesses
    if guess in display or guess in wrong_letters:
        print(f"You've already guessed {guess}!, try guessing another letter")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word and guess not in wrong_letters:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        wrong_letters.append(guess)
        lives -= 1

# if all lives lost
    if lives >0:
    #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")
        print(f"wrong letters {wrong_letters}")
        print(stages[lives])
    else:
        end_of_game = True
        print(f"The word was {chosen_word}!")
        print("You lose. GAME OVER.")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")