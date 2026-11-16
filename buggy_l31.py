def seat_wait_avg(waits):
    return sum(waits) / len(waits)          # BUG: empty list -> ZeroDivisionError
def seat_wait_avg_fixed(waits):
    return sum(waits) / len(waits) if waits else 0.0
