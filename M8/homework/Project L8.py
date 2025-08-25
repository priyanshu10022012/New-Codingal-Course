import random

# Program to guess a number
print("🎲 Welcome to Number Guessing Game! 🎲")

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
guess = None

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    
    if guess < secret_number:
        print("🔼 Too low! Try again.")
    elif guess > secret_number:
        print("🔽 Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
