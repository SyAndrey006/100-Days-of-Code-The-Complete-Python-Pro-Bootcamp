from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "andrew.100daysofcode@gmail.com"
ACCOUNT_PASSWORD = 'Andrey1507'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=4233232316&f_AL=true&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER"
)

time.sleep(3)
sign_in_button = driver.find_element(by=By.CSS_SELECTOR,value="button.sign-in-modal__outlet-btn.btn-md.btn-primary.btn-secondary[data-modal='base-sign-in-modal']")
sign_in_button.click()

time.sleep(2)
email_field = driver.find_element(by=By.CSS_SELECTOR,value="input#base-sign-in-modal_session_key[autocomplete='username']")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.CSS_SELECTOR,value="input#base-sign-in-modal_session_password[autocomplete='current-password']")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

save_buttons = driver.find_elements(By.CSS_SELECTOR, "button.jobs-save-button")
print(f"Found {len(save_buttons)} Save buttons")

for button in save_buttons:
    try:
        save_button = button.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
        if "Save" in save_button.text:
            save_button.click()
            print("Clicked Save on a job")
            time.sleep(1.5)
    except:
        continue