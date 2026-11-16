"""AI (assistant) version of the ordering function, used in L1.3 / L5.4."""
def order_waitlist_ai(parties):
    return sorted(parties, key=lambda p: p.joined_at)
