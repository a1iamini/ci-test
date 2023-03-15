import unittest
from greetor import greetor, second_greetor

class TestGreeting(unittest.TestCase):
	
	def test_greetor(self):
		self.assertEqual(greetor(), "how are you?")

	def test_second_greetor(self):
		self.assertEqual(second_greetor(), "hi.. how is it going?")
