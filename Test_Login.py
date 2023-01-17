import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Basic(unittest.TestCase):
    def setUp(self):
         options = webdriver.ChromeOptions()
         options.add_experimental_option('excludeSwitches', ['enable-logging'])
         self.driver = webdriver.Chrome(options=options)
         self.driver.maximize_window()
         self.driver.get('https://katalon-demo-cura.herokuapp.com/') #Buka Situs       

    def test_login_success(self):
        driver = self.driver       
        BtnMakeAppointment = self.driver.find_element(by=By.ID, value='btn-make-appointment')
        BtnMakeAppointment.click()
        TxtUsername = driver.find_element(by=By.ID, value='txt-username')
        TxtUsername.send_keys("John Doe")
       
        TxtPassword = driver.find_element(by=By.ID, value='txt-password')
        TxtPassword.send_keys('ThisIsNotAPassword')
       
        BtnLogin = driver.find_element(by=By.ID, value='btn-login')
        BtnLogin.click()
        time.sleep(1)

        actualRslt = "Make Appointment"
        response_message = driver.find_element(By.XPATH,"//*[@id='appointment']/div/div/div/h2").text
        self.assertEqual(response_message, actualRslt)

    def test_login_fail(self):
        driver = self.driver       
        BtnMakeAppointment = self.driver.find_element(by=By.ID, value='btn-make-appointment')
        BtnMakeAppointment.click()
        TxtUsername = driver.find_element(by=By.ID, value='txt-username')
        TxtUsername.send_keys("usernamesalah")
       
        TxtPassword = driver.find_element(by=By.ID, value='txt-password')
        TxtPassword.send_keys('passwordsalah')
       
        BtnLogin = driver.find_element(by=By.ID, value='btn-login')
        BtnLogin.click()
        time.sleep(1)

        actualRslt = driver.find_element(By.XPATH,"//*[@id='login']/div/div/div[1]/p[2]").text
        expectRslt = "Login failed! Please ensure the username and password are valid."
        self.assertEqual(actualRslt,expectRslt)

unittest.main()



