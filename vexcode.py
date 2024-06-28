size = 0
direction = 0

def Y():
    global myVariable, size, direction
    pen.move(DOWN)
    drivetrain.drive_for(FORWARD, size, MM)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, size, MM)
    drivetrain.drive_for(REVERSE, size, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, size, MM)
    drivetrain.drive_for(REVERSE, size, MM)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    drivetrain.drive_for(REVERSE, size, MM)
    pen.move(UP)

def F():
    global myVariable, size, direction
    pen.move(DOWN)
    drivetrain.drive_for(FORWARD, (size * 2), MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, size, MM)
    drivetrain.drive_for(REVERSE, size, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, size, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, size, MM)
    drivetrain.drive_for(REVERSE, size, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(REVERSE, size, MM)
    pen.move(UP)

def initials():
    global myVariable, size, direction
    F()
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, (size * 2), MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    Y()

def when_started1():
    global size, direction
    direction = 30
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 700, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    size = 400
    initials()
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 500, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(REVERSE, 500, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(REVERSE, 500, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    size = 200
    pen.set_pen_color_rgb(179, 95, 255, 100)
    drivetrain.turn_for(RIGHT, direction, DEGREES)
    initials()

vr_thread(when_started1)

