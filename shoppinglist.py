#!/usr/bin/env python3

from collections import defaultdict
import importlib.util
import os.path
import sys

from brew.common import lfill, rfill


malt = defaultdict(float)
hops = defaultdict(int)
yeast = defaultdict(int)

for arg in sys.argv[1:]:
    name, ext = os.path.splitext(arg)
    spec = importlib.util.spec_from_file_location(name, arg)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cls = mod.Recipe()

    for f in cls.fermentables:
        malt[f.name] += f.amount

    for h in cls.hops:
        hops[h.name] += h.amount

    yeast[cls.yeast.name] += 1

print('Malt')
for m in sorted(malt):
    print(' ', rfill(m, 20), lfill(f'{malt[m]:.2f}', 5))

print('Hops')
for h in sorted(hops):
    print(' ', rfill(h, 20), lfill(str(hops[h]), 5))

print('Yeast')
for y in sorted(yeast):
    print(' ', rfill(y, 20), lfill(str(yeast[y]), 5))
