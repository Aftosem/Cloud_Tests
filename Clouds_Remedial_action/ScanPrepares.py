from Clouds_Remedial_action import test_Clouds
import unittest


class preBegin:



    def tSuites(self):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        runner = unittest.TextTestRunner(verbosity=3)
    #Suite former
        suite.addTests(loader.loadTestsFromModule(test_Clouds))
        # if preBegin.tDBox:
        #     suite.addTests(loader.loadTestsFromModule(№№№))
        # if preBegin.tOD:
        #     suite.addTests(loader.loadTestsFromModule(№№№))
    #RUN
        runner.run(suite)



Pre = preBegin()
Pre.tSuites()






