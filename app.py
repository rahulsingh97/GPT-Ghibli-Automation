import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
import os
import winsound

print("Clearing console...")
os.system('cls' if os.name == 'nt' else 'clear')

prompt = "Create Ghibli style for this image"

print("Setting up Chrome options...")
op = webdriver.ChromeOptions()
op.add_argument(f"user-agent={UserAgent.random}")
op.add_argument("user-data-dir=./")
# Set smaller window size (width x height)
op.add_argument("window-size=720,400")
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])

print("Launching browser...")
driver = uc.Chrome(chrome_options=op)

MAIL = "rs846239@gmail.com"
PASSWORD = "fromaitogpt69?"
PATH = "path you your chrome driver"  # Not used in this code

print("Navigating to ChatGPT login page...")
driver.get('https://chat.openai.com/auth/login')
print("Page title:", driver.title)
sleep(3)

print("Finding the first button element to click...")
inputElements = driver.find_elements(By.TAG_NAME, "button")[0]
print("Button text:", inputElements.text)
inputElements.click()

sleep(6)

# Debug: Uncomment to print all input fields and buttons if needed
# inputElements = driver.find_elements(By.TAG_NAME, "input")
# for i in range(len(inputElements)):
#     print("Input Field:", i, inputElements[i].get_attribute("outerHTML"))
# buttons = driver.find_elements(By.TAG_NAME, "button")
# for i in range(len(buttons)):
#     print("Button:", i, buttons[i].get_attribute("outerHTML"))

print("Entering email...")
mail = driver.find_elements(By.TAG_NAME, "input")[0]
print("Email field text:", mail.text)
mail.send_keys(MAIL)

print("Clicking the email submit button...")
btn = driver.find_elements(By.TAG_NAME, "input")[1]
print("Email button text:", btn.text)
btn.click()

print("Captcha might be required.")
print("Please solve the captcha and press Enter to continue...")
winsound.Beep(1000, 500)
input("Press Enter to continue...")

sleep(8)

print("Entering password...")
password = driver.find_elements(By.TAG_NAME, "input")[4]
print("Password field text:", password.text)
password.send_keys(PASSWORD)

sleep(3)

print("Waiting for the login button to be clickable...")
wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_button-login-password")))
print("Login button text:", btn.text)
btn.click()

sleep(10)

# -------------------------
# File Upload and Send Message
# -------------------------
print("Locating file input element for file upload...")
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_path = r"C:\Users\Hotel Dasharath\Desktop\Coding\Python\GPT ghibli Automation\photos\Engagement_779.JPG"
print("Uploading file:", file_path)
file_input.send_keys(file_path)
sleep(10)
print("File uploaded.")

inputprompt = driver.find_elements(By.XPATH, '//*[@id="prompt-textarea"]/p')
inputprompt[0].send_keys(prompt)

sleep(10)

send_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div[3]/div[1]/div/div/div[2]/form/div[1]/div/div[2]/div/div[2]/div/button')
print("Send button text:", send_button.text)
send_button.click()


print("Prompt sent.")
