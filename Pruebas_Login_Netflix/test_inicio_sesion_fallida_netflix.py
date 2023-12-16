from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_netflix():
    d=webdriver.Chrome()
    d.get("https://www.netflix.com/do/login")
    d.maximize_window()
    d.save_screenshot("login_netflix.png")
    email = d.find_element(By.ID, "id_userLoginId").send_keys("adrian@gmail.com")
    d.save_screenshot("login_netflix2.png")
    time.sleep(4)
    contrasena = d.find_element(By.ID, "id_password").send_keys("Pineadklaj")
    d.save_screenshot("login_netflix3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
    btnEnviar.click()
    time.sleep(2)
    d.save_screenshot("login_netflix4.png")
    msjError = d.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div')
    time.sleep(4)
    d.close()
    d.quit()