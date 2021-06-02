from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    browser.find_element_by_id("book").click()

    x = calc(browser.find_element_by_id("input_value").text)

    browser.find_element_by_id("answer").send_keys(x)

    browser.find_element_by_xpath("//*[@type='submit']").click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(10)
    browser.quit()
