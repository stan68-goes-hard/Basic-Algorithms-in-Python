import tkinter as tk
from mfrc522 import SimpleMFRC522

import RPi.GPIO as GPIO

reader = SimpleMFRC522()

def read_rfid():
    try:
        id, text = reader.read()
        result_label.config(text=f"ID: {id}\nText: {text}")
    finally:
        GPIO.cleanup()

def write_rfid():
    try:
        text = entry.get()
        reader.write(text)
        result_label.config(text="Write successful")
    finally:
        GPIO.cleanup()

# Create the main window
root = tk.Tk()
root.title("RFID Read/Write")

# Create and place the widgets
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

read_button = tk.Button(root, text="Read", command=read_rfid)
read_button.pack(pady=5)

write_button = tk.Button(root, text="Write", command=write_rfid)
write_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()