import random
words = ["apple", "train", "house", "music", "river"]
secret_word = random.choice(words)
guessed_letters = []
tries = 6
print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
while tries > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ " 
    print("\nWord:", display_word)
    print("Incorrect guesses left:", tries)
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        guessed_letters.append(guess)
        tries -= 1
    won = True
    for letter in secret_word:
        if letter not in guessed_letters:
            won = False
            break
    if won:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break
if tries == 0:
    print("\nGame Over! The word was:", secret_word)
