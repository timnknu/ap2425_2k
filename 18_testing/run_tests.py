import unittest

#from tests.test_set1 import TestMatrixProcessingFunctin, TestMatrixProcessingFunctin_NegElems
from tests.test_set1 import *

s = unittest.TestSuite()
# s.addTest( unittest.TestLoader().loadTestsFromTestCase(TestMatrixProcessingFunctin) )
# s.addTest( unittest.TestLoader().loadTestsFromTestCase(TestMatrixProcessingFunctin_NegElems) )
s.addTest( unittest.defaultTestLoader.discover('tests') )
runner = unittest.TextTestRunner(verbosity=2)
runner.run(s)