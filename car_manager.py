from turtle import Turtle,Screen
import random
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_DENSITY = 10

screen = Screen()

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_creator()
        self.move_speed = STARTING_MOVE_DISTANCE

    def car_creator(self):
        self.create_car()
        random_interval = random.randint(500,1500)
        screen.ontimer(self.car_creator, random_interval)

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(300, random.randint(-200, 270))
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT