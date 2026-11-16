import ast, sys, builtins
src = open(sys.argv[1]).read(); tree = ast.parse(src)
for fn in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
    for d in fn.args.defaults:
        if isinstance(d, (ast.List, ast.Dict, ast.Set)):
            print(f"{sys.argv[1]}:{d.lineno}: W0102 mutable default argument in {fn.name}()")
    assigned = {a.arg for a in fn.args.args}
    loads = set()
    for n in ast.walk(fn):
        if isinstance(n, ast.Name):
            (assigned if isinstance(n.ctx, ast.Store) else loads).add(n.id) if True else None
            if isinstance(n.ctx, ast.Load) and n.id not in assigned and not hasattr(builtins, n.id):
                print(f"{sys.argv[1]}:{n.lineno}: E0602 undefined name '{n.id}' in {fn.name}()")
    for v in sorted(assigned - loads - {a.arg for a in fn.args.args}):
        print(f"{sys.argv[1]}: W0612 unused variable '{v}' in {fn.name}()")
