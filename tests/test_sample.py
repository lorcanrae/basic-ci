# pylint: disable-all

import unittest
from rad_package.helper import sum_a_and_b

class TestSample(unittest.TestCase):
    def test_sample(self):
        # We are simply checking whether 42==42!
        self.assertEqual(42, 42)

    def test_sum_a_and_b(self):
        out_ = sum_a_and_b(1, 2.)
        self.assertIsInstance(out_, (int, float))
