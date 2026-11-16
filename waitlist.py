"""TableMate - waitlist ordering module (prototype).  FR-03, FR-04, FR-05"""
from dataclasses import dataclass

MAX_SKIPS = 3          # a party skipped 3 times gets top priority (fairness)
NOSHOW_RATE = 0.18     # case target: 18% no-shows


@dataclass
class Party:
    pid: str
    party_size: int
    joined_at: int      # minutes since opening
    skips: int = 0


def order_waitlist(parties):
    """FR-03: FIFO by join time, tie -> pid; starved parties first."""
    return sorted(parties, key=lambda p: (p.skips < MAX_SKIPS, p.joined_at, p.pid))


def assign_table(parties, table_size):
    """FR-04: give a free table to the first party it fits; count skips."""
    if table_size < 1:
        raise ValueError("table_size must be >= 1")
    queue = order_waitlist(parties)
    for i, p in enumerate(queue):
        if p.party_size <= table_size:
            for earlier in queue[:i]:
                earlier.skips += 1
            return p
    return None


def max_bookings(capacity, noshow=NOSHOW_RATE):
    """FR-05: bookings to accept so expected show-ups ~ capacity."""
    if not 0 <= noshow < 1:
        raise ValueError("noshow must be in [0,1)")
    return int(capacity / (1 - noshow))


def expected_wait(position, avg_turn_min=45, tables=1):
    """FR-03: estimated wait in minutes for a 1-based queue position."""
    if position < 1 or tables < 1:
        raise ValueError("position and tables must be >= 1")
    return (position - 1) // tables * avg_turn_min + avg_turn_min // 2
