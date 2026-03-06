import random

print("Welcome to Rock-Paper-Scissors Game")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    print("\nChoose one:")
    print("rock")
    print("paper")
    print("scissors")

    user_choice = input("Enter your choice:").lower()

    if user_choice not in choices:
        print("Invalid choice! please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Its a Tie!")
    elif (user_choice == "rock" and computer_choice =="scissors") or \
         (user_choice == "scissors" and computer_choice =="paper")or \
         (user_choice == "paper" and computer_choice =="rock"):
        print("You win!")
        user_score += 1
    else:
        print("computer wins!")
        computer_score += 1

    print("\n Scores:")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)


    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThank you for playing!")
        break
