def main():
    fill_row()
    while front_is_clear():
        move()
        turn_right()
        fill_row()
    turn_right()
    while front_is_clear():
        move()

def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
  