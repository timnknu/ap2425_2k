import unittest

from tests.test_set1 import TestMatrixProcessingFunctin

s = unittest.TestSuite()
s.addTest( unittest.TestLoader().loadTestsFromTestCase(TestMatrixProcessingFunctin) )
runner = unittest.TextTestRunner(verbosity=2)
runner.run(s)