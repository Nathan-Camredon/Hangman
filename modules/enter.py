import keyboard

def letter_press():
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and len(event.name) == 1 and event.name.isalpha():
                return event.name
