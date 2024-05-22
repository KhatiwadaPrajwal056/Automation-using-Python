#  Install pyautogui
#  pyautogui lets your Python scripts control the mouse and keyboard to automate interactions with other applications.

# opencv
# update -U pillow
# opencv-python
# opencv-python--user

import pyautogui as gui
from time import sleep
import urllib
# mouse operation: movements,clicks,scroll
# Location on your screen is determined by (x,y) . It starts from top left corner (0,0) and bottom will be the your resoution.

# check your resolution:
# print(gui.size()) 

# current coordinate of your mouse
# print(gui.position())
# while(1):
#     print(gui.position())
#     sleep(1)

 # I can also write as :
# x,y = gui.position()
# check if cursor is on screen or not
# print(gui.onScreen(x,y))
# print(gui.onScreen(x,-1))


# Lets see some insteresting functions

# Move the mouse
# gui.moveTo(100,500) # this generally moves the mouse
# gui.moveTo(100,500,1) # moves the mouse in 1 sec

# moving cursor relative to current position:
# gui.moveRel(-550,-500,0.5)


# draging the mouse (hold and click)
# gui.dragRel(0,-300,button="left",duration=0.4) # relative
# gui.dragTo(100,100,button="left",duration=0.4)

# clicking the mouse
# gui.click() # single click
# gui.doubleClick(duration=1) # double click

# instead of double click function we can use:
# gui.click(clicks=2,duration=1)

# scroll the mouse: +ve scrolls up and -ve scrolls down
# gui.scroll(200)


#keyboard functions:

# gui.write("hello")

# this function has limitation to praess shift or ctrl+c etc.
# for the alternative we have::
# gui.hotkey("ctrl","c")
# gui.hotkey("ctrl","v")

# taking screenshot
# img = gui.screenshot()
# img.save(r"/Users/khatiwadaprajwal22icloud.com/Desktop/untitled folder 2/screenshot1.png")

# others function: imagenotfound ¶ locatecenteronscreen


# gui.ImageNotFoundException
import os

os.chdir("/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/Automation-using-Python/GUI Automation")

moles = ["assets/mole1_mac.png","assets/mole2_mac.png"]
START_BUTTON = "assets/start_button_mac.png"
CONTINUE_BUTTON = "assets/continue_button.png"
 
def click_button_mac(image_path, button_name):
    """
    Locate and click a button on the screen for Mac (Retina Display). Give permission to Vscode and the web-browser for screen recording from settings

    Parameters:
        image_path (str): Path to the button image.
        button_name (str): Name of the button for display purposes.
    """
    print(f"Locating {button_name} Button!")
    try:
        button_location = gui.locateCenterOnScreen(image_path, confidence=0.8)
        print(button_location)
        x = button_location.x / 2
        y = button_location.y / 2
        gui.click(x,y)
    except gui.ImageNotFoundException:
        print(f"Error locating {button_name} button!")

def hit_the_mole():
    # this function will hit the mole if appears on the screen.
    for mole in moles:
        try:
            x,y = gui.locateCenterOnScreen(mole,confidence=0.8)
            # The optional confidence keyword argument specifies the accuracy with which the function should locate the image on screen. This is helpful in case the function is not able to locate an image due to negligible pixel differences:
            gui.click(x/2,y/2)
            print("Mole hit")
        except gui.ImageNotFoundException:
            print("No mole found")
        
sleep(3)
click_button_mac(CONTINUE_BUTTON, "Continue")
click_button_mac(START_BUTTON, "Start")
while (1):
    hit_the_mole()
    sleep(0.1)


