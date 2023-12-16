from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_itla():
    d=webdriver.Chrome()
    d.get("https://plataformavirtual.itla.edu.do/login/index.php")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_itla1.png")
    btnRecuperar = d.find_element(By.XPATH, '//*[@id="region-main"]/div/div[2]/div/div/div/div/div/div[2]/div[1]/p/a')
    btnRecuperar.click()
    time.sleep(2)
    d.save_screenshot("recuperar_login_itla2.png")    
    time.sleep(4)
    d.close()
    d.quit()