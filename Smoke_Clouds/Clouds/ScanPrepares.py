from Smoke_Clouds.Clouds.Actions import Parametrs
from Smoke_Clouds.Clouds import test_BOX
import unittest

loader = unittest.TestLoader()
suite  = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=3)




Parametrs().setPath()
Parametrs().setCycle()
suite.addTests(loader.loadTestsFromModule(test_BOX))
runner.run(suite)