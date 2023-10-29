# Back to Nature Clock with customized Star Wars Alarm ### 


<img width="611" alt="image" src="https://github.com/xuliu15/talking-clock/assets/144012055/2d18094a-1330-4a22-bf95-1cecabaedc98">



## 7.1 Installation
### STEPS TO RUN AND INSTALL HAVE BEEN TESTED USING MAC OS. THERE MAY BE ISSUES OCCURRING FOR LINUX AND WINDOWS SO BE ADVISED! 

Click on the green Code button at the top of the repository > Download ZIP.
Extract the ZIP to the location where you want to install it on your computer.
(You can also just clone the repository locally if you are familiar with Git. In that case, the steps above can be skipped)

Open the terminal (or command prompt, depending on the OS you use) and navigate to where you extracted the zip via the terminal.

### Requirements before installing  
Make sure you have Python 3.9 installed. Download the latest 3.9 version from here: https://www.python.org/downloads/

### How to Run  
Run python main.py in the terminal. Make sure to be in the same directory where the repository is installed in the terminal. It will open an interactive Graphical User Interface.
You need to install all necessary packages before running the code. Here is a summary of the third-party libraries your code requires and how to install them:
- Pillow (PIL): You can install it by running `pip install Pillow`.
- gTTS (Google Text-to-Speech): You can install it with `pip install gTTS`.
- pygame: You can install it via `pip install pygame`.
- pydub: You can install it using `pip install pydub`.
- espeak. With MacOS, use ‘brew install espeak’.
Next, run the file code.py from the root directory with the command python code.py.

One window will open when the command is executed. The window contains the analog clock (with the digital clock right below) on the background picture on the right and control panels on the left.

To start, choose voice sex and language first (this friendly reminder is displayed in light orange on the control panels as well), then you can play around with whether you would like the clock to announce the current time by clicking “Announce Current Time”, or let the clock remind you time elapsing hour by hour by pressing the button of “Activate Hourly Time Announcement”. On the top left, you are able to choose the timezone in Amsterdam or Chongqing, once you click one of them, you will notice the analog clock and digital clock change accordingly. This clock across two time zones is beneficial when you would like to schedule a business meeting or call with the family across time zones. You can do so by setting up an alarm by clicking “Set Alarm”, you would have to manually type in year-month-day, however, the drop-down menu for hours and minutes is available. Once the current time hits the scheduled alarm time, you shall hear the theme songs of Star Wars. Just like how you set alarms on your phones, multiple entries of the alarms are allowed, but the subsequent alarms cannot ring due to coding limitations. 

## 7.2 Team Organization and Project Workflow 

This is the speaking/talking clock that we developed in Python 3.9 for an assignment for the course "Introduction to Voice Technology" and “Programming” as part of the Voice Technology MSc at RUG - Campus Fryslan. 

The team members are Xinyi Ma, Wansu Zhu, Xueying Liu, Cathy Ting Zhang, and Sherry Yu-Ting Yeh. 
Our initial brainstorms aim to construct the clock with the following features: time zones, set alarm, change gender, change voice (this specifically refers to voice quality, such that we originally intended to incorporate the voice of SpongeBob SquarePants), and change languages. We assigned each function to specific team members and then discussed how to integrate all these functions. During our discussions, we encountered new problems, which we promptly reassigned to team members for resolution. We continued to work together to tackle these challenges.

- Xinyi Ma: Basic interface design. Current Time function. Synthesis voice recordings. Video presentation. 
- Wansu Zhu: Alarm function. Interface improvements. Video presentation. 
- Xueying Liu: Hourly and current time announce functions (for both genders and languages), Video presentation. 
- Cathy Ting Zhang: Time zone function. Time announcement function. Actual human voice recordings. Video presentation. 
- Sherry Yu-Ting Yeh: Analog clock, digital clock, and the background picture. Documentation.


## 7.3 The resource documentation and technical reflection


TThe repository contains the folder "Audios" that includes the mp3 files the programme uses. Mandarin_Male_MP3 include Mandarin male voice that were generated and downloaded from (https://www.narakeet.com/languages/). Mandarin_Female_MP3 include Madarin female voice recorded by our team member Cathy Ting Zhang. These files are for hourly time announcement. 


The background_day.jpg file in the repository is used as the background picture for the clock window.


As for the background picture, we initially aim to construct an interface that can automatically change the background picture once the clock hits 6 p.m. and then change the background picture back again at 6 am. However, several attempts have resulted in missing background pictures (i.e. the interface ended up displaying the clock without background pictures) or the numbers on the clock disappeared. Therefore we decided to keep only one background picture. The background picture for nighttime has been eliminated. Furthermore, the background picture results in a variety of displays on different laptops, the background picture is either missing or becomes a “zoom-in” version that displays only the top left corner which is the sky. 

The alarm function runs successfully in the local time (Amsterdam timezone), but we didn't manage to connect it with time zone switching function due to time limit. 

## 7.4 GUI user manual

Back to Nature Clock provides intuitive operation for users. There is a digital clock display in the 24-hour format down below the analog clock, allowing users to figure out daytime or night. It enables users to choose a time zone in either Amsterdam (Europe) or Chongqing (Asia) and announce the current time with synthetic voice, with the option of both female and male voicing, Mandarin and English voicing. The synthesized voices in the current time announcement were produced by espeak( for male Mandarin and English) and gTTS (for female English and Mandarin).The hourly time announcement function is also available, along with the customization in voice by gender (female/male) and language (English/ Mandarin). Kindly note that the real human voice was used only for hourly time announcements in Mandarin female voice. 

### Linguistic Rules for Time Announcement 
While English typically announces time in an AM/PM manner, Mandarin tends to split 24 hours into more time blocks–as in morning, noon, afternoon, evening, and midnight, etc.  The time announcement works in a way that time blocks preceding the exact time (hours and minutes). The other difference is that, for example, 12:30, in English can be displayed as twelve thirty or half past twelve, in both progressive and regressive (announcing minutes first, followed by hours) manner, while Mandarin can only display in a progressive manner.  On a side note, in Mandarin, there are two different characters (which also have different pronunciations) representing the number “2”. In this case, the user may notice 12 and 2 sounds phonetically different as 12  is shí èr, while 2 is liǎng. Variety of characters or pronunciation for the same number is not uncommon—Japanese also serves as an example when it comes to pronouncing numbers in different contexts. Furthermore, the concept of o'clock in English is pretty much equivalent to diǎn in Mandarin. However, while in English 12:30 can be announced as twelve thirty without uttering “o'clock”, every time announcement in Mandarin will require the utterance of “diǎn” between hours and minutes. Simply put, spelling out twelve-thirty in Mandarin is not allowed, it will be  "shí èr (twelve) diǎn sānshí(thirty) fēn(minutes)". In Mandarin, the corresponding concept of “half” will be "bàn", so it is also valid to say  "shí èr (twelve) diǎn bàn(thirty, half of 60 mins). 



## 7.5 Licensing statement / reflection FAIR data / GDPR Compliance
The audio files used were generated from  https://www.narakeet.com/languages/
The consent form for the collection of this data is attached since the only actual human voice was recorded by our team member Ting Zhang. 
The data used for the speaking clock therefore complies with GDPR regulations.


