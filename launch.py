from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
# Set up the Chrome driver
# Set up Chrome options
chrome_options = Options()
# keep DevTools port constant
chrome_options.add_argument("--remote-debugging-port=9222")


# Set up the Chrome service using ChromeDriverManager
service = Service(ChromeDriverManager().install())
# pass options into the driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to open
url = "https://www.futureskillsprime.in/iDH/fsp/Dashboard/Products_detail/163111434"

# Open the URL
driver.get(url)

# Example: Find an element and print its text

# Wait for page to load
time.sleep(2)

# Login credentials
load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

try:
    # Find the username and password fields
    # Note: You'll need to inspect the login page to get the correct selectors
    # These are examples and may need to be adjusted
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userid_temp"))  # Replace with actual ID
    )
    password_field = driver.find_element(By.ID, "confData")  # Replace with actual ID
    
    # Type in the credentials
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Find and click the login button
    login_button = driver.find_element(By.XPATH, "//a[@data-b='Login']")  # Adjust selector as needed
    login_button.click()
    
    print("Login information entered successfully")
    
    # Wait for login to process
    time.sleep(3)
    
    # Now you can continue with the rest of your automation
    element = driver.find_element(By.TAG_NAME, "h1")
    print(element.text)
except Exception as e:
    print(f"An error occurred: {e}")


# Keep the browser window open until the user closes it
input("Press Enter to close the browser...")

# Close the browser
driver.quit()