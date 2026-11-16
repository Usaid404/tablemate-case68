import sys, os, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from helpers import *
class T(unittest.TestCase):
    def test_msg(self): self.assertEqual(format_wait_message(3, 40), "You are #3 in line, about 40 min wait")
    def test_msg_bad(self):
        with self.assertRaises(ValueError): format_wait_message(0, 5)
    def test_mask(self): self.assertEqual(mask_phone("98765 43210"), "XXXXXX3210")
    def test_mask_short(self):
        with self.assertRaises(ValueError): mask_phone("12")
    def test_party(self):
        self.assertTrue(is_party_valid(4)); self.assertFalse(is_party_valid(0)); self.assertFalse(is_party_valid(True)); self.assertFalse(is_party_valid(13))
unittest.main(verbosity=2) if __name__ == "__main__" else None
