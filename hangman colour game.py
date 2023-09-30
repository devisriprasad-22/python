import random

def choose_word():
    word_list = ["red", "blue", "green", "white", "yellow", "orange", "pink"]
    return random.choice(word_list)

def play_hangman(word):
    guessed_word = "_" * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    print(guessed_word)

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]
            print(guessed_word)
            if guessed_word == word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
    
    if attempts == 0:
        print("Sorry, you're out of attempts. The word was:", word)

if __name__ == "__main__":
    word_to_guess = choose_word()
    play_hangman(word_to_guess)
