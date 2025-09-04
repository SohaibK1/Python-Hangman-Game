import random

def hangman():
    # Predefined list of words
    words = ["python", "programming", "hangman", "codealpha", "internship"]
    word = random.choice(words)  # Pick a random word
    guessed_letters = []
    attempts = 6
    guessed_word = ["_"] * len(word)

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word: ", " ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! '{guess}' is not in the word. Attempts left: {attempts}")

        print("Word: ", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
