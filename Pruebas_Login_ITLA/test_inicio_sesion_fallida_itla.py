from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_itla():
    d=webdriver.Chrome()
    d.get("https://plataformavirtual.itla.edu.do/login/index.php")
    d.maximize_window()
    d.save_screenshot("login_itla.png")
    email = d.find_element(By.ID, "username").send_keys("adrian@gmail.com")
    d.save_screenshot("login_itla2.png")
    time.sleep(4)
    contrasena = d.find_element(By.ID, "password").send_keys("Pineadklaj")
    d.save_screenshot("login_itla3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.ID, "loginbtn")
    btnEnviar.click()
    time.sleep(2)
    d.save_screenshot("login_itla4.png")
    msjError = d.find_element(By.XPATH, '//*[@id="region-main"]/div/div[2]/div/div/div/div/div[1]/div')
    time.sleep(4)
    d.close()
    d.quit()