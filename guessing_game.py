import random

def play_guessing_game():
    print("\n Welcome to the Number Guessing Game!")
    # Difficulty of levels
    print("\nChoose a difficulty level:")
    print("1 is Easy   (1–20, 10 attempts)")
    print("2 is Medium (1–50, 8 attempts)")
    print("3 is Hard   (1–100, 6 attempts)")

    # Choose difficulty

    while True:
        level = input("Witch level 1, 2 or 3: ")
        if level in ["1", "2", "3"]:
            level = int(level)
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

    # Choose difficulty setting

    if level == 1:
       max_num = 20
       attempts_left = 10
    elif level == 2:
       max_num = 50
       attempts_left = 8 
    elif level == 3:
       max_num = 100
       attempts_left = 6 
    
     # Generate a number

    secret_number = random.randint(1, max_num)
    attempts_used = 0
    print(f"\nThe secret number is between 1 and {max_num}.")
    print(f"You have {attempts_left} attempts. Good luck finding it! \n")

    # Game loop

    while attempts_left > 0:
        try:
            gess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
    
        attempts_used += 1
        attempts_left -= 1

        if gess < secret_number:
            print("Too low")
        elif gess > secret_number:
            print("Too high")
        else: 
            print(f"\n Correct! You guessed it in {attempts_used} attempts!")
            return
        print(f"Attempts left: {attempts_left}\n")
    
    print(f" Out of attempts! The number was {secret_number}.")
while True:
    play_guessing_game()
    play_again = input("Do you want to play again (yes/no): ").lower()
    if play_again != 'yes':
        print("Goodbye! Thanks for playing.")
        break


