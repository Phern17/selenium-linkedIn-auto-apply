from selenium import webdriver
import os
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe"
user_email = 'mphern17@gmail.com'
password = os.getenv('PASSWORD')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2450996123&f_AL=true&f_E=2&geoId="
           "102454443&keywords=junior%20software%20engineer&location=Singapore")

login_button = driver.find_element_by_css_selector('.nav__button-secondary')
login_button.click()

time.sleep(2)

username_input = driver.find_element_by_name('session_key')
username_input.send_keys(user_email)

password_input = driver.find_element_by_name('session_password')
password_input.send_keys(password)

confirm_button = driver.find_element_by_tag_name('button')
confirm_button.click()

time.sleep(8)

temp_list = driver.find_elements_by_css_selector('.jobs-search-results__list li')
job_list = [item for item in temp_list if item.get_attribute('id') != ""]

for job in job_list:
    job.click()
    time.sleep(1)
    try:
        apply_button = driver.find_element_by_class_name('jobs-apply-button')
    except NoSuchElementException:
        continue
    else:
        apply_button.click()
        time.sleep(1)

        phone_input = driver.find_element_by_class_name('fb-single-line-text__input')
        if phone_input.text == "":
            pass
        else:
            phone_input.send_keys('146604392')

        time.sleep(1)
        submit_button = driver.find_element_by_css_selector('footer button')

        if submit_button.get_attribute('data-control-name') == "continue_unify":
            cancel_button = driver.find_element_by_class_name('artdeco-modal__dismiss')
            cancel_button.click()
            time.sleep(1)
            confirm_button_form = driver.find_element_by_css_selector('.artdeco-modal--layer-confirmation')
            discard_button = confirm_button_form.find_element_by_css_selector('.artdeco-button--primary')
            discard_button.click()
            time.sleep(2)

        else:
            submit_button.click()
            time.sleep(2)
            exit_assessment = driver.find_element_by_class_name('artdeco-modal__dismiss')
            exit_assessment.click()
            time.sleep(1)

driver.quit()
