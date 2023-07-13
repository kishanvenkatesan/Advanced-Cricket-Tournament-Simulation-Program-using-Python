import random


class Umpire:
    def __init__(self):
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def get_overs(self):
        return self.overs

    def predict_outcome(self, batsman, bowler):
        # Simulate the outcome of a ball based on batsman and bowler stats
        batting_prob = batsman.batting_skill
        bowling_prob = bowler.bowling_skill

        # Adjust probabilities based on player experience or other factors
        batting_prob *= batsman.experience
        bowling_prob *= bowler.experience

        # Simulate the outcome based on probabilities
        rand_num = random.uniform(0, 1)
        if rand_num < batting_prob:
            return "boundary"  # Example outcome for hitting a boundary
        elif rand_num < batting_prob + bowling_prob:
            return "wicket"  # Example outcome for taking a wicket
        else:
            return "dot ball"  # Example outcome for a dot ball

    def update_score(self, runs):
        self.scores += runs

    def update_wickets(self):
        self.wickets += 1

    def update_overs(self):
        self.overs += 1
