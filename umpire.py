import random


class Umpire:
    def __init__(self):
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def get_overs(self):
        return self.overs

    def predict_outcome(self, batsman, bowler, fielders):
        # Simulate the outcome of a ball based on batsman and bowler stats
        # batting_prob = batsman.batting_skill
        # bowling_prob = bowler.bowling_skill
        #
        # Adjust probabilities based on player experience or other factors
        # batting_prob *= batsman.experience
        # bowling_prob *= bowler.experience

        batting_skill = batsman.batting_skill
        batting_experience = batsman.experience
        bowling_skill = bowler.bowling_skill
        bowling_experience = bowler.experience
        fielding_skill = 0
        for i in range(len(fielders)):         # fielder in fielders:
            fielding_skill += fielders[i].fielding_skill

        total_skill = batting_skill + batting_experience + bowling_skill + bowling_experience + fielding_skill

        batting_probability = batting_skill / total_skill
        bowling_probability = bowling_skill / total_skill
        fielding_probability = fielding_skill / total_skill
        probabilities = [batting_probability, bowling_probability, fielding_probability]

        chances = [ 0.1, 0.2, 0.2, 0.1, 0.2, 0.11, 0.1]
        outcomes = [0, 1, 2, 3, 4, 6, "wicket"]
        scores = [0, 1, 2, 3, 4, 6]

        outcome = random.choices(outcomes, weights=chances, k=1)[0]
        runs = random.choices(scores, k=1)[0]

        if outcome == "wicket":
            return "wicket"
        elif outcome == 0:
            return "dot ball"
        elif outcome == 1:
            return "Scored one run"
        elif outcome == 2:
            return "Scored two runs"
        elif outcome == 3:
            return "Scored three runs"
        elif outcome == 4:
            return "It's a beautiful boundary"
        elif outcome == 6:
            return "It's a spectacular six"

        # Simulate the outcome based on probabilities
        # rand_num = random.uniform(0, 1)
        # if rand_num < batting_prob:
        #     return "boundary"  # Example outcome for hitting a boundary
        # elif rand_num < batting_prob + bowling_prob:
        #     return "wicket"  # Example outcome for taking a wicket
        # else:
        #     return "dot ball"  # Example outcome for a dot ball

    def update_score(self, runs):
        self.scores += runs

    def update_wickets(self):
        self.wickets += 1

    def update_overs(self):
        self.overs += 1
