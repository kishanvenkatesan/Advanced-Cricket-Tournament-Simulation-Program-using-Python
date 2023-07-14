import random


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []
        self.current_bowler = None
        self.score = 0
        self.is_batted = False

    def select_captain(self, player):
        self.captain = player

    def set_batting_order(self, order):
        self.batting_order = order

    def choose_bowler(self, players, previous_bowler):
        # self.current_bowler = random.choice(self.players)
        eligible_bowlers = [player for player in players if player.bowling_skill > 0 and player != previous_bowler]
        if not eligible_bowlers:
            return None
        else:
            # Calculate the weight for each bowler based on their skill and experience
            weights = [bowler.bowling_skill * bowler.experience for bowler in eligible_bowlers]
            total_weight = sum(weights)
            # Generate a random number within the total weight range
            random_num = random.uniform(0, total_weight)
            # Choose the bowler based on the weighted random selection
            cumulative_weight = 0
            for i, bowler in enumerate(eligible_bowlers):
                cumulative_weight += weights[i]
                if random_num <= cumulative_weight:
                    if bowler is not None:
                        self.current_bowler = bowler
                        return bowler
        bowler = random.choice(players)
        return bowler

    def add_score(self, runs):
        self.score += runs
