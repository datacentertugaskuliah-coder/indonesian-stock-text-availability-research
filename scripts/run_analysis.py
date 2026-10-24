#!/usr/bin/env python3
"""Run the research notebook's exact executable cells as Python without modifying the model."""
import json
import os
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
notebook=ROOT/'notebooks/Source_Only_20PNG_20CSV.ipynb'
cells=json.loads(notebook.read_text(encoding='utf-8'))['cells']
ns={'__name__':'__main__'}
for number,cell in enumerate(cells,1):
    if cell.get('cell_type')!='code':
        continue
    source=''.join(cell['source'])
    if not source.strip():
        continue
    print(f'Running notebook code cell {number}...',flush=True)
    exec(compile(source,str(notebook)+f':cell{number}','exec'),ns)
