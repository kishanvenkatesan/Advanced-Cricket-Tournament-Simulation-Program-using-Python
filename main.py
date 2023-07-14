import threading
from player import Player
from team import Team
from field import Field
from match import Match
from commentator import Commentator
from umpire import Umpire

# Create player objects
player1 = Player("M S Dhoni", 0.8, 0.2, 0.99, 0.8, 0.9)
player2 = Player("Virat", 0.7, 0.3, 0.95, 0.7, 0.8)
player3 = Player("Saurav Ganguly", 0.6, 0.7, 0.9, 0.6, 0.7)
player4 = Player("Sachin Tendulkar", 0.9, 0.6, 0.96, 0.6, 0.9)
player5 = Player("Anil Kumble", 0.8, 0.8, 0.94, 0.7, 0.6)
player6 = Player("Yuvraj Singh", 0.8, 0.2, 0.92, 0.8, 0.8)

# Create team objects
team1 = Team("Team 1", [player1, player2, player5])
team2 = Team("Team 2", [player3, player4, player6])

# Create field object
field = Field("Large", 0.8, "Good", 0.1)

umpire = Umpire()
commentator = Commentator()

# Create match object
match = Match(team1, team2, field)


# Start the match
def run_match():
    match.start_match()
    while not match.is_match_over():
        # Simulate the match
        match.play()


# Create and start the thread for running the match
match_thread = threading.Thread(target=run_match)
match_thread.start()

# Wait for the match thread to finish
match_thread.join()

# Display match summary and winner
match.display_match_summary()
match.display_winner()
