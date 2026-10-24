#!/usr/bin/env python3
"""Compare an optional local rerun with archived tables without replacing the original evidence."""
import csv
import math
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REFERENCE=ROOT/'results/tables'
PRODUCED=Path(sys.argv[1]).expanduser().resolve() if len(sys.argv)>1 else ROOT/'artifacts/Q1_20PNG_20CSV/tables'
if not PRODUCED.exists():
    raise SystemExit(f'Generated table directory not found: {PRODUCED}')

def contents(path):
    with path.open(encoding='utf-8-sig',newline='') as fp:
        return list(csv.DictReader(fp))

biggest=[]
for original in sorted(REFERENCE.glob('Table_*.csv')):
    new=PRODUCED/original.name
    if not new.exists():
        print('MISSING',original.name);continue
    a,b=contents(original),contents(new)
    if len(a)!=len(b):
        print('ROW_COUNT_CHANGED',original.name,len(a),len(b));continue
    maxdiff=0.0; changed_non_numeric=[]
    for n,(ra,rb) in enumerate(zip(a,b)):
        for col in ra:
            u,v=ra[col],rb[col]
            if u==v:continue
            try:
                x,y=float(u),float(v)
                if math.isfinite(x) and math.isfinite(y):
                    maxdiff=max(maxdiff,abs(x-y))
                    continue
            except ValueError:pass
            changed_non_numeric.append((n,col,u,v))
    biggest.append((maxdiff,original.name))
    print(original.name,'max_abs_numeric_delta:',f'{maxdiff:.9g}',
          'non_numeric_differences:',len(changed_non_numeric))
print('Largest numeric table delta:',max(biggest) if biggest else 'N/A')
print('Do not automatically overwrite the reference output from reruns.')
