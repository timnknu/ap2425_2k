import unittest

from t30_2_unittest_ex import t302_matrix_process

class TestMatrixProcessingFunctin(unittest.TestCase):
    def setUp(self):
        self.M = [
            [2.0, 3.0, 15],
            [3.0, 2.0, 10]
        ]

    def test_sumel1(self):
        res = t302_matrix_process(self.M)
        # має бути: res[0] == сума елементів матриці
        self.assertAlmostEquals(res[0], 35)

    def test_min_el(self):
        res = t302_matrix_process(self.M)
        # має бути: res[1] == мінімальному елементу
        self.assertAlmostEquals(res[1], 2)

    def test_max_el(self):
        res = t302_matrix_process(self.M)
        # має бути: res[2] == максимальному елементу
        self.assertAlmostEquals(res[2], 15)

class TestMatrixProcessingFunctin_NegElems(unittest.TestCase):
    def setUp(self):
        self.M = [
            [-2.0, -3.0, -15],
            [-3.0, -2.0, -10]
        ]

    def test_sumel1(self):
        res = t302_matrix_process(self.M)
        # має бути: res[0] == сума елементів матриці
        self.assertAlmostEquals(res[0], -35)

    def test_min_el(self):
        res = t302_matrix_process(self.M)
        # має бути: res[1] == мінімальному елементу
        self.assertAlmostEquals(res[1], -15)

    def test_max_el(self):
        res = t302_matrix_process(self.M)
        # має бути: res[2] == максимальному елементу
        self.assertAlmostEquals(res[2], -2)
