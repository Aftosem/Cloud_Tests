import sys
import time

class Parametrs:

    def getPath(self):
        print("Set cloud auto-test parameters:\n")
        pathP = input("Enter CC ip https://192.168.0.")
        pathP = "https://192.168.0." + pathP
        return pathP

    def getCycle(self):
        cycleP = input("Enter how many times repeat = ")
        return cycleP

    def askCallsCloud(self):
        time.sleep(0.3)
        print("\n")
        print("Choose what cloud do you want to scan:\n\t1 Citrix\n\t2 Box\n\t3 GoogleDrive\n\t4 DropBox\n\t5 OneDrive\n\t6 OneDrive for Business\n\t7 Azure\n")
        answer = input("Choose 1-7: ")
        ansP = Parametrs.comfirmChecker(int(answer), 1, 7)
        return ansP
        # if not CloudsTest.start:
        #     B = input("Scan BOX Cloud? (Type y or n) - ")
        #     CloudsTest.tBox = CloudsTest.comfirmChecker(B)
        #     CloudsTest.start = CloudsTest.tBox
        # if not CloudsTest.start:
        #     DB = input("Scan DropBox Cloud? (Type y or n) - ")
        #     CloudsTest.tDBox = CloudsTest.comfirmChecker(DB)
        #     CloudsTest.start = CloudsTest.tDBox
        # if not CloudsTest.start:
        #     OD = input("Scan OneDrive Cloud? (Type y or n) - ")
        #     CloudsTest.tOD = CloudsTest.comfirmChecker(OD)
        #     CloudsTest.start = CloudsTest.tOD
    def additionalfeatures(self):
        print("Choose additional parameters:\n\t1 Incremental Scan\n\t2 File size limits\n\t3 Files changed")
        answer = input("Choose 1-3: ")
        ansAdd = Parametrs.comfirmChecker(int(answer), 1, 3)
        return ansAdd

    def comfirmChecker(ans, min, max):
        if ans<min:
            print("Wrong choice. Choose from 1 to 7. You choose ", ans)
            sys.exit(2)
        elif ans>max:
            print("Wrong choice. Choose from 1 to 7. You choose ", ans)
            sys.exit(2)
        else:
            return ans
