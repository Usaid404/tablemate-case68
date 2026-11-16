import sys, os, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from waitlist import *

P = Party
class TestWaitlist(unittest.TestCase):
    def test_TC01_fifo(self):
        q = order_waitlist([P("B", 2, 10), P("A", 4, 5), P("C", 2, 20)])
        self.assertEqual([p.pid for p in q], ["A", "B", "C"])
    def test_TC02_tie_break(self):
        q = order_waitlist([P("B", 2, 5), P("A", 2, 5)])
        self.assertEqual([p.pid for p in q], ["A", "B"])
    def test_TC03_starved_first(self):
        q = order_waitlist([P("A", 2, 1), P("Z", 6, 50, skips=3)])
        self.assertEqual(q[0].pid, "Z")
    def test_TC04_assign_fits(self):
        got = assign_table([P("A", 6, 1), P("B", 2, 2)], 4)
        self.assertEqual(got.pid, "B")
    def test_TC05_skip_counted(self):
        a = P("A", 6, 1); assign_table([a, P("B", 2, 2)], 4)
        self.assertEqual(a.skips, 1)
    def test_TC06_none_fits(self):
        self.assertIsNone(assign_table([P("A", 8, 1)], 4))
    def test_TC07_bad_table(self):
        with self.assertRaises(ValueError): assign_table([], 0)
    def test_TC08_max_bookings_18pct(self):
        self.assertEqual(max_bookings(50), 60)
    def test_TC09_bad_noshow(self):
        with self.assertRaises(ValueError): max_bookings(50, 1.0)
    def test_TC10_expected_wait(self):
        self.assertEqual(expected_wait(1), 22)
        self.assertEqual(expected_wait(3, tables=2), 67)

if __name__ == "__main__":
    unittest.main(verbosity=2)
