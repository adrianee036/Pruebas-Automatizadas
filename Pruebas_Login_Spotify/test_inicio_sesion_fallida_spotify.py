from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_spotify():
    d=webdriver.Chrome()
    d.get("https://accounts.spotify.com/en/login")
    d.maximize_window()
    d.save_screenshot("login_spotify.png")
    email = d.find_element(By.ID, "login-username").send_keys("adrian@gmail.com")
    d.save_screenshot("login_spotify2.png")
    time.sleep(4)
    contrasena = d.find_element(By.ID, "login-password").send_keys("Pineadklaj")
    d.save_screenshot("login_spotify3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.ID, "login-button")
    btnEnviar.click()
    time.sleep(2)
    d.save_screenshot("login_spotify4.png")
    msjError = d.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/span')
    time.sleep(4)
    d.close()
    d.quit()