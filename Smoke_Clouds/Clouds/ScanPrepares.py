from Smoke_Clouds.Clouds import test_BOX
import unittest


class preBegin:

    tBox = tDBox = tOD = False

    def askQuntityClouds(self):
        B = input("Scan BOX Cloud? (Type y or n) - ")
        DB = input("Scan DropBox Cloud? (Type y or n) - ")
        OD = input("Scan OneDrive Cloud? (Type y or n) - ")
        preBegin.tBox = preBegin.comfirmChecker(B)
        preBegin.tDBox = preBegin.comfirmChecker(DB)
        preBegin.tOD = preBegin.comfirmChecker(OD)

    def comfirmChecker(ans):
        if ans == ("y" or "у"):
            return True
        else:
            return False

    def tSuites(self):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        runner = unittest.TextTestRunner(verbosity=3)
    #Suite former
        if preBegin.tBox:
            suite.addTests(loader.loadTestsFromModule(test_BOX))
        # if preBegin.tDBox:
        #     suite.addTests(loader.loadTestsFromModule(№№№))
        # if preBegin.tOD:
        #     suite.addTests(loader.loadTestsFromModule(№№№))
    #RUN
        runner.run(suite)



Pre = preBegin()
Pre.askQuntityClouds()
Pre.tSuites()






