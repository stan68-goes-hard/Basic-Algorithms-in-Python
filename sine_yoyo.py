import math
import time
import RPi.GPIO as GPIO 

# Set up GPIO

#        GPIO.setmode(GPIO.BCM)
#        BUTTON_PIN = 17
#        GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)#


# sine calculation and prompting


def endless_sinus_generator():
    angle = 0

    i: float    
    i = 0            # Timer start value
    while True:
        value = math.sin(math.radians(angle))
        print(value)
        angle = (angle + 1) % 360
        time.sleep(0.01)  # Adjust the sleep time as needed
        bar_length = int((value + 1) * 18)  # Scale the value to fit in a range of 0 to 20
        bar = '\n*' * bar_length
        print(bar) 
        #timer
        i = i+1
        print(i)
        
            print(i)
            print("5 minutes have passed. Exiting...")
            i=0
            break                                                       # Timer 
                                                       # Timer
        #timer end 
        
#        # Button press detection
#        try:
#            while True:
#                button_state = GPIO.input(BUTTON_PIN)
#                if button_state == GPIO.LOW:
#                    print("Button Pressed")
#                time.sleep(0.1)  # Adjust the sleep time as needed
#        except KeyboardInterrupt:
#            pass
#        finally:
#            GPIO.cleanup()



    


if __name__ == "__main__":
    endless_sinus_generator()
    # To compile this script into an executable, you can use a tool like PyInstaller.
    # First, install PyInstaller if you haven't already:
    
    # If you have a RPi5 or RPi4, you can install PyInstaller using the following command:
    # $python -m venv env
    #Before you work on a project, run the following command from the root of the project to start using the virtual environment:
    # $source env/bin/activate
    # You should then see a prompt similar to the following:
    # (env) $
    # When you finish working on a project, run the following command from any directory to leave the virtual environment:
    # $deactivate



    # Then, you can compile the script by running the following command in your terminal:
    # pyinstaller --onefile "/home/stan68/Basic Algorythms Python/sinus yoyo graphical generator.py"

    # This will create a single executable file in the "dist" directory.