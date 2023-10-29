# -*- coding: utf-8 -*-
"""talking_clock.ipynb

Created by Xinyi Ma, Wansu Zhu, Xueying Liu, Cathy Ting Zhang, and Sherry Yu-Ting Yeh.
at the Rijksuniversiteit Groningen/Campus Fryslan.
29.10.2023 Final Version

"""

import tkinter as tk
import subprocess
import pygame
import math
import time
import os
import threading
import re
import pytz
import tkinter.messagebox as messagebox
from time import strftime
from tkinter import ttk
from PIL import Image, ImageTk
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime

# Initialize pygame mixer
pygame.mixer.init()

# General root
root = tk.Tk()
root.title('Analog Clock')


# To use this code, need to install espeak first: brew install espeak
# brew install espeak-data
def text_to_speech_english(text):
    subprocess.call(["espeak", text])

def text_to_speech_mandarin(text):
    subprocess.call(["espeak", "-v", "zh+m1", text])


#********************************************************************************************************************
# Create left panel
left_frame = ttk.Frame(root, padding=(30, 15))
left_frame.grid(row=0, column=0, sticky="ns")

# Time zone listbox layout
text_field_1 = tk.Label(left_frame, text="Select Time Zone")
text_field_1.grid(row=0, column=0, pady=10)

listbox_1 = tk.Listbox(left_frame, selectmode=tk.SINGLE, height=3)
listbox_1.insert(1, "Europe/Amsterdam")
listbox_1.insert(2, "Asia/Chongqing")
listbox_1.grid(row=1, column=0, pady=10)

#********************************************************************************************************************
# Switch time zone & draw the clock

selected_time_zone = 'Europe/Amsterdam'
listbox_1.select_set(0)  # set a default time zone

# Bind time zone selection event to listbox
def on_select(evt):
    global selected_time_zone
    w = evt.widget
    index = int(w.curselection()[0])
    selected_time_zone = w.get(index)
    update_clock(selected_time_zone)

listbox_1.bind('<<ListboxSelect>>', on_select)

def update_clock():
    current_time = datetime.now(pytz.timezone(selected_time_zone))
    seconds = current_time.second
    minutes = current_time.minute
    hours = current_time.hour

    # Calculate the angles for the clock hands
    second_angle = -math.radians(seconds * 6) + math.pi / 2
    minute_angle = -math.radians((minutes * 6) + (seconds / 10)) + math.pi / 2
    hour_angle = -math.radians((hours * 30) + (minutes / 2)) + math.pi / 2

    # Clear the canvas
    canvas.delete('all')

    # Set the background image as the canvas background
    canvas.create_image(0, 0, anchor='nw', image=background)

    # Draw clock hands
    draw_hand(second_angle, 80, 'grey')
    draw_hand(minute_angle, 70, 'brown')
    draw_hand(hour_angle, 50, 'brown')

    # Digital clock
    current_time_struct = current_time.timetuple() # current_time type: datetime_datetime (convert to struct_time argument)
    digital_time = time.strftime("%H:%M:%S", current_time_struct) #"%I:%M:%S %p" for 12 hours
    canvas.create_text(150, 330, text=digital_time, font=('Helvetica', 25, 'bold'), fill='white')

    # Draw clock interface markings
    draw_markings()

    # Update the clock every 1000ms (1 second)
    root.after(1000, update_clock)


#********************************************************************************************************************
# Current time function
def tell_time_male_madarin():
    global selected_time_zone
    current_time = datetime.now(pytz.timezone(selected_time_zone))
    current_time_struct = current_time.timetuple()
    time_string = time.strftime("%I:%M %p", current_time_struct)
    if __name__ == "__main__":
        text_to_speech_mandarin(f'现在是 {time_string}')

def tell_time_female_madarin():
    global selected_time_zone
    current_time = datetime.now(pytz.timezone(selected_time_zone))
    current_time_struct = current_time.timetuple()
    time_string = time.strftime("%I:%M %p", current_time_struct)
    mp3_fp = BytesIO()
    tts = gTTS(f'现在是{time_string}', lang='zh-CN')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    audio = AudioSegment.from_mp3(mp3_fp)
    play(audio)

def say_current_time():
    if get_gender() == 'Male' and get_language() == 'English':
        play_male_english()
    elif get_gender() == 'Female' and get_language() == 'English':
        play_female_english()
    elif get_gender() == 'Male' and get_language() == 'Mandarin':
        tell_time_male_madarin()
    elif get_gender() == 'Female' and get_language() == 'Mandarin':
        tell_time_female_madarin()

say_time_button = ttk.Button(left_frame, text="Announce Current Time", command=say_current_time)
say_time_button.grid(row=14, column=0, pady=5)

#********************************************************************************************************************
# Create the right side clock interface

right_frame = ttk.Frame(root, padding=(30, 15))
right_frame.grid(row=0, column=1, sticky="nsew")

def draw_hand(angle, length, color):
    x = 150 + length * math.cos(angle)
    y = 150 - length * math.sin(angle)
    canvas.create_line(150, 150, x, y, fill=color, width=3)

# Create a list of colors for the numbers
number_colors = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']

# Create a function to draw clock interface markings
def draw_markings():
    # Draw numbers 1 to 12 around the clock face
    for i in range(1, 13):
        angle = -math.radians((i * 30)) + math.pi / 2
        x = 150 + 110 * math.cos(angle)
        y = 150 - 110 * math.sin(angle)
        color = number_colors[i - 1]  # Assign a color from the list based on the number
        canvas.create_text(x, y, text=str(i), font=('Helvetica', 12, 'bold'), fill=color)

# Load the background image using Pillow
background_image = Image.open('background_day.jpg')  # Replace 'background_day.jpg' with your image file path
background = ImageTk.PhotoImage(background_image)

# Create a canvas to draw the clock
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.grid(row=0, column=2)

# Start the clock update function
update_clock()


#********************************************************************************************************************
# Hourly time anouncement function

# Remind users to click both buttons to confirm and start hourly time anouncement
def check_selections():
    selected_gender = selected_voice.get()
    selected_lang = selected_language.get()
    if selected_gender and selected_lang:
        messagebox.showinfo("Info", "Gender and language set! Time will be announced.")
    else:
        messagebox.showwarning("Warning", "Please select both gender and language.")

confirm_button = ttk.Button(left_frame, text="Activate Hourly Time Anouncement", command=check_selections)
confirm_button.grid(row=13, column=0, pady=5)


def check_time_loop():
    while True:
        current_time = time.localtime() #type: tuple
        current_minute = current_time.tm_min #type: integer
        current_hours = current_time.tm_hour

        if current_minute == 0:
            time_string = time.strftime("%I:%M %p", current_time)
            print(f"Current time string: {time_string}")
            if get_gender() == 'Male' and get_language() == 'English':
                play_male_english()
            elif get_gender() == 'Female' and get_language() == 'English':
                play_female_english()
            elif get_gender() == 'Male' and get_language() == 'Mandarin':
                play_male_mandarin()
            elif get_gender() == 'Female' and get_language() == 'Mandarin':
                play_female_mandarin()

        time.sleep(6)  # Sleep for n seconds before checking again


def play_male_english():
    global selected_time_zone
    current_time = datetime.now(pytz.timezone(selected_time_zone))
    current_time_struct = current_time.timetuple()
    time_string = time.strftime("%I:%M %p", current_time_struct)
    if __name__ == "__main__":
        text_to_speech_english(f'It is {time_string}')

def play_female_english():
    global selected_time_zone
    current_time = datetime.now(pytz.timezone(selected_time_zone))
    current_time_struct = current_time.timetuple()
    time_string = time.strftime("%I:%M %p", current_time_struct)
    mp3_fp = BytesIO()
    tts = gTTS(f'it is {time_string}', lang='en')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    audio = AudioSegment.from_mp3(mp3_fp)
    play(audio)

def play_male_mandarin():
    global selected_time_zone
    current_time = datetime.now(pytz.timezone(selected_time_zone))
    current_time_struct = current_time.timetuple()
    current_hours = current_time_struct.tm_hour
    audio_file_path = f'Mandarin_Male_MP3/M_M_{current_hours}.mp3'
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

def play_female_mandarin():
    global selected_time_zone
    current_time = datetime.now(pytz.timezone(selected_time_zone))
    current_time_struct = current_time.timetuple()
    current_hours = current_time_struct.tm_hour
    audio_file_path = f'Mandarin_Female_MP3/M_F_{current_hours}.mp3'
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

def get_gender():
    gender = selected_voice.get() # Convert StringVar to String
    return gender

def get_language():
    language = selected_language.get()
    return language

thread = threading.Thread(target=check_time_loop)
thread.start()

if thread.is_alive(): # check
    print("Thread is running.")
else:
    print("Thread is not running.")




#********************************************************************************************************************
# Set alarm
def validate_date_input(input_text):
    # Regular expression pattern for YYYY-MM-DD date format
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    if re.fullmatch(date_pattern, input_text):
        return True
    return False

def alarm_setting():
    def save_alarm():
        selected_date = date_entry.get()
        selected_hour = combobox_hour.get()
        selected_minute = combobox_minute.get()
        alarm_datetime = f"{selected_date} {selected_hour}:{selected_minute}"
        alarms.append(alarm_datetime)
        alarm_listbox.insert("end", alarm_datetime)
        alarm_window.destroy()

    def stop_alarm():
        pygame.mixer.music.stop()
        alarm_window.destroy()

    alarm_window = tk.Toplevel(root)
    alarm_window.title("Set Alarm")

    label_date = tk.Label(alarm_window, text="Date (YYYY-MM-DD)")
    label_date.pack()

    date_entry = ttk.Entry(alarm_window, validate="key", validatecommand=(validate_date_input, "%P"))
    date_entry.pack()

    label_time = tk.Label(alarm_window, text="Time")
    label_time.pack()

    label_hour = tk.Label(alarm_window, text="Hour")
    label_hour.pack()
    hour = list(map(str, range(25)))
    combobox_hour = ttk.Combobox(alarm_window, values=hour)
    combobox_hour.pack()

    label_minute = tk.Label(alarm_window, text="Minute")
    label_minute.pack()
    minute = list(map(str, range(61)))
    combobox_minute = ttk.Combobox(alarm_window, values=minute)
    combobox_minute.pack()

    save_button = tk.Button(alarm_window, text="Save Alarm", command=save_alarm)
    save_button.pack()


alarms = []  # List to store saved alarm times

alarm_listbox = tk.Listbox(left_frame)
alarm_listbox.grid(row=4, column = 0)

button1 = tk.Button(left_frame, text="Set Alarm", command=alarm_setting)
button1.grid(row = 5, column=0, pady =10)

def alarm_thread_func():
    while True:
        current_datetime = time.strftime("%Y-%m-%d %H:%M")
        for alarm_datetime in alarms:
            if current_datetime == alarm_datetime:
                alarm_window = tk.Toplevel(root)
                alarm_window.title("Alarm")
                alarm_label = tk.Label(alarm_window, text=f"Alarm at {alarm_datetime}")
                alarm_label.pack()
                stop_button = tk.Button(alarm_window, text="Stop Alarm", command=stop_alarm)
                stop_button.pack()
                audio_file_path = 'starwars.wav'
                pygame.mixer.music.load(audio_file_path)
                pygame.mixer.music.play()
                time.sleep(300)  # Alarm rings for 5 minutes (300 seconds)
                alarm_window.destroy()

def stop_alarm():
    pygame.mixer.music.stop()
    alarm_window.destroy()

alarm_thread = threading.Thread(target=alarm_thread_func)
alarm_thread.daemon = True
alarm_thread.start()


#********************************************************************************************************************
# This part is mainly for the hourly time anouncement function
# We defined variables to store the selected gender and language with the aim of using different voices to anounce time


# Create a label to instruct the user
prompt_label = tk.Label(left_frame, text="Please select gender and language first",fg="#ED9121")
prompt_label.grid(row=6, column=0, pady=10)

# Select voice
label=ttk.Label(left_frame, text = "Select the Vocie Sex :")
label.grid(row = 7, column=0, pady =10 )

selected_voice = tk.StringVar()  # Create a StringVar object to store the selected voice
sexchoice = ttk.Combobox(left_frame, width = 20, textvariable = selected_voice)
sexchoice['values'] = ("Female", "Male")
sexchoice.grid(row=8, column = 0)

change_gender = ttk.Button(left_frame, text="Confirm", command=get_gender) #get_gender funcition is defined in the Hourly time anouncement part
change_gender.grid(row=9, column=0, pady=5)


# Select language
label=ttk.Label(left_frame, text = "Select Language :")
label.grid(row = 10, column=0, pady =10 )

selected_language = tk.StringVar()  # Create a StringVar object to store the selected language
languagechoice = ttk.Combobox(left_frame, width = 20, textvariable = selected_language)
languagechoice['values'] = ("English", "Mandarin")
languagechoice.grid(row=11, column = 0)

change_language = ttk.Button(left_frame, text="Confirm", command=get_language) #get_language funcition is also defined in the Hourly time anouncement part
change_language.grid(row=12, column=0, pady=5)



#********************************************************************************************************************

root.mainloop()

