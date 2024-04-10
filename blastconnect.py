from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Assume you're using Chrome; adjust as needed for Firefox, Safari, etc.
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://baseball-academy-japan.blastconnect.com/login")

# pause for page to load
time.sleep(2)

# Identify the username and password input fields and enter your login credentials
username = driver.find_element_by_id("mat-input-0")
password = driver.find_element_by_id("mat-input-1")

# Replace 'your_username' and 'your_password' with your actual login details.
username.send_keys("your_username")
password.send_keys("your_password")

# Mimic pressing the Enter key to submit the login form
password.send_keys(Keys.RETURN)