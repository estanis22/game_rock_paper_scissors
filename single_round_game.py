# Prompt Players to choose their name and store it.
name1 = input("Player 1, please choose your name: ")
name2 = input("Player 2, please choose your name: ")

# Ask Players to choose Rock, Paper, or Scissors, remove extra spaces, and convert to lowercase.
player1 = input(name1 + ", please choose Rock, Paper, or Scissors: ").strip().lower()
player2 = input(name2 + ", please choose Rock, Paper, or Scissors: ").strip().lower()

# Check if Players choice is valid
condition1 = (player1 == "scissors" or player1 == "rock" or player1 == "paper")
condition2 = (player2 == "scissors" or player2 == "rock" or player2 == "paper")

# Conditions, player1 winner choice.
condition3 = (player1 == "scissors" and player2 == "paper")
condition4 = (player1 == "paper" and player2 == "rock")
condition5 = (player1 == "rock" and player2 == "scissors")


if condition1 and condition2: # If both players made valid choices.
    if player1 == player2: # If both players chose the same option.
        print("It's a tie!")
    elif condition3 or condition4 or condition5: # If Player 1's choice beats Player 2's choice.
        print("Congratulations! You won,", name1)
    else: # If Player 1's choice does not beats Player 2's choice.
        print("Congratulations! You won,", name2)
elif not condition1 and not condition2: # If neither player made a valid choice
    print("Neither player chose a valid option. Do you both not know the rules? The options are Rock, Paper, or Scissors.")
elif not condition1: # If only Player 1 made an invalid choice.
    print("Invalid choice " + name1 + ". Please select Rock, Paper, or Scissors.")
else: # If only Player 2 made an invalid choice.
    print("Invalid choice " + name2 + ". Please select Rock, Paper, or Scissors.")





