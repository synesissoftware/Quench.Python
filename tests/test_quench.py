import unittest

import pyquench as quench


class Test_quench(unittest.TestCase):

    def test_version(self):

        self.assertEqual('0.0.0', quench.__version__)
