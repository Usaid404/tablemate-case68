"""TableMate service layer + repositories (for integration tests, L4.2)."""
import sqlite3
from waitlist import Party, assign_table


class SqliteRepo:
    def __init__(self, path=":memory:"):
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE party(pid TEXT PRIMARY KEY, size INT, joined INT, skips INT)")

    def save(self, p):
        self.db.execute("INSERT OR REPLACE INTO party VALUES(?,?,?,?)",
                        (p.pid, p.party_size, p.joined_at, p.skips))

    def load_all(self):
        return [Party(*r) for r in self.db.execute("SELECT pid,size,joined,skips FROM party")]

    def delete(self, pid):
        self.db.execute("DELETE FROM party WHERE pid=?", (pid,))


class StubRepo:
    """In-memory stub with canned data."""
    def __init__(self, parties=None):
        self.items = {p.pid: p for p in (parties or [])}
    def save(self, p): self.items[p.pid] = p
    def load_all(self): return list(self.items.values())
    def delete(self, pid): self.items.pop(pid, None)


class WaitlistService:
    def __init__(self, repo):
        self.repo = repo

    def join(self, pid, size, minute):
        self.repo.save(Party(pid, size, minute))

    def seat_next(self, table_size):
        parties = self.repo.load_all()
        chosen = assign_table(parties, table_size)
        for p in parties:
            self.repo.save(p)          # persist skip counters
        if chosen:
            self.repo.delete(chosen.pid)
        return chosen
