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

    def test_bookappointment(self):
        driver = self.driver
        CmbFacility = Select(driver.find_element(by=By.ID, value='combo_facility'))
        CmbFacility.select_by_value('Hongkong CURA Healthcare Center')

        Chckbox = driver.find_element(by=By.ID, value='chk_hospotal_readmission')
        Chckbox.click()

        Option = driver.find_element(by=By.XPATH, value='//*[@id="appointment"]/div/div/form/div[3]/div/label[2]')
        Option.click()

        DateTime = driver.find_element(by=By.ID, value='txt_visit_date')
        DateTime.click()

        PickDate = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/table/tbody/tr[3]/td[5]')
        PickDate.click()
        
        Comment = driver.find_element(by=By.ID, value='txt_comment')
        Comment.send_keys("Testing ini adalah tessting aja.")

        BtnBook = driver.find_element(by=By.ID, value='btn-book-appointment')
        BtnBook.click()
        time.sleep(1)

        actualRslt = "Appointment Confirmation"
        response_message = driver.find_element(By.XPATH,"//*[@id='summary']/div/div/div[1]/h2").text
        self.assertEqual(response_message, actualRslt)
        
unittest.main()


