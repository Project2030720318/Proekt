import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertIsNone(main())  # Очакваме main да не връща нищо

if __name__ == "__main__":
    unittest.main()
