# Initialize variables
secret_number = "cat"
out_of_guess = False
guess_count = 0
guess_limit = 5  # Adjusted guess limit for simplicity

# Loop until the player runs out of guesses or guesses correctly
while guess_count < guess_limit and not out_of_guess:
    # Prompt the player to enter their guess
    guess = input("Guess the secret word: ")

    # Check if the guess matches the secret number
    if guess == secret_number:
        print("Congratulations! You guessed the secret word correctly.")
        break  # Exit the loop because the player won

    # Increment guess count
    guess_count += 1

    # Calculate remaining chances
    chances_remaining = guess_limit - guess_count
    print(f"You have {chances_remaining} chances remaining.")

# If the player runs out of guesses without guessing correctly
if guess_count == guess_limit:
    print(f"Out of guesses. The secret word was '{secret_number}'. Try again next time.")
