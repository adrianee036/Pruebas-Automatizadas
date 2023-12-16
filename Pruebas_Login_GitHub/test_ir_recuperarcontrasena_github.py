from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_github():
    d=webdriver.Chrome()
    d.get("https://github.com/login")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_github1.png")
    btnRecuperar = d.find_element(By.ID, "forgot-password")
    btnRecuperar.click()
    d.save_screenshot("recuperar_login_github2.png")    
    time.sleep(4)
    d.close()
    d.quit()