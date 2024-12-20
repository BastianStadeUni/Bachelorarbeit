import random
import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    NoAlertPresentException
)



def scroll_full_website():
    #Scroll to the bottom and to the top of the website
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)


def click_random_buttons(number_of_buttons):
    for _ in range(number_of_buttons):
        buttons = driver.find_elements(By.XPATH, "//button")
        if not buttons:
            print("No buttons on this website...")
            return
        clickable_buttons = [
            button for button in buttons if button.is_displayed() and button.is_enabled()
        ]
        if not clickable_buttons:
            print("No clickable buttons on this website...")
            return
        try:
            button = random.choice(clickable_buttons)
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)
            print(f"clicking button with text: {button.text}")
            driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
        except (ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException) as e:
            print(f"Could not click button: {e}")


def click_random_links(number_of_links):
    for _ in range(number_of_links):
        links = driver.find_elements(By.XPATH, "//a")
        if not links:
            print("No links on this Website...")
            return 
        clickable_links = [
            link for link in links if link.is_displayed() and link.is_enabled()
        ]
        if not clickable_links:
                print("No clickable links on this Website...")
                return 
        try:
            link = random.choice(clickable_links)
            link_href = link.get_attribute("href")
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            time.sleep(1)
            print(f"clicking link with text: {link.text} and URL: {link.get_attribute("href")}")
            driver.execute_script("arguments[0].click();", link)
            time.sleep(1)
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException) as e:
            print(f"Could not click link: {e}")

def click_random_image(number_of_images):
    for _ in range(number_of_images):
        images = driver.find_elements(By.XPATH, "//img")
        if not images:
            print("No images found...")
            return
        clickable_images = [ 
            image for image in images if image.is_displayed() and image.is_enabled()
        ]
        if not clickable_images:
            print("No clickable images found...")
            return
        try:
            image = random.choice(clickable_images)
            driver.execute_script("arguments[0].scrollIntoView(true);", image)
            time.sleep(1)
            print(f"Clicking on Image with text: {image.text}")
            driver.execute_script("arguments[0].click();", image)
            time.sleep(1)
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException) as e:
            print(f"Could not click on picture: {e}")


def interact_with_email_form():
    handle_popups()
    #Set dummy data
    dummy_pw = "password123"
    dummy_email = "dummy@email.com"
    #find email and password fields
    email_fields = driver.find_elements(By.XPATH, "//input[@type='email'] | //input[@id='email']")
    password_fields = driver.find_elements(By.XPATH, "//input[@type='password'] | //input[@id='password']")
    submit_buttons = driver.find_elements(By.XPATH, "//button[@type='submit'] | //button[@id='submit'] | //button[@type='login'] | //button[@id='login'] | //button[@type='register'] | //button[@id='register']")
    try:
        #Enter Email into email form
        if email_fields:
            email_field = email_fields[0]
            if email_field.is_displayed() and email_field.is_enabled():
                email_field.send_keys(dummy_email)
                print("Entered Email")
                time.sleep(1)
        else:
            print("No email-field found")
        #Enter password into password form
        if password_fields:
            password_field = password_fields[0]
            if password_field.is_displayed() and password_field.is_enabled():
                password_field.send_keys(dummy_pw)
                print("Entered Password")
                time.sleep(1)
        else:
            print("No password-field found")
        #Press submit button
        if submit_buttons and submit_buttons[0].is_displayed() and submit_buttons[0].is_enabled():
            submit_button = submit_buttons[0]
            print("Clicking Submit-button")
            driver.execute_script("arguments[0].click();", submit_button)
        else:
            #if no submit button present, press enter in email field
            if email_fields:
                email_field.send_keys(Keys.ENTER)
                print("Pressed enter on Email-field")
                time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

def handle_popups():
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print(f"Accepted alert with text: {alert.text}")
    except NoAlertPresentException:
        print("No alert...")

def return_to_base_URL():
    print("Returning to base URL")
    driver.get(base_URL)
    driver.switch_to.window(base_tab)
    time.sleep(2)

#main start
if __name__ == "__main__":
    options = Options()
    #service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(options=options)
    #base_URL = "https://www.webscraper.io"
    base_URL = "https://www.animetoast.cc/"
    driver.get(base_URL)
    base_tab = driver.current_window_handle
    time.sleep(2)

    interact_with_email_form()
    for _ in range(3):
        for x in range(10):
            r_num = random.randint(1, 100)
            handle_popups()
            if r_num < 50:
                click_random_links(1)
            elif r_num < 75:
                click_random_buttons(1)
            else:
                click_random_image(1)
            time.sleep(1)
        return_to_base_URL()
        
    driver.quit()
