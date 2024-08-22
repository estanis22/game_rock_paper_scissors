
# Prompt Players to choose their name and store it.
name1 = input("Player 1, please choose your name: ")
name2 = input("Player 2, please choose your name: ")


# Initialize the counter for players score.
countplayer1 = 0
countplayer2 = 0

# While loop that continues until one player wins 2 rounds.
while countplayer1 < 2 and countplayer2 < 2:

    # Ask Players to choose Rock, Paper, or Scissors, remove extra spaces, and convert to lowercase.
    player1 = input(name1 + ", please choose Rock, Paper, or Scissors: ").strip().lower()
    player2 = input(name2 + ", please choose Rock, Paper, or Scissors: ").strip().lower()

    # Check if both players made valid choices.
    if (player1 not in ["rock", "paper", "scissors"]) or (player2 not in ["rock", "paper", "scissors"]):
        print("Invalid choice by one or both players. The options are Rock, Paper, or Scissors.")
        continue  # Skip the rest of the loop and ask for input again.

    # Conditions, player1 winner choice.
    condition3 = (player1 == "scissors" and player2 == "paper")
    condition4 = (player1 == "paper" and player2 == "rock")
    condition5 = (player1 == "rock" and player2 == "scissors")
    if player1 == player2: # If both players chose the same option.
       print("It's a tie!")    
    elif condition3 or condition4 or condition5: # If Player 1's choice beats P layer 2's choice.
        print(f"Congratulations! You won, {name1}")
        countplayer1 += 1
    else: # If Player 1's choice does not bea   ts Player 2's choice.
        print(f"Congratulations! You won, {name2}")
        countplayer2 += 1
    # Display the current score
    print(f"Score: {name1} {countplayer1} - {name2} {countplayer2}")
# Announce the overall winner.
if countplayer1 == 2:
    print(f"{name1.upper()} IS THE CHAMPION!")
else:
    print(f"{name2.upper()} IS THE CHAMPION!")