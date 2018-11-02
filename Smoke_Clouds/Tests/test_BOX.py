import unittest
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class BOXTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\\drivers\\Selenium\\geckodriver-v0.23.0-win64\\geckodriver.exe')
        self.driver.implicitly_wait(10)

    def test_BOX(self):
        driver = self.driver
        path = "https://192.168.0.70"

        def actionStep():
            sTime(1)
            action = ActionChains(self.driver)
            action.send_keys(Keys.DOWN)
            action.perform()
            sTime(1)
            action.send_keys(Keys.ENTER)
            action.perform()

        def sTime(t):
            time.sleep(t)

            #Enter
        print("Start")
        driver.get(path)
        login_field = driver.find_element_by_id("username")
        login_field.send_keys("Administrator")
        password_field = driver.find_element_by_id("password")
        password_field.send_keys("password")
        driver.find_element_by_id("_submit").click()
        sTime(2)

            #Go to Cloud BOX
        driver.get(path+"/setup/discovery/box-scan")
        sTime(2)

            #Set parameters
        driver.find_element_by_id("addPath-btnInnerEl").click()
        sTime(2)
        driver.find_element_by_id("textfield-1025-inputEl").send_keys("ATest", str(datetime.now().strftime("_%Y-%m-%d_%H:%M")))
        driver.find_element_by_id("textfield-1026-inputEl").send_keys("https://app.box.com/folder/50535200360")
        #driver.find_element_by_id("boundlist-1068").find_element_by_class_name("icon-online").click()
        driver.find_element_by_id("combobox-1027-inputCell").click()
        actionStep()
        driver.find_element_by_id("combobox-1028-inputCell").click()
        actionStep()
        driver.find_element_by_id("button-1021-btnIconEl").click()

            #Schedule at now
        driver.find_element_by_id("radiofield-1055-inputEl").click()
        driver.find_element_by_id("now_button_new-btnIconEl").click()
        driver.find_element_by_id("scan_max_time-inputEl").clear()
        driver.find_element_by_id("scan_max_time-inputEl").send_keys("50")
        driver.find_element_by_id("scan_start_expiration_time-inputEl").clear()
        driver.find_element_by_id("scan_start_expiration_time-inputEl").send_keys("30")
        driver.find_element_by_id("file_scan_limit-inputEl").clear()
        driver.find_element_by_id("file_scan_limit-inputEl").send_keys("10")

            #Start scan
        driver.find_element_by_id("button-1063-btnIconEl").click()
        sTime(5)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()