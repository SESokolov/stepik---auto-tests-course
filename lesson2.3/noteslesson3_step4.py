from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_xpath("//*[@type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = calc(browser.find_element_by_id("input_value").text)

    browser.find_element_by_id("answer").send_keys(x)

    browser.find_element_by_xpath("//*[@type='submit']").click()
    #confirm = browser.switch_to.alert
    #confirm.accept()

    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    #welcome_text = welcome_text_elt.text

    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
