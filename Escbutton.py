import keyboard

pressed = False

def on_press():
    global pressed
    if not pressed:
        keyboard.write("`")
        pressed = True

def on_release():
    global pressed
    pressed = False

keyboard.add_hotkey("alt+q", on_press)
keyboard.on_release_key("q", lambda e: on_release())

keyboard.wait()