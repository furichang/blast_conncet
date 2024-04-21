from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")
#options.add_argument("--headless")
driver_path="chromedriver.exe"
service = Service(driver_path)

driver = webdriver.Chrome(options=options,service=service)
driver.get("https://baseball-academy-japan.blastconnect.com/login")

# pause for page to load
time.sleep(2)

# Identify the username and password input fields and enter your login credentials
email = driver.find_element(By.NAME,"email")
password = driver.find_element(By.NAME,"password")

# Replace 'your_email' and 'your_password' with your actual login details.
email.send_keys("umemura@aoyama-h.ed.jp")
password.send_keys("masa0214")

login_button = driver.find_element(By.CSS_SELECTOR,".btn-primary")
# Mimic pressing the Enter key to submit the login form
# password.send_keys(Keys.RETURN)
login_button.click()
time.sleep(10)

element_to_hover = driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div")
actions = ActionChains(driver)
actions.move_to_element(element_to_hover).click().perform()

#driver.quit()

