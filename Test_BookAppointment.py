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

    def test_bookappointment(self):
        
        driver = self.driver
        CmbFacility = Select(driver.find_element(by=By.ID, value='combo_facility'))
        CmbFacility.select_by_value('Hongkong CURA Healthcare Center')
        

        Chckbox = driver.find_element(by=By.ID, value='chk_hospotal_readmission')
        Chckbox.click()
        time.sleep(5)

        Option = driver.find_element(by=By.XPATH, value='//*[@id="appointment"]/div/div/form/div[3]/div/label[2]')
        Option.click()
        time.sleep(4)

        DateTime = driver.find_element(by=By.ID, value='txt_visit_date')
        DateTime.click()
        time.sleep(3)

        PickDate = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/table/tbody/tr[3]/td[5]')
        PickDate.click()
        time.sleep(2)
        Comment = driver.find_element(by=By.ID, value='txt_comment')
        Comment.send_keys("Testing ini adalah tessting aja.")

        time.sleep(1)
        BtnBook = driver.find_element(by=By.ID, value='btn-book-appointment')
        BtnBook.click()


# test1 = Basic()
# test1.setUp()
# test1.test_login()


test2 = Basic()
test2.setUp()
test2.test_login()
test2.test_bookappointment()


