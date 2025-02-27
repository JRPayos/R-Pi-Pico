# Numbers of 1-4, GPIO 2-5
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
    "one": digitalio.DigitalInOut(board.GP2),
    "two": digitalio.DigitalInOut(board.GP3),
    "three": digitalio.DigitalInOut(board.GP4),
    "four": digitalio.DigitalInOut(board.GP5),
}

# Configure buttons as inputs with pull-up resistors
for button in buttons.values():
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP  # Pull-up resistor (active-low)

# Key mapping (Send numbers 1, 2, 3, 4)
key_mapping = {
    "one": Keycode.ONE,
    "two": Keycode.TWO,
    "three": Keycode.THREE,
    "four": Keycode.FOUR,
}

# Track previous button states to detect "new" presses
previous_states = {name: True for name in buttons}  # True = Not Pressed (Pull-up)

while True:
    for name, button in buttons.items():
        current_state = button.value  # Read current button state

        if not current_state and previous_states[name]:  # Detect new button press
            kbd.press(key_mapping[name])  # Send key press
            time.sleep(0.1)  # Short debounce
            kbd.release_all()  # Release key

        previous_states[name] = current_state  # Update previous state

    time.sleep(0.01)  # Small delay to reduce CPU usage
