import math
import time

def endless_sinus_generator():
    angle = 0
    while True:
        value = math.sin(math.radians(angle))
        print(value)
        angle = (angle + 1) % 360
        time.sleep(0.01)  # Adjust the sleep time as needed
        bar_length = int((value + 1) * 4000)  # Scale the value to fit in a range of 0 to Endless. 
        #Note: after the value reaches the maximum number of characters in the console, it starts printing with doubled frequency.
        bar = "*" * bar_length
        print(f"{value:.2f} \n {bar}")
        if bar_length > 4361:
					
                print(""" 
                
  /$$     /$$ /$$$$$$  /$$   /$$ /$$$$$$$         /$$$$$$  /$$$$$$$  /$$   /$$       /$$$$$$  /$$$$$$         /$$$$$$  /$$   /$$       /$$$$$$$$ /$$$$$$ /$$$$$$$  /$$$$$$$$
 |  $$   /$$//$$__  $$| $$  | $$| $$__  $$       /$$__  $$| $$__  $$| $$  | $$      |_  $$_/ /$$__  $$       /$$__  $$| $$$ | $$      | $$_____/|_  $$_/| $$__  $$| $$_____/
  \  $$ /$$/| $$  \ $$| $$  | $$| $$  \ $$      | $$  \__/| $$  \ $$| $$  | $$        | $$  | $$  \__/      | $$  \ $$| $$$$| $$      | $$        | $$  | $$  \ $$| $$      
   \  $$$$/ | $$  | $$| $$  | $$| $$$$$$$/      | $$      | $$$$$$$/| $$  | $$        | $$  |  $$$$$$       | $$  | $$| $$ $$ $$      | $$$$$     | $$  | $$$$$$$/| $$$$$   
    \  $$/  | $$  | $$| $$  | $$| $$__  $$      | $$      | $$____/ | $$  | $$        | $$   \____  $$      | $$  | $$| $$  $$$$      | $$__/     | $$  | $$__  $$| $$__/   
     | $$   | $$  | $$| $$  | $$| $$  \ $$      | $$    $$| $$      | $$  | $$        | $$   /$$  \ $$      | $$  | $$| $$\  $$$      | $$        | $$  | $$  \ $$| $$      
     | $$   |  $$$$$$/|  $$$$$$/| $$  | $$      |  $$$$$$/| $$      |  $$$$$$/       /$$$$$$|  $$$$$$/      |  $$$$$$/| $$ \  $$      | $$       /$$$$$$| $$  | $$| $$$$$$$$
     |__/    \______/  \______/ |__/  |__/       \______/ |__/       \______/       |______/ \______/        \______/ |__/  \__/      |__/      |______/|__/  |__/|________/
                                                                                                                                                                         
                
                """
                )
                
            
                    
        
            
 

if __name__ == "__main__":
    endless_sinus_generator()
