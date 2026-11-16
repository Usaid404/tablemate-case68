import sys, os, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from service import *
from waitlist import Party

class TestIntegration(unittest.TestCase):
    def test_TC11_service_with_stub(self):
        svc = WaitlistService(StubRepo([Party("A", 6, 1), Party("B", 2, 2)]))
        self.assertEqual(svc.seat_next(4).pid, "B")
        self.assertEqual(svc.repo.items["A"].skips, 1)   # skip persisted
    def test_TC12_service_with_sqlite(self):
        svc = WaitlistService(SqliteRepo())
        svc.join("A", 4, 1); svc.join("B", 2, 2)
        self.assertEqual(svc.seat_next(4).pid, "A")
        self.assertEqual([p.pid for p in svc.repo.load_all()], ["B"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
