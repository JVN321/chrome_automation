

import pyautogui,time
import pyperclip
import time
import random

# Locate the image on the screen
try:
    location = pyautogui.locateCenterOnScreen('start.png', confidence=0.7)
    if location is not None:

        pyautogui.click(location.x, location.y)
        time.sleep(1)
        pyautogui.press('f12')
        time.sleep(1)
        location = pyautogui.locateCenterOnScreen('inspect_icon.png', confidence=0.7)
        pyautogui.click(location.x, location.y)
        time.sleep(1)
        location = pyautogui.locateCenterOnScreen('submit.png', confidence=0.7)
        pyautogui.click(location.x, location.y)
        time.sleep(1)
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(4)
try:
    location = pyautogui.locateCenterOnScreen('console.png', confidence=0.7)
    pyautogui.click(location.x, location.y)
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(3)
with open("nasscom_quiz.js", "r") as f:
    quiz_script = f.read()
    pyperclip.copy(quiz_script) 


pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')

delay = random.randint(70, 90)
time.sleep(delay)

try:
    location = pyautogui.locateCenterOnScreen('final_submit.png', confidence=0.7)
    if location is not None:
        pyautogui.click(location.x, location.y)
        time.sleep(1)
except Exception as e:
    print(f"An error occurred: {e}")

