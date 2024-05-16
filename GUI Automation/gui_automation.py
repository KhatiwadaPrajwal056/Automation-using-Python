'''
    There are two versions of same function, one for normal os and one for mac os.
    Since the library hasn't been fixed yet,
    we have to divide the center location by 2 and 
    thus we will get the image location and the rest is same.
'''
import pyautogui
import time
import os



# Change directory to the script's directory
os.chdir(os.path.dirname(__file__))

# Paths to images
moles = ["assets/mole1_mac.png", "assets/mole2_mac.png"]
START_BUTTON = "assets/start_button_mac.png"
CONTINUE_BUTTON = "assets/continue_button.png"

def click_button(image_path, button_name):
    """
    Locate and click a button on the screen.

    Parameters:
        image_path (str): Path to the button image.
        button_name (str): Name of the button for display purposes.
    """
    print(f"Locating {button_name} Button!")
    try:
        button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        print(button_location)
        pyautogui.click(button_location)
    except pyautogui.ImageNotFoundException:
        print(f"Error locating {button_name} button!")

def click_button_mac(image_path, button_name):
    """
    Locate and click a button on the screen for Mac (Retina Display). Give permission to Vscode and the web-browser for screen recording from settings

    Parameters:
        image_path (str): Path to the button image.
        button_name (str): Name of the button for display purposes.
    """
    print(f"Locating {button_name} Button!")
    try:
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        print(button_location)
        x = button_location.x / 2
        y = button_location.y / 2
        pyautogui.click(x,y)
    except pyautogui.ImageNotFoundException:
        print(f"Error locating {button_name} button!")


def whack_mole():
    """
    Whack moles on the screen.
    """
    for mole_image in moles:
        try:
            moles_location = pyautogui.locateOnScreen(mole_image, confidence=0.8,grayscale=True)
            pyautogui.click(moles_location)
            print("Whacked!")
        except pyautogui.ImageNotFoundException:
            print("No Mole on Screen")

def whack_mole_mac():
    """
    Whack moles on the screen for mac_devices.
    """
    for mole_image in moles:
        try:
            moles_location = pyautogui.locateCenterOnScreen(mole_image, confidence=0.8)
            x = moles_location.x/2
            y = moles_location.y/2
            pyautogui.click(x,y)
            print("Whacked!")
        except pyautogui.ImageNotFoundException:
            print("No Mole on Screen")

if __name__ == "__main__":
    time.sleep(5) # 10 seconds of timer to manually open the https://plays.org/whack-a-mole/ site and make it ready with Start Button on Screen
    # click_button(CONTINUE_BUTTON, "Continue")
    # click_button(START_BUTTON, "Start")
    click_button_mac(CONTINUE_BUTTON, "Continue")
    click_button_mac(START_BUTTON, "Start")
    while True:
        whack_mole_mac()
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage
