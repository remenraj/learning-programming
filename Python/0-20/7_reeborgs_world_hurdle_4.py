# solution for hurdle 4
# link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%204&url=worlds%2Ftutorial_en%2Fhome4.json

# function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# main code for reaching the goal
while at_goal() == False:

    # moving while not at goal and front is clear
    while front_is_clear() and not at_goal():
        move()

    # checking if front is clear and right is not clear
    if wall_in_front() and not right_is_clear():
        turn_left()

    # checking if front is clear and right is clear
    if wall_in_front() and right_is_clear():
        turn_right()
