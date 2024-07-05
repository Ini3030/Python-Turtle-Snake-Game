from food import Food
from snake import Snake
from scoreboard import ScoreBoard, EASY, NORMAL, HARD, EXTREME
from turtle import Screen
import time


DIFFICULTIES = {
    "easy": float(EASY),
    "normal": float(NORMAL),
    "hard": float(HARD),
    "extreme": float(EXTREME),
}


# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Disables animations until screen.update() is called
screen.tracer(0)

#  Difficulty selection
difficulty = ""
while difficulty not in DIFFICULTIES:
    difficulty = screen.textinput(title="Choose a difficulty", prompt="Easy/Normal/Hard/Extreme").lower()
DIFFICULTY_VALUE = str(DIFFICULTIES[difficulty])

# Object creation
snake = Snake()
food = Food()
scoreboard = ScoreBoard(DIFFICULTY_VALUE)

# Keypress inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def cooldown():
    screen.update()
    time.sleep(1.5)


# Game Start
game_on = True
cooldown()
while game_on:
    snake.move()
    screen.update()
    # Controls in-game difficulty
    time.sleep(DIFFICULTIES[difficulty])

    # Detect collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        scoreboard.increase_score()
        snake.add_segment()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        scoreboard.reset_score(DIFFICULTY_VALUE)
        cooldown()
        snake.reset()
        cooldown()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score(DIFFICULTY_VALUE)
            cooldown()
            snake.reset()
            cooldown()


screen.exitonclick()

# TODO fix top and left screen edge — too much space
# TODO fix food being off-center
# TODO fix bug when turning twice quickly in the same direction tail collision is detected
# TODO fix cancel button in difficulty selection
# TODO change prompt arg in line 27 from being hard-coded to using the difficulty dictionary
