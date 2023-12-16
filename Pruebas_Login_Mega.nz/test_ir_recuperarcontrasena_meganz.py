from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_meganz():
    d=webdriver.Chrome()
    d.get("https://mega.nz/login")
    d.maximize_window()
    time.sleep(10)
    d.save_screenshot("recuperar_login_meganz1.png")
    btnRecuperar = d.find_element(By.XPATH, '//*[@id="login_form"]/div[4]/a')
    btnRecuperar.click()
    time.sleep(3)
    d.save_screenshot("recuperar_login_meganz2.png")    
    time.sleep(4)
    d.close()
    d.quit()