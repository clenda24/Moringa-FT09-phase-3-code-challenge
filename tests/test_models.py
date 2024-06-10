# tests/test_models.py

import unittest
from your_module import Magazine  # Adjust the import according to your project structure

class TestModels(unittest.TestCase):
    def test_magazine_creation(self):
        # Add the missing 'category' argument
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.title, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

if __name__ == "_main_":
    unittest.main()