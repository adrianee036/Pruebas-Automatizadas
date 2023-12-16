from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_hulu():
    d=webdriver.Chrome()
    d.get("https://auth.hulu.com/web/login?next=https%3A%2F%2Fwww.hulu.com%2Fmy-stuff")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("login_hulu.png")
    email = d.find_element(By.XPATH, '//*[@id="fouc-login"]/div[2]/div/div[3]/label/div[2]/input').send_keys("adrianee036@gmail.com")
    d.save_screenshot("login_hulu2.png")
    time.sleep(4)
    contrasena = d.find_element(By.XPATH, '//*[@id="fouc-login"]/div[2]/div/div[4]/label/div[2]/input').send_keys("Pineadklaj")
    d.save_screenshot("login_hulu3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.XPATH, '//*[@id="fouc-login"]/div[2]/div/button')
    btnEnviar.click()
    time.sleep(2)
    d.save_screenshot("login_hulu4.png")
    msjError = d.find_element(By.ID, "password_error_message")
    time.sleep(4)
    d.close()
    d.quit()