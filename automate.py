from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

USERNAME = "username" #add username
PASSWORD = "password" #add password
POST_URL = "POST_URL"  #add post url
COMMENT_TEXT = ["wow","nice","cool","perfect","yoo"] #take random comment for avoid bot detection
COMMENT_COUNT = 25 

driver = webdriver.Chrome()

try:
    driver.get("https://www.instagram.com/")
    time.sleep(4)

    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(USERNAME)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN) 
    time.sleep(5)

    driver.get(POST_URL)
    time.sleep(4)

    for i in range(COMMENT_COUNT):
        try:
            comment_box = driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']")
            comment_box.click()
            time.sleep(2)

            comment_box.send_keys(randome.choice(COMMENT_TEXT))
            time.sleep(1)

            comment_box.send_keys(Keys.RETURN) #avoiding bot detection
            time.sleep(5)  

            print(f"Comment {i+1} posted!")
        except Exception as e:
            print(f"Error posting comment {i+1}: {e}")
            time.sleep(5)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()





