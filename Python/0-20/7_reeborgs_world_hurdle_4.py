# solution for hurdle 4
# link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


# function defining code for turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# function to jump over a wall
def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while wall_in_front() == False:
        move()
    turn_left()


# main code for reaching the goal
while at_goal() == False:

    # calling function to jump over the wall in front
    while wall_in_front() == True:
        jump()

    # checking if the front is clear to move and also if the goal is achieved
    while front_is_clear() == True and at_goal() == False:
        move()
