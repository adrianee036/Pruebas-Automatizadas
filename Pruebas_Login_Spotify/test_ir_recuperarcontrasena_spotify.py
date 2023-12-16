from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_spotify():
    d=webdriver.Chrome()
    d.get("https://accounts.spotify.com/en/login")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_spotify1.png")
    btnRecuperar = d.find_element(By.ID, "reset-password-link")
    btnRecuperar.click()
    d.save_screenshot("recuperar_login_spotify2.png")    
    time.sleep(4)
    d.close()
    d.quit()