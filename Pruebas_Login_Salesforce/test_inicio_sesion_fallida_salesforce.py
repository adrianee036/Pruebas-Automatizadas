from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_salesforce():
    d=webdriver.Chrome()
    d.get("https://login.salesforce.com/")
    d.maximize_window()
    d.save_screenshot("login_salesforce.png")
    email = d.find_element(By.ID, "username").send_keys("adrian@gmail.com")
    d.save_screenshot("login_salesforce2.png")
    time.sleep(4)
    contrasena = d.find_element(By.ID, "password").send_keys("Pineadklaj")
    d.save_screenshot("login_salesforce3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.ID, "Login")
    btnEnviar.click()
    d.save_screenshot("login_salesforce4.png")
    msjError = d.find_element(By.ID, "error")
    time.sleep(4)
    d.close()
    d.quit()