from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_linkedin():
    d=webdriver.Chrome()
    d.get("https://www.linkedin.com/login?_l=es")
    d.maximize_window()
    d.save_screenshot("login_linkedin.png")
    email = d.find_element(By.ID, "username").send_keys("adrianee036@gmail.com")
    d.save_screenshot("login_linkedin2.png")
    time.sleep(4)
    contrasena = d.find_element(By.ID, "password").send_keys("Pineadklaj")
    d.save_screenshot("login_linkedin3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    btnEnviar.click()
    d.save_screenshot("login_linkedin4.png")
    msjError = d.find_element(By.ID, "error-for-password")
    time.sleep(4)
    d.close()
    d.quit()