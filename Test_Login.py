import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class Basic(unittest.TestCase):
    def setUp(self):
         self.driver = webdriver.Chrome(ChromeDriverManager().install())
         self.driver.maximize_window()       

    def test_login(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/') #Buka Situs
        BtnMakeAppointment = self.driver.find_element(by=By.ID, value='btn-make-appointment')
        BtnMakeAppointment.click()
        time.sleep(4)    
        TxtUsername = driver.find_element(by=By.ID, value='txt-username')
        TxtUsername.send_keys("John Doe")
        time.sleep(3) 
        TxtPassword = driver.find_element(by=By.ID, value='txt-password')
        TxtPassword.send_keys('ThisIsNotAPassword')
        time.sleep(2)
        BtnLogin = driver.find_element(by=By.ID, value='btn-login')
        BtnLogin.click()
        time.sleep(1)

# test1 = Basic()
# test1.setUp()
# test1.test_login()



