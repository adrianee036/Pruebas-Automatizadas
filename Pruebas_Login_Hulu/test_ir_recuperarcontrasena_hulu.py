from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_hulu():
    d=webdriver.Chrome()
    d.get("https://auth.hulu.com/web/login?next=https%3A%2F%2Fwww.hulu.com%2Fmy-stuff")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_hulu1.png")
    btnRecuperar = d.find_element(By.XPATH, '//*[@id="fouc-login"]/div[2]/div/div[5]/a')
    btnRecuperar.click()
    time.sleep(2)
    d.save_screenshot("recuperar_login_hulu2.png")    
    time.sleep(4)
    d.close()
    d.quit()