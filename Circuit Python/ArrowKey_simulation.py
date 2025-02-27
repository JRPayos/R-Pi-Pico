import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)

# Define buttons and their GPIOs
buttons = {
    "up": digitalio.DigitalInOut(board.GP2),
    "down": digitalio.DigitalInOut(board.GP3),
    "left": digitalio.DigitalInOut(board.GP4),
    "right": digitalio.DigitalInOut(board.GP5),
}

# Configure buttons as inputs with pull-up resistors
for button in buttons.values():
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP  # Pull-up resistor (active-low)

# Key mapping
key_mapping = {
    "up": Keycode.UP_ARROW,
    "down": Keycode.DOWN_ARROW,
    "left": Keycode.LEFT_ARROW,
    "right": Keycode.RIGHT_ARROW,
}

while True:
    for name, button in buttons.items():
        if not button.value:  # Button pressed (active-low)
            kbd.press(key_mapping[name])  # Send key press
            time.sleep(0.3)  # Debounce, delay to repeat the key if keypress is hold
            kbd.release_all()  # Release key

    time.sleep(0.01)  # Small delay to avoid CPU overuse

