from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_linkedin():
    d=webdriver.Chrome()
    d.get("https://login.salesforce.com/")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_salesforce1.png")
    btnRecuperar = d.find_element(By.ID, "forgot_password_link")
    btnRecuperar.click()
    d.save_screenshot("recuperar_login_salesforce2.png")    
    time.sleep(4)
    d.close()
    d.quit()