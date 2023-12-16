from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_linkedin():
    d=webdriver.Chrome()
    d.get("https://www.linkedin.com/login?_l=es")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_linkedin1.png")
    btnRecuperar = d.find_element(By.XPATH, '//*[@id="organic-div"]/form/a')
    btnRecuperar.click()
    d.save_screenshot("recuperar_login_linkedin2.png")    
    time.sleep(4)
    d.close()
    d.quit()