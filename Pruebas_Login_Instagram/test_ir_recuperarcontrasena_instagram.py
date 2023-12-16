from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_instagram():
    d=webdriver.Chrome()
    d.get("https://www.instagram.com/accounts/login/")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_instagram1.png")
    btnRecuperar = d.find_element(By.XPATH, '//*[@id="loginForm"]/a')
    btnRecuperar.click()
    d.save_screenshot("recuperar_login_instagram2.png")    
    time.sleep(4)
    d.close()
    d.quit()