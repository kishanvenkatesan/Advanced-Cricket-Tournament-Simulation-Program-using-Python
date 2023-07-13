from umpire import Umpire
from commentator import Commentator
import random


class Match:
    def __init__(self, team1, team2, field):
        self.current_bowling_team = None
        self.current_batting_team = None
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire()
        self.commentator = Commentator()
        self.previous_bowler = None

    def start_match(self):
        # Starting the match
        self.toss()
        self.select_batting_order()

    def toss(self):
        # Simulate a toss to decide which team bats first
        toss_winner = random.choice([self.team1, self.team2])
        self.current_batting_team = toss_winner
        self.current_bowling_team = self.team1 if toss_winner == self.team2 else self.team2

    def select_batting_order(self):
        # Randomly set the batting order for the teams
        random.shuffle(self.team1.players)
        random.shuffle(self.team2.players)
        self.team1.set_batting_order(self.team1.players.copy())
        self.team2.set_batting_order(self.team2.players.copy())

    def play(self):
        self.start_match()
        print("The match is starting....!")
        print("\nThe ", self.current_batting_team.name, " has won the toss and will be batting first")
        while not self.is_match_over():
            batting_team = self.current_batting_team
            bowling_team = self.current_bowling_team

            self.simulate_over(batting_team, bowling_team)

            if self.is_team_innings_completed(self.current_batting_team):
                # if self.is_team_innings_completed(self.current_bowling_team):
                #     return
                # else:
                self.change_innings()

    def simulate_over(self, batting_team, bowling_team):
        if not batting_team.batting_order:
            return

        bowling_team = self.team1 if self.current_bowling_team == self.team1 else self.team2
        batting_team = self.current_batting_team
        while True:
            bowler = bowling_team.choose_bowler(bowling_team.players, self.previous_bowler)
            if bowler is None:
                # bowler = bowling_team.choose_random(bowling_team.players)
                print(len(batting_team.players))
                bowler = random.choice(bowling_team.players)

            batsman = batting_team.batting_order[0]
            if bowler != batsman:  # and not (batsman == bowler):
                break
        # bowler = bowling_team.current_bowler
        print("\nChange of over. Bowler " + bowler.name + " is bowling")
        for _ in range(6):
            if not batting_team.batting_order:
                break

            batsman = batting_team.batting_order[0]
            self.simulate_ball(batsman, bowler)

        # Update the previous bowler
        self.previous_bowler = bowler

        # Update overs count for the umpire
        self.umpire.update_overs()

    def simulate_ball(self, batsman, bowler):
        # Simulate a ball and update match stats
        outcome = self.umpire.predict_outcome(batsman, bowler)
        # runs_scored = random.choice([0, 1, 2, 3, 4, 6])
        # Update match statistics based on the outcome
        if outcome == 'wicket':
            self.umpire.update_wickets()
            batting_team = self.current_batting_team
            if self.is_team_innings_completed(batting_team):
                # if self.is_team_innings_completed(bowling_team):
                #     exit()
                # else:
                self.change_innings()
            else:
                batting_team.batting_order.pop(0)
                # Remove batsman from the field
        elif outcome == 'boundary':
            self.umpire.update_score(4)
            batting_team = self.current_batting_team
            batting_team.add_score(4)  # Add 4 to the batting team's score
        # else

        # Generate commentary based on the match stats and ongoing game events
        commentary = self.commentator.provide_commentary(batsman, bowler, outcome)
        print(commentary)

    def change_innings(self):
        # Switch batting and bowling teams for the second innings
        print("\nThe innings has been completed and ", self.current_bowling_team.name, " will be batting now")
        self.current_batting_team.is_batted = True
        self.previous_bowler = None
        self.current_batting_team, self.current_bowling_team = self.current_bowling_team, self.current_batting_team

        # self.commentator.provide_commentary(None, None, None)

    def is_match_over(self):
        # Check if the match is over (e.g., all overs completed for both teams)
        return self.is_team_innings_completed(self.team1) and self.is_team_innings_completed(self.team2)

    def is_team_innings_completed(self, team):
        # Check if the innings is completed for a specific team (e.g., all overs completed or all players out)
        # return team.is_batted == True or team.batting_order == [] or self.umpire.get_overs() >= 20
        return team.batting_order == [] or self.umpire.get_overs() >= 20

    def display_match_summary(self):
        # Display match summary based on the match statistics
        # You can customize the implementation as per your requirements
        print("\nMatch Summary:")
        print(f"Team 1 Score: {self.team1.score}")
        print(f"Team 2 Score: {self.team2.score}")
        print(f"Overs Played: {self.umpire.get_overs()}")

    def display_winner(self):
        # Determine and display the winner based on the match statistics
        # You can customize the implementation as per your requirements
        if self.team1.score > self.team2.score:
            print(f"{self.team1.name} wins!")
        elif self.team2.score > self.team1.score:
            print(f"{self.team2.name} wins!")
        else:
            print("It's a draw!")
