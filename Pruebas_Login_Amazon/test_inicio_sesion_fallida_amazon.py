from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_inicio_sesion_fallida_amazon():
    d=webdriver.Chrome()
    d.get("https://www.amazon.com/-/es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    d.maximize_window()
    d.save_screenshot("login_amazon.png")
    email = d.find_element(By.ID, "ap_email").send_keys("adrian@gmail.com")
    d.save_screenshot("login_amazon2.png")
    time.sleep(2)
    btnContinuar = d.find_element(By.ID, "continue")
    btnContinuar.click()
    time.sleep(4)
    contrasena = d.find_element(By.ID, "ap_password").send_keys("123456")
    d.save_screenshot("login_amazon3.png")
    time.sleep(4)
    btnEnviar = d.find_element(By.ID, "signInSubmit")
    btnEnviar.click()
    d.save_screenshot("login_amazon4.png")
    try:
       d.find_element(By.ID, "auth-error-message-box")
    except:
        d.find_element(By.XPATH, '//*[@id="cvf-page-content"]/div/div/div/form/div[2]/input')
    time.sleep(4)
    d.close()
    d.quit()