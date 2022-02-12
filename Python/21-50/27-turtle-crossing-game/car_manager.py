from turtle import Turtle
import random
from screen_settings import HEIGHT, WIDTH


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.car_speed = MOVE_INCREMENT
        self.cars = []

    def generate_cars(self):
        """Generate a random car and add it to the list of cars"""

        random_choice = random.randint(1, 6)
        if random_choice == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=2, stretch_len=3)
            new_car.setposition(
                x=WIDTH / 2 + 50,
                y=random.randint(a=-HEIGHT / 2 + 80, b=HEIGHT / 2 - 80),
            )
            self.cars.append(new_car)

    def move_cars(self):
        """Move all the cars in the list"""

        for i in range(len(self.cars)):

            self.cars[i].forward(self.car_speed)

    def increase_speed(self):
        """Increase the speed of the cars"""

        self.car_speed += 2
