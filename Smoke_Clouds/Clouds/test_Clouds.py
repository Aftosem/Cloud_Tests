import unittest
import time
import os
import shutil
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Smoke_Clouds.Clouds.Actions import Parametrs



class CloudsTest(unittest.TestCase, Parametrs):

    tCitr = tBox = tGD = tDBox = tOD = tOD4 = tAz = False
    activeCloud = "Cloud"
    presTime = str(datetime.now().strftime("_%Y-%m-%d_(%H.%M)"))
    pathP = Parametrs().getPath()
    #cycleP = Parametrs().getCycle()
    scanCloud = Parametrs().askQuntityClouds()

    def setUp(self):
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
        if CloudsTest.scanCloud == 1:
            driver.get(path + "/setup/discovery/citrix-scan")
            CloudsTest.activeCloud = "Citrix"
            CloudsTest.cloudURL = "https://gttb.sharefile.com/home/myfiles/fo179ac0-a1e9-44b1-be5a-cec87f9b1fdb"
            CloudsTest.tCitr = False
        elif CloudsTest.scanCloud == 2:
            driver.get(path + "/setup/discovery/box-scan")
            CloudsTest.activeCloud = "BOX"
            CloudsTest.cloudURL = "https://app.box.com/folder/58315420329"
            CloudsTest.tBox = False
        elif CloudsTest.scanCloud == 3:
            driver.get(path + "/setup/discovery/googledrive-scan")
            CloudsTest.activeCloud = "GoogleDrive"
            CloudsTest.cloudURL = "https://drive.google.com/drive/folders/1IOYLUcSwsFwJfva8WFLaJ0P3faCjm8ut?ogsrc=32"
            CloudsTest.tGD = False
        elif CloudsTest.scanCloud == 4:
            driver.get(path + "/setup/discovery/dropbox-scan")
            CloudsTest.activeCloud = "DropBox"
            CloudsTest.cloudURL = "https://www.dropbox.com/home/Dima/ATest"
            CloudsTest.tDBox = False
        elif CloudsTest.scanCloud == 5:
            driver.get(path + "/setup/discovery/onedrive-scan")
            CloudsTest.activeCloud = "OneDrive"
            CloudsTest.cloudURL = "https://onedrive.live.com/?id=69E878A83F70C432%211612&cid=69E878A83F70C432"
            CloudsTest.tOD = False
        elif CloudsTest.scanCloud == 6:
            driver.get(path + "/setup/discovery/one-drive-for-business-scan")
            CloudsTest.activeCloud = "OneDriveForBusiness"
            CloudsTest.cloudURL = "https://gtbtech-my.sharepoint.com/personal/qa_gtbtech_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fqa_gtbtech_onmicrosoft_com%2FDocuments%2F4Dima%2FATest"
            CloudsTest.tOD4 = False
        elif CloudsTest.scanCloud == 7:
            driver.get(path + "/setup/discovery/azure-scan")
            CloudsTest.activeCloud = "Azure"
            CloudsTest.cloudURL = "https://portal.azure.com/casualscan/"
            CloudsTest.tAz = False
        else:
            sys.exit(3)
        CloudsTest().sTime(2)

            #Set parameters
        driver.find_element_by_id("addPath-btnInnerEl").click()
        CloudsTest().sTime(2)
        driver.find_element_by_id("textfield-1025-inputEl").send_keys("ATest_", CloudsTest.activeCloud, CloudsTest.presTime)
        driver.find_element_by_id("textfield-1026-inputEl").send_keys(CloudsTest.cloudURL)
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
            for i in range(0, len(sortedFiles)-maxFiles, 1):
                shutil.rmtree(destination+sortedFiles[i], ignore_errors=True)



if __name__ == "__main__":
    unittest.main()