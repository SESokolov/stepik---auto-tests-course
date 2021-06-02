from selenium import webdriver
import time
import os 



try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    browser.find_element_by_css_selector("input[name='firstname']").send_keys("имя")
    browser.find_element_by_css_selector("input[name='lastname']").send_keys("фамилия")
    browser.find_element_by_css_selector("input[name='email']").send_keys("email")
    browser.find_element_by_css_selector("input[type='file']").send_keys(file_path)

    browser.find_element_by_xpath("//*[@type='submit']").click()
    #time.sleep(1)

    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    #welcome_text = welcome_text_elt.text

    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
