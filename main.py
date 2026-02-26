import random

def play_game():
    secret_number = random.randint(0, 50)
    attempts = 0
    max_attempts = 6

    print("\nI have slected a number between 0 and 50.")
    print(f"You have {max_attempts} attemps to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a vaild number!")
            continue

        attempts += 1

        if guess == secret_number:
            print("correct! you guessed it in", attempts, "attempts.")
            return True
        elif guess < secret_number:
            print("too low! try again.")
        else:
            print("too high! try again.")
    
    print("Game over! the number was:", secret_number)
    return False


def main():
    print("wlecome to advance number guessing game")

    score =0

    while True:
        if play_game():
            score += 1

        print("current score:", score)

        choice =input("Do you want to play again? (yes/no):").lower()

        if choice != "yes":
            print("Thanks for playing! final score:", score)
            break

if __name__== "__main__":
    main()