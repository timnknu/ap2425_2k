import unittest

from t30_2_unittest_ex import t302_matrix_process

class TestMatrixProcessingFunctin(unittest.TestCase):
    def test_sumel1(self):
        M = [
            [2.0, 3.0, 15],
            [3.0, 2.0, 10]
        ]
        res = t302_matrix_process(M)
        # має бути: res[0] == сума елементів матриці
        self.assertAlmostEquals(res[0], 35)

