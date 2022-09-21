def on_button_pressed_a():
    sprite.move(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    sprite.move(-1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    sprite.move(-1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    sprite.move(1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

sprite: game.LedSprite = None
sprite = game.create_sprite(0, 0)

def on_forever():
    pass
basic.forever(on_forever)
