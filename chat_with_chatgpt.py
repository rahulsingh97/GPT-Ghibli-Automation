# app.py 
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

#clear the console
os.system('cls' if os.name == 'nt' else 'clear')

prompt =  "hello, how are you?"
# print(prompt)

op = webdriver.ChromeOptions()
op.add_argument(f"user-agent={UserAgent.random}")
op.add_argument("user-data-dir=./")
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = uc.Chrome(chrome_options=op)

MAIL = "rs846239@gmail.com"
PASSWORD = "fromaitogpt69?"
PATH = "path you your chrome driver"

driver.get('https://chat.openai.com/auth/login')
print (driver.title)
sleep(3)

inputElements = driver.find_elements(By.TAG_NAME, "button")[0]
print (inputElements.text)
inputElements.click()

sleep(6)

##print all the input fields and all the buttons found

# inputElements = driver.find_elements(By.TAG_NAME, "input")
# for i in range(len(inputElements)):
#     print("Input Field: ", i, inputElements[i].get_attribute("outerHTML"))

# bottons = driver.find_elements(By.TAG_NAME, "button")
# for i in range(len(bottons)):
#     print("Button: ", i, bottons[i].get_attribute("outerHTML"))

mail = driver.find_elements(By.TAG_NAME,"input")[0]
print(mail.text)
mail.send_keys(MAIL)

btn=driver.find_elements(By.TAG_NAME,"input")[1]
print(btn.text)
btn.click()

print("Captcha might be required")
print("Please solve the captcha and press Enter to continue...")
winsound.Beep(1000, 500)
input("Press Enter to continue...")

sleep(8)

password= driver.find_elements(By.TAG_NAME,"input")[4]
print(password.text)
password.send_keys(PASSWORD)

sleep(3)

wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_button-login-password")))
print(btn.text)
btn.click()

sleep(10)

btn = driver.find_elements(By.TAG_NAME,"button")[24]
print(btn.text)
btn.click()

sleep(3)

btn = driver.find_element(By.XPATH, '//*[@id="radix-:R1kmcpjq8pcfaaekklj5H1:"]/div/div[4]')
print(btn.text)
btn.click()

input("Press Enter to continue...")



# inputElements = driver.find_elements(By.TAG_NAME, "textarea")

# i = 0
# # while i<10:
# inputElements[0].send_keys(prompt)
# sleep(2)
# inputElements[0].send_keys(Keys.ENTER)
# sleep(10)
# inputElements = driver.find_elements(By.TAG_NAME, "p")
# sleep(5)
# results = []
# for element in inputElements:
#    results.append(element.text)
# print(results)
# i+=1
# sleep(5)