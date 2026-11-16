import random
random.seed(7)
def sim(cap):
    queue=[]; waits={"small(1-2)":[], "medium(3-4)":[], "large(5-6)":[]}
    grp=lambda s:"small(1-2)" if s<=2 else "medium(3-4)" if s<=4 else "large(5-6)"
    for minute in range(3000):
        if random.random()<0.9:
            queue.append({"size":random.choice([1,2,2,2,3,4,4,5,6]),"t":minute,"skips":0})
        if queue:
            table=random.choice([2,2,4,4,6])
            order=sorted(queue,key=lambda p:(p["skips"]<cap,p["t"]))
            for i,p in enumerate(order):
                if p["size"]<=table:
                    for e in order[:i]: e["skips"]+=1
                    waits[grp(p["size"])].append(minute-p["t"]); queue.remove(p); break
    return {k:(sum(v)/len(v) if v else 0) for k,v in waits.items()}
print("Average wait (min) by party size group, 3000-minute simulation")
for name,cap in (("fit-first, no skip cap",10**9),("with skip cap (MAX_SKIPS=3)",3)):
    r=sim(cap); print(f"{name:30s}", "  ".join(f"{k}={v:5.1f}" for k,v in r.items()))
