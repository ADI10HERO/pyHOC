import numpy
from unittest import TestCase

from applied_maths import pyhoc

signal = numpy.load('tests/signal.npy')
expected_nzc = [821, 1182, 1682, 2062, 2434, 2688, 3006, 3252,
                3548, 3752, 4006, 4170, 4396, 4528, 4738, 4852,
                5048, 5158, 5336, 5434]


class TestHOC(TestCase):

    def test_sequence(self):
        global signal
        hoc = pyhoc.PyHOC()
        nzc = hoc.sequence(signal, 20)

        self.assertTrue((nzc == expected_nzc).all())
