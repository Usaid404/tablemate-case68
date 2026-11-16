mods=[("booking",900,14,6),("waitlist",450,11,5),("notify",300,6,2),("auth",350,3,1),("reports",600,4,1),("profile",250,2,0),("menu",400,1,0),("admin",200,2,1)]
print(f"{'module':9s}{'LOC':>5s}{'chg':>5s}{'bugs':>5s} rule_risk actual")
hit=0
for n,l,c,b in mods:
    pred="HIGH" if (c>=5 and b>=2) or b>=4 else "LOW"; act="HIGH" if b>=2 else "LOW"; hit+=pred==act
    print(f"{n:9s}{l:5d}{c:5d}{b:5d} {pred:9s} {act}")
print(f"rule matches actual on {hit}/{len(mods)} modules")
