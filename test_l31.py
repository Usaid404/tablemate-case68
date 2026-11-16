from buggy_l31 import *
for f in (seat_wait_avg, seat_wait_avg_fixed):
    try: print(f.__name__, "([]) ->", f([]))
    except Exception as e: print(f.__name__, "([]) -> ERROR", type(e).__name__)
print("fixed([10,20]) ->", seat_wait_avg_fixed([10,20]))
