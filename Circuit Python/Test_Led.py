import time
import board
import digitalio

# Define the LED pins
led1 = digitalio.DigitalInOut(board.GP0)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP1)
led2.direction = digitalio.Direction.OUTPUT

while True:
    led1.value = True  # Turn on LED 1
    led2.value = False # Turn off LED 2
    time.sleep(0.1)    # Wait 500ms
    
    led1.value = False # Turn off LED 1
    led2.value = True  # Turn on LED 2
    time.sleep(0.1)    # Wait 500ms
