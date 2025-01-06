while at_goal() == False:
    if wall_in_front() == False:
        while front_is_clear() == True:
            move()
    else wall_in_front() == True:
        while front_is_clear() == False:
            jump()