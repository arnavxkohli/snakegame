import turtle as t


class Snake:
    def __init__(self):
        self.head = None
        self.segments = []
        self.length = 3
        self.distance = 20
        self.start = []
        self.direction = "right"

    def initialize(self):
        for i in range(self.length):
            new_turtle = t.Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(-20 + (i - 1) * 20, 0)
            self.segments.append(new_turtle)
        self.head = self.segments[0]

    def change_length(self, length):
        self.length = length

    def increase_difficulty(self, difficulty):
        self.distance += difficulty * 20
    
    def clearscreen(self):
        for segment in self.segments:
            segment.reset()
    
    def reset(self):
        self.clearscreen()
        self.segments.clear()
        self.initialize()

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            if self.segments[i].fillcolor() == "black":
                self.segments[i].color("white")
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.fd(self.distance)

    def up(self):
        if self.direction != "down":
            self.head.seth(90)
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.head.seth(270)
            self.direction = "down"

    def left(self):
        if self.direction != "right":
            self.head.seth(180)
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.head.seth(0)
            self.direction = "right"

    def eat(self):
        new_turtle = t.Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("black")
        self.segments.append(new_turtle)
        self.head = self.segments[0]

