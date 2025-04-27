import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui,pyperclip

# Set up Chrome options
chrome_options = Options()
# attach to existing Chrome on port 9222
chrome_options.debugger_address = "127.0.0.1:9222"

# Set up the Chrome service using ChromeDriverManager
service = Service(ChromeDriverManager().install())
# launch driver with debug port options
driver = webdriver.Chrome(service=service, options=chrome_options)

for i in range(58):
    # URL to open
    url = "https://www.futureskillsprime.in/iDH/fsp/Dashboard/Products_detail/163111434"

    # Open the URL
    driver.get(url)
    time.sleep(4)  # wait for page to initialize before injecting JS

    # load and inject automation script so functions become globals
    with open("nasscom_auto.js", "r") as f:
        nasscom_script = f.read()
    driver.execute_script("""
        var s = document.createElement('script');
        s.type = 'text/javascript';
        s.textContent = arguments[0];
        document.head.appendChild(s);
    """, nasscom_script)


    # orchestrate steps
    driver.execute_script("findCurrentCourse();")
    time.sleep(4)
    driver.execute_script("markAsComplete();")
    time.sleep(30)
    driver.execute_script("launch_quiz();")
    time.sleep(10)

    # switch to quiz window
    main_window = driver.current_window_handle
    all_windows = driver.window_handles
    quiz_window = [w for w in all_windows if w != main_window][0]
    driver.switch_to.window(quiz_window)



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
    time.sleep(1)  # Add a small delay to ensure the script is fully typed out
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


    driver.close()
    driver.switch_to.window(main_window)

    # Example: Find an element and print its text

    # Wait for page to load
    time.sleep(2)



# Close the browser
driver.quit()