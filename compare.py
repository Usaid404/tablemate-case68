import time
from waitlist import Party, order_waitlist
from waitlist_ai import order_waitlist_ai
cases = {"tie on join time": [Party("B",2,5), Party("A",2,5)],
         "starved party": [Party("A",2,1), Party("Z",6,50,skips=3)],
         "plain FIFO": [Party("B",2,10), Party("A",4,5)]}
for name, c in cases.items():
    m = [p.pid for p in order_waitlist(list(c))]; a = [p.pid for p in order_waitlist_ai(list(c))]
    print(f"{name:18s} manual={m} ai={a} {'OK' if m==a else 'DIFF'}")
big = [Party(f"P{i}", 2, i % 50) for i in range(20000)]
for fn in (order_waitlist, order_waitlist_ai):
    t = time.perf_counter()
    for _ in range(20): fn(big)
    print(fn.__name__, f"{(time.perf_counter()-t)/20*1000:.2f} ms per 20000 parties")
