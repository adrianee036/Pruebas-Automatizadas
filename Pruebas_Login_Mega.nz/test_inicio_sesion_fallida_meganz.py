from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_meganz():
    d=webdriver.Chrome()
    d.get("https://mega.nz/login")
    d.maximize_window()
    time.sleep(6)
    d.save_screenshot("login_meganz.png")
    email = d.find_element(By.ID, "login-name2").send_keys("adrian@gmail.com")
    d.save_screenshot("login_meganz2.png")
    time.sleep(4)
    contrasena = d.find_element(By.ID, "login-password2").send_keys("Pineadklaj")
    d.save_screenshot("login_meganz3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.XPATH, '//*[@id="login_form"]/button')
    btnEnviar.click()
    time.sleep(2)
    d.save_screenshot("login_meganz4.png")
    msjError = d.find_element(By.ID, "msgDialog")
    time.sleep(4)
    d.close()
    d.quit()