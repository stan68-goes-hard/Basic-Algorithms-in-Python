import math
import time

def endless_sinus_generator():
    angle = 0
    while True:
        value = math.sin(math.radians(angle))
        print(value)
        angle = (angle + 1) % 360
        time.sleep(0.005)  # Adjust the sleep time as needed
        bar_length = int((value + 1) * 36)  # Scale the value to fit in a range of 0 to 20
        bar = '*' * bar_length
        print(f"{value:.2f} \n {bar}")
if __name__ == "__main__":
    endless_sinus_generator()
