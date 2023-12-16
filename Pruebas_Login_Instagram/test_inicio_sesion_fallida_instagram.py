from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_instagram():
    d=webdriver.Chrome()
    d.get("https://www.instagram.com/accounts/login/")
    d.maximize_window()
    time.sleep(4)
    d.save_screenshot("login_instagram.png")
    email = d.find_element(By.NAME, "username").send_keys("adrian@gmail.com")
    d.save_screenshot("login_instagram2.png")
    time.sleep(4)
    contrasena = d.find_element(By.NAME, "password").send_keys("Pineadklaj")
    d.save_screenshot("login_instagram3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    btnEnviar.click()
    time.sleep(2)
    d.save_screenshot("login_instagram4.png")
    msjError = d.find_element(By.XPATH, '//*[@id="loginForm"]/span/div')
    time.sleep(4)
    d.close()
    d.quit()