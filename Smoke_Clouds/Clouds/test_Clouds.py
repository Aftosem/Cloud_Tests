import unittest
import time
import sys
import os
import shutil
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Smoke_Clouds.Clouds.Actions import Parametrs



class CloudsTest(unittest.TestCase, Parametrs):

    pathP = Parametrs().getPath()
    #cycleP = Parametrs().getCycle()
    tBox = tDBox = tOD = checkC = start = False
    activeCloud = "Cloud"
    presTime = str(datetime.now().strftime("_%Y-%m-%d_(%H.%M)"))

    def setUp(self):
        CloudsTest().askQuntityClouds()
        if CloudsTest.checkC == False:
            sys.exit()
    #Initiate WebDriver
        self.driver = webdriver.Firefox(executable_path=os.path.dirname(os.path.realpath(__file__)) + "\\geckodriver.exe")
        self.driver.implicitly_wait(10)

    def test_BOX(self):
        driver = self.driver
        path = CloudsTest.pathP

            #WEB_Enter
        driver.get(path)
        login_field = driver.find_element_by_id("username")
        login_field.send_keys("Administrator")
        password_field = driver.find_element_by_id("password")
        password_field.send_keys("password")
        driver.find_element_by_id("_submit").click()
        CloudsTest().sTime(2)

            #Go to Clouds
        if CloudsTest.tBox:
            driver.get(path + "/setup/discovery/box-scan")
            CloudsTest.activeCloud = "BOX"
            CloudsTest.tBox = False
        elif CloudsTest.tDBox:
            driver.get(path + "/setup/discovery/dropbox-scan")
            CloudsTest.activeCloud = "DropBox"
            CloudsTest.tDBox = False
        elif CloudsTest.tOD:
            driver.get(path + "/setup/discovery/onedrive-scan")
            CloudsTest.activeCloud = "OneDrive"
            CloudsTest.tOD = False
        CloudsTest().sTime(2)

            #Set parameters
        driver.find_element_by_id("addPath-btnInnerEl").click()
        CloudsTest().sTime(2)
        driver.find_element_by_id("textfield-1025-inputEl").send_keys("ATest_", CloudsTest.activeCloud, CloudsTest.presTime)
        driver.find_element_by_id("textfield-1026-inputEl").send_keys("https://app.box.com/folder/50535200360")
        #driver.find_element_by_id("boundlist-1068").find_element_by_class_name("icon-online").click()
        driver.find_element_by_id("combobox-1027-inputCell").click()
        CloudsTest().actionStep(2, driver)
        driver.find_element_by_id("combobox-1028-inputCell").click()
        CloudsTest().actionStep(2, driver)
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
        CloudsTest().sTime(5)


    def tearDown(self):
        CloudsTest().copyLogs()
        CloudsTest.sTime(self, 2)
        self.driver.quit()

##################################################_additionals functions_########################################

    def sTime(self, t):
        self.t = t
        time.sleep(self.t)

    def actionStep(self, t, dr):
        CloudsTest.sTime(self, t)
        action = ActionChains(dr)
        action.send_keys(Keys.DOWN)
        action.perform()
        CloudsTest.sTime(self, (t/2))
        action.send_keys(Keys.ENTER)
        action.perform()

    def askQuntityClouds(self):
        CloudsTest.sTime(self, 0.3)
        print("\n")
        if not CloudsTest.start:
            B = input("Scan BOX Cloud? (Type y or n) - ")
            CloudsTest.tBox = CloudsTest.comfirmChecker(B)
            CloudsTest.start = CloudsTest.tBox
        if not CloudsTest.start:
            DB = input("Scan DropBox Cloud? (Type y or n) - ")
            CloudsTest.tDBox = CloudsTest.comfirmChecker(DB)
            CloudsTest.start = CloudsTest.tDBox
        if not CloudsTest.start:
            OD = input("Scan OneDrive Cloud? (Type y or n) - ")
            CloudsTest.tOD = CloudsTest.comfirmChecker(OD)
            CloudsTest.start = CloudsTest.tOD

    def comfirmChecker(ans):
        if ans == ("y" or "у"):
            CloudsTest.checkC = True
            return True
        else:
            return False

    def copyLogs(self):
        src = "C:\\ProgramData\\GTB Technologies\\eDiscovery\\Logs"
        destination = "C:\\ProgramData\\GTB Technologies\\ATLogs\\Discovery\\"
        source = os.listdir(src)
        if not os.path.exists(destination+CloudsTest.presTime):
            os.makedirs(destination+CloudsTest.presTime)
        for files in source:
            full_file_name = os.path.join(src, files)
            if files.endswith(".log"):
                shutil.copy2(full_file_name, destination+CloudsTest.presTime)
        sortedFiles = sorted(os.listdir(destination), key=os.path.dirname)
        maxFiles = 5
        if len(sortedFiles) > maxFiles:
            for i in range(len(sortedFiles)-1, maxFiles-1, -1):
                shutil.rmtree(destination+sortedFiles[i], ignore_errors=True)



if __name__ == "__main__":
    unittest.main()