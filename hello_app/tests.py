import pytest
import unittest 
from . import wave


class TestWave(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(wave.make_dot_string(0),0)
        self.assertEqual(wave.make_dot_string(30),1)
        self.assertEqual(wave.make_dot_string(60),9)
        self.assertEqual(wave.make_dot_string(120),9)



