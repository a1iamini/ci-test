import unittest
from greetor import greetor

class TestGreeting(unittest.TestCase):
	
	def test_greetor(self):
		self.assertEqual(greetor(), "how are you?")

