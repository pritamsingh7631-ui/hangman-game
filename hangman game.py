import random

# Predefined list of 5 words
WORDS = ["apple", "tiger", "chair", "music", "plane"]

def masked_word(secret, guesses):
    """Return the word with underscores for unguessed letters."""
    return " ".join([ch if ch in guesses else "_" for ch in secret])

def main():
    secret = random.choice(WORDS)   # Randomly pick a word
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("=== Hangman Game ===")
    print(f"The secret word has {len(secret)} letters.")
    print(f"You have {max_wrong} incorrect guesses allowed.\n")

    while wrong_guesses < max_wrong and "_" in masked_word(secret, guessed_letters):
        print("Word:", masked_word(secret, guessed_letters))
        print(f"Incorrect guesses left: {max_wrong - wrong_guesses}")
        print(f"Guessed so far: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.\n")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("⚠ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret:
            print("✅ Good guess!\n")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!\n")

    # Game result
    if "_" not in masked_word(secret, guessed_letters):
        print("🎉 Congratulations! You guessed the word:", secret)
    else:
        print(f"💀 Game Over! The word was '{secret}'.")

if __name__ == "__main__":
    main()
