import pytest
import unittest 
from . import wave

class TestWave(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(wave.make_dot_string(0),0)
        self.assertEqual(wave.make_dot_string(30),1)
        self.assertEqual(wave.make_dot_string(60),10)
        self.assertEqual(wave.make_dot_string(120),10)

    def test_division_by0(self):
        self.assertNotRaises(ZeroDivisionError, wave.make_dot_string, 90)
