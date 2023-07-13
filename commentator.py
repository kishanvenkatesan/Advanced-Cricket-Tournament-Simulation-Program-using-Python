class Commentator:
    def __init__(self):
        pass

    def provide_commentary(self, batsman, bowler, outcome):
        # Generate commentary based on the match stats and ongoing game events
        # Use batsman, bowler, and outcome to create descriptive commentary
        commentary = f"{batsman.name} facing {bowler.name}. {outcome}!"
        return commentary

    def change_over(self):
        commentary = "Change of over"
        return commentary