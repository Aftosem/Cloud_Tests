import unittest
import time
import sys
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Smoke_Clouds.Clouds.Actions import Parametrs



class BOXTest(unittest.TestCase, Parametrs):

    pathP = Parametrs().getPath()
    cycleP = Parametrs().getCycle()
    tBox = tDBox = tOD = checkC = start = False
    activeCloud = "Cloud"

    def setUp(self):
        BOXTest().askQuntityClouds()
        if BOXTest.checkC == False:
            sys.exit()
    #Initiate WebDriver
        self.driver = webdriver.Firefox(executable_path=os.path.dirname(os.path.realpath(__file__)) + "\\geckodriver.exe")
        self.driver.implicitly_wait(10)

    def test_BOX(self):
        driver = self.driver
        path = BOXTest.pathP

            #WEB_Enter
        driver.get(path)
        login_field = driver.find_element_by_id("username")
        login_field.send_keys("Administrator")
        password_field = driver.find_element_by_id("password")
        password_field.send_keys("password")
        driver.find_element_by_id("_submit").click()
        BOXTest().sTime(2)

            #Go to Cloud BOX
        if BOXTest.tBox:
            driver.get(path + "/setup/discovery/box-scan")
            BOXTest.activeCloud = "BOX"
            BOXTest.tBox = False
        elif BOXTest.tDBox:
            driver.get(path + "/setup/discovery/dropbox-scan")
            BOXTest.activeCloud = "DropBox"
            BOXTest.tDBox = False
        elif BOXTest.tOD:
            driver.get(path + "/setup/discovery/onedrive-scan")
            BOXTest.activeCloud = "OneDrive"
            BOXTest.tOD = False
        BOXTest().sTime(2)

            #Set parameters
        driver.find_element_by_id("addPath-btnInnerEl").click()
        BOXTest().sTime(2)
        driver.find_element_by_id("textfield-1025-inputEl").send_keys("ATest_", BOXTest.activeCloud, str(datetime.now().strftime("_%Y-%m-%d_%H:%M")))
        driver.find_element_by_id("textfield-1026-inputEl").send_keys("https://app.box.com/folder/50535200360")
        #driver.find_element_by_id("boundlist-1068").find_element_by_class_name("icon-online").click()
        driver.find_element_by_id("combobox-1027-inputCell").click()
        BOXTest().actionStep(2, driver)
        driver.find_element_by_id("combobox-1028-inputCell").click()
        BOXTest().actionStep(2, driver)
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
        BOXTest().sTime(5)


    def tearDown(self):
        self.driver.quit()

##################################################_additionals functions_########################################

    def sTime(self, t):
        self.t = t
        time.sleep(self.t)

    def actionStep(self, t, dr):
        BOXTest.sTime(self, t)
        action = ActionChains(dr)
        action.send_keys(Keys.DOWN)
        action.perform()
        BOXTest.sTime(self, t)
        action.send_keys(Keys.ENTER)
        action.perform()

    def askQuntityClouds(self):
        BOXTest.sTime(self, 0.2)
        if not BOXTest.start:
            B = input("Scan BOX Cloud? (Type y or n) - ")
            BOXTest.tBox = BOXTest.comfirmChecker(B)
            BOXTest.start = BOXTest.tBox
        if not BOXTest.start:
            DB = input("Scan DropBox Cloud? (Type y or n) - ")
            BOXTest.tDBox = BOXTest.comfirmChecker(DB)
            BOXTest.start = BOXTest.tDBox
        if not BOXTest.start:
            OD = input("Scan OneDrive Cloud? (Type y or n) - ")
            BOXTest.tOD = BOXTest.comfirmChecker(OD)
            BOXTest.start = BOXTest.tOD

    def comfirmChecker(ans):
        if ans == ("y" or "у"):
            BOXTest.checkC = True
            return True
        else:
            return False



if __name__ == "__main__":
    unittest.main()