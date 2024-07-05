from turtle import Turtle


# To adjust difficulty: modify number values inside strings
EASY = "0.14"
NORMAL = "0.11"
HARD = "0.08"
EXTREME = "0.05"

# List index for "data.txt"
DIFFICULTY_INDEX = {
    EASY: 0,
    NORMAL: 1,
    HARD: 2,
    EXTREME: 3,
}

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")
POSITION = (0, 275)


class ScoreBoard(Turtle):

    def __init__(self, difficulty="0.11"):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(POSITION)
        self.score = 0
        with open(file="data.txt", mode="r") as file:
            # Reads data — Creates list attribute — Each data line is a list item
            self.scores_list = file.read().splitlines()
            # Receives difficulty value from "main.py" — Selects list index from dictionary
            # If no value is received: uses "NORMAL" difficulty value
            # Transforms read data to Int — Saves as high-score attribute
            self.high_score = int(self.scores_list[DIFFICULTY_INDEX[difficulty]])
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}  HIGH-SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # Unused: Use as replacement for "reset_score()" if no difficulty structure is coded in "main.py"
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self, difficulty="0.11"):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as updated_file:
                # Updates high-score in the list — Uses input from "main.py" to select correct index
                self.scores_list[DIFFICULTY_INDEX[difficulty]] = str(self.high_score)
                for score in self.scores_list:
                    updated_file.write(f"{score}\n")
        self.score = 0
        self.update_scoreboard()
