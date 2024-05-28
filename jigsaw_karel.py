def main():
    while(no_beepers_present()):
        move()
    pick_beeper()
    move()
    turn_left()
    for _ in range(2):
        move()
    put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    for _ in range(3):
        turn_left()
    while front_is_clear():
        move()
    turn_left()    
    turn_left()