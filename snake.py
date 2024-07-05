from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_LENGTH = 3


class Snake:

    def __init__(self):
        self.segments = []
        self.starting_x_axis = 0
        self.starting_y_axis = 0
        self.starting_length = STARTING_LENGTH
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Snake creation
        for new_segment in range(self.starting_length):
            self.add_segment()

    def add_segment(self):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(x=self.starting_x_axis, y=self.starting_y_axis)
        self.starting_x_axis -= MOVE_DISTANCE
        self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.starting_x_axis = 0
        self.starting_y_axis = 0
        self.create_snake()
        self.head = self.segments[0]
