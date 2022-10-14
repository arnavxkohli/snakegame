from turtle import Screen
import snake as s
import food as f
import score as sc
import time

screen = Screen()
screen.setup(height=500, width=500)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")

snake = s.Snake()
snake.initialize()

scoreboard = sc.Score()

food = f.Food()
food.generate()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(scoreboard.game_over, "Escape")

while scoreboard.game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.increase()

    snake.move()
    if snake.head.distance(food) < 15:
        food.generate()
        snake.eat()
        scoreboard.update()

    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        scoreboard.reset()
        scoreboard.clear()
        snake.reset()
        scoreboard.writehighscore()

    for i in range(1, len(snake.segments)-2):
        if snake.head.distance(snake.segments[i]) < 10:
            scoreboard.clear()
            scoreboard.reset()
            snake.reset()
            scoreboard.writehighscore()

if not scoreboard.game_on:
    scoreboard.writehighscore()

screen.exitonclick()


