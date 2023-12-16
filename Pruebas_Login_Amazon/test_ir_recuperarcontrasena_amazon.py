from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_ir_recuperarcontrasena_amazon():
    d=webdriver.Chrome()
    d.get("https://www.amazon.com/-/es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    d.maximize_window()
    time.sleep(2)
    d.save_screenshot("recuperar_login_amazon.png")
    btnAyuda = d.find_element(By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div[2]/div[1]/form/div/div/div/div[3]/div/a')
    btnAyuda.click()
    d.save_screenshot("recuperar_login_amazon1.png")
    time.sleep(1)
    btnRecuperar = d.find_element(By.ID, "auth-fpp-link-bottom")
    btnRecuperar.click()

    time.sleep(2)
    d.save_screenshot("recuperar_login_amazon3.png")
    time.sleep(4)
    d.close()
    d.quit()