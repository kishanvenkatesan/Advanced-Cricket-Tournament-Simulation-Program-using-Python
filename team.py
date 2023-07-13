import random


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []
        self.current_bowler = None
        self.score = 0

    def select_captain(self, player):
        self.captain = player

    def set_batting_order(self, order):
        self.batting_order = order

    def choose_bowler(self):
        self.current_bowler = random.choice(self.players)

    def add_score(self, runs):
        self.score += runs
