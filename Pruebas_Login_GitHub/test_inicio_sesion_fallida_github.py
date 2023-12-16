from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_github():
    d=webdriver.Chrome()
    d.get("https://github.com/login")
    d.maximize_window()
    d.save_screenshot("login_github.png")
    email = d.find_element(By.ID, "login_field").send_keys("adrian@gmail.com")
    d.save_screenshot("login_github2.png")
    time.sleep(2)
    contrasena = d.find_element(By.ID, "password").send_keys("123456")
    d.save_screenshot("login_github3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.NAME, "commit")
    btnEnviar.click()
    d.save_screenshot("login_github4.png")
    msjError = d.find_element(By.XPATH, '//*[@id="js-flash-container"]/div')
    time.sleep(4)
    d.close()
    d.quit()