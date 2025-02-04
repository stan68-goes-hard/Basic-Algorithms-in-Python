import math
import time

def endless_sinus_generator():
    angle = 0
    while True:
        value = math.sin(math.radians(angle))
        print(value)
        angle = (angle + 1) % 360
        time.sleep(0.01)  # Adjust the sleep time as needed

if __name__ == "__main__":
    endless_sinus_generator()