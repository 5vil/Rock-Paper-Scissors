import random

while True:
    user_action = input("Enter an option(Rock, Paper, Scissors:)")
    actions = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(actions)

    print(f"\nYou chose {user_action} the computer chose {computer_choice}")

    if user_action == computer_choice:
        print(f"Both players chose {user_action}, Its a Tie!")
    elif user_action == "Rock":
        if computer_choice == "Scissors":
            print("Rock smashes Scissors, You win!")
        else:
            print("Paper covers rock, You lose :(")
    elif user_action == "Paper":
        if computer_choice == "Scissors":
            print("Scissors cut paper, you lose :(")
        else:
            print("Paper cover rock, You win !")
    elif user_action == "Scissors":
        if computer_choice == "Paper":
            print("Scissors cut Paper, You win!")
        else:
            print("Rock smashes Scissors, You lose :(")

    if user_action != actions:
        print("Please enter a valid option")

    play_again = input("Would you like to play again (y/n)")
    if play_again != "y":
        break

