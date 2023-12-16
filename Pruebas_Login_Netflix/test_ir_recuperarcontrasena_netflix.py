from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_netflix():
    d=webdriver.Chrome()
    d.get("https://www.netflix.com/do/login")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_netflix1.png")
    btnRecuperar = d.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/div[3]/a')
    btnRecuperar.click()
    time.sleep(2)
    d.save_screenshot("recuperar_login_netflix2.png")    
    time.sleep(4)
    d.close()
    d.quit()