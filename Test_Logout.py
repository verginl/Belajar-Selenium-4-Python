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
         
         BtnMakeAppointment = self.driver.find_element(by=By.ID, value='btn-make-appointment')
         BtnMakeAppointment.click()
         TxtUsername = self.driver.find_element(by=By.ID, value='txt-username')
         TxtUsername.send_keys("John Doe")
       
         TxtPassword = self.driver.find_element(by=By.ID, value='txt-password')
         TxtPassword.send_keys('ThisIsNotAPassword')
       
         BtnLogin = self.driver.find_element(by=By.ID, value='btn-login')
         BtnLogin.click()
         time.sleep(1)    

    def test_logout(self):
        driver = self.driver
        btnMenu = self.driver.find_element(by=By.XPATH, value="//*[@id='menu-toggle']")
        btnMenu.click()
        
        menuLogout = self.driver.find_element(by=By.XPATH, value="//*[@id='sidebar-wrapper']/ul/li[5]/a")
        menuLogout.click()
        time.sleep(2)  

        btnMenu2 = self.driver.find_element(by=By.XPATH,value="//*[@id='menu-toggle']")
        btnMenu2.click()
        actualRslt = "Login"
        response_message = driver.find_element(By.XPATH,"//*[@id='sidebar-wrapper']/ul/li[3]/a").text
        self.assertEqual(response_message, actualRslt)
unittest.main()


