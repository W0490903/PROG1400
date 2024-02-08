import random

# Step 1: Define the base class
class Player:
    def __init__(self, name):
        self.name = name

    def choose_move(self):
        pass

# Step 2: Create a derived class (HumanPlayer) that inherits from the base class (Player)
class HumanPlayer(Player):
    def choose_move(self):
        move = input(f"{self.name}, enter your move (rock, paper, or scissors): ").lower()
        while move not in ["rock", "paper", "scissors"]:
            print("Invalid move. Please enter 'rock', 'paper', or 'scissors'.")
            move = input(f"{self.name}, enter your move (rock, paper, or scissors): ").lower()
        return move

# Step 3: Create another derived class (ComputerPlayer) that also inherits from the base class (Player)
class ComputerPlayer(Player):
    def choose_move(self):
        return random.choice(["rock", "paper", "scissors"])

# Step 4: Create a Game class to manage the gameplay
class RockPaperScissorsGame:
    def __init__(self):
        self.player1 = HumanPlayer("Player 1")
        self.player2 = ComputerPlayer("Computer")

    def determine_winner(self, move1, move2):
        if move1 == move2:
            return "It's a tie!"
        elif (move1 == "rock" and move2 == "scissors") or \
             (move1 == "scissors" and move2 == "paper") or \
             (move1 == "paper" and move2 == "rock"):
            return f"{self.player1.name} wins!"
        else:
            return f"{self.player2.name} wins!"

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")

        move1 = self.player1.choose_move()
        move2 = self.player2.choose_move()

        print(f"{self.player1.name} chose {move1}")
        print(f"{self.player2.name} chose {move2}")

        result = self.determine_winner(move1, move2)
        print(result)

# Step 5: Instantiate the Game class and play the game
if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()
