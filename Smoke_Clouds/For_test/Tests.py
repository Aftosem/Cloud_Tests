import unittest
from selenium import webdriver
from Smoke_Clouds.For_test.Actions import doActions_test
from selenium.webdriver.common.keys import Keys
import time


class BOXTest(unittest.TestCase, doActions_test):
    path = "https://192.168.0." + doActions_test().getPath()

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\\drivers\\Selenium\\geckodriver-v0.23.0-win64\\geckodriver.exe')
        self.driver.implicitly_wait(10)

    def test_BOX(self):

        driver = self.driver
        #path = "https://192.168.0.70"

        #Enter
        driver.get(BOXTest.path)
        login_field = driver.find_element_by_id("username")
        login_field.send_keys("Administrator")
        password_field = driver.find_element_by_id("password")
        password_field.send_keys("password")
        driver.find_element_by_id("_submit").click()
        time.sleep(1)

        # Go to Cloud BOX
        driver.get(BOXTest.path + "/setup/discovery/box-scan")
        time.sleep(2)

        ####
        if not driver.find_element_by_id("gridcolumn-1016-textEl").is_selected():
            driver.find_element_by_id("gridcolumn-1016-textEl").click()



    def tear_down(self):
        self.driver.quit()


# if __name__ == "__main__":
#     unittest.main()