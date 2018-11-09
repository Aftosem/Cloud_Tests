
class Parametrs:

    def getPath(self):
        print("Set cloud auto-test parameters:\n")
        pathP = input("Enter CC ip https://192.168.0.")
        pathP = "https://192.168.0." + pathP
        return pathP

    def getCycle(self):
        cycleP = input("Enter how many times repeat = ")
        return cycleP


# class DoActions:
#
#     def sTime(self, t):
#         time.sleep(t)
#
#     def actionStep(self, driver):
#         DoActions().sTime(2)
#         action = ActionChains(driver)
#         action.send_keys(Keys.DOWN)
#         action.perform()
#         DoActions().sTime(2)
#         action.send_keys(Keys.ENTER)
#         action.perform()
