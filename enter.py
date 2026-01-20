import keyboard

def letter_press():
        while True:
            key = keyboard.read_key()
            if len(key) == 1 and key.isalpha():
                return key
