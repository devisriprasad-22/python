import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")

        play_again = input("Roll again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Goodbye!")
            break
