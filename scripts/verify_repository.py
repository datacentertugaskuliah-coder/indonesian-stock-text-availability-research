#!/usr/bin/env python3
"""Audits archived evidence hashes and numeric consistency without claiming model re-training.

Uses the Python standard library only so it runs in clean GitHub Actions runners.
"""
from pathlib import Path
import csv
import hashlib
import json
import math
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'
MANIFEST = ROOT / 'audit' / 'evidence_manifest.json'
LABELS = ('Down', 'Flat', 'Up')
failed = []
checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        failed.append(message)

def near(actual, expected, name, tol=1e-7):
    require(math.isfinite(float(actual)) and abs(float(actual)-expected) <= tol,
            f'{name}: observed {actual}, expected {expected} (tolerance {tol})')

def rows_of(num):
    matches = sorted((RESULTS/'tables').glob(f'Table_{num:02d}_*.csv'))
    require(len(matches) == 1, f'Expected one Table_{num:02d}, found {len(matches)}')
    if len(matches) != 1:
        return []
    with matches[0].open(encoding='utf-8-sig',newline='') as handle:
        return list(csv.DictReader(handle))

def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def png_data(path):
    # Read raster dimensions and the optional pHYs pixels-per-metre resolution field.
    with path.open('rb') as handle:
        require(handle.read(8)==bytes.fromhex('89504e470d0a1a0a'), f'Invalid PNG: {path.name}')
        width=height=0
        density=None
        while True:
            len_buf=handle.read(4)
            if len(len_buf)!=4: break
            length=int.from_bytes(len_buf,'big')
            chunk_type=handle.read(4)
            data=handle.read(length)
            crc=handle.read(4)
            if len(data)!=length or len(crc)!=4:break
            if chunk_type==b'IHDR':
                width,height=struct.unpack('>II',data[:8])
            if chunk_type==b'pHYs' and len(data)==9:
                px,py,unit=struct.unpack('>IIB',data)
                if unit==1:
                    density=(px*.0254,py*.0254)
            if chunk_type==b'IEND': break
    return width,height,density

def macro_from_confusion(cm):
    supports=[sum(cm[i]) for i in range(3)]
    predicted=[sum(cm[i][j] for i in range(3)) for j in range(3)]
    return sum(2*cm[i][i]/(supports[i]+predicted[i]) if supports[i]+predicted[i] else 0.0 for i in range(3))/3


def main():
    require(MANIFEST.exists(), 'Missing integrity manifest')
    if not MANIFEST.exists():
        print('\n'.join(failed), file=sys.stderr);return 1
    manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
    for ext,sub in [('csv','tables'),('png','figures')]:
        found=sorted((RESULTS/sub).glob(f'*.{ext}'))
        require(len(found)==20, f'Expected 20 {ext} files, got {len(found)}')
        require(sorted(int(f.name.split('_')[1]) for f in found)==list(range(1,21)),
                f'Unexpected {ext} numbering')
        for f in found:
            if ext=='csv':
                with f.open(encoding='utf-8-sig',newline='') as stream:
                    reader=csv.reader(stream)
                    header=next(reader,None)
                    body=list(reader)
                require(header is not None and len(header)>1 and bool(body),f'Empty/bad CSV: {f.name}')
            else:
                w,h,density=png_data(f)
                require(w>=750 and h>=450,f'Unexpected PNG pixel size: {f.name} ({w}x{h})')
                require(density is not None and 295 <= density[0] <= 305 and 295 <= density[1] <= 305,
                        f'Missing/incorrect 300 DPI tag: {f.name} {density}')
    require(len(manifest['files'])==41,'Expected 40 result artifacts and one notebook')
    for rel,spec in manifest['files'].items():
        file=ROOT/rel
        require(file.exists(),f'Missing manifest entry file {rel}')
        if file.exists():
            require(file.stat().st_size==spec['size_bytes'],f'Size mismatch {rel}')
            require(sha256(file)==spec['sha256'],f'SHA-256 mismatch {rel}')
    require(not list(ROOT.rglob('*.docx')), 'DOCX should not exist in GitHub repository')
    require(not list(ROOT.rglob('*.ris')), 'RIS should not exist in GitHub repository')
    require(not list((ROOT/'data/raw').glob('*.csv')), 'Raw source data must not be stored here')
    annual=rows_of(1)
    require(len(annual)==3,'Annual coverage table needs exactly 3 years')
    if len(annual)==3:
        expected={2022:(3690,3375,315,527),2023:(3585,3570,15,824),2024:(3555,3540,15,1668)}
        for r in annual:
            year=int(r['year'])
            require(year in expected, f'Unexpected year {year}')
            if year in expected:
                observed=tuple(int(r[k]) for k in ['market_sessions','eligible','excluded','sessions_with_archived_text'])
                require(observed==expected[year],f'Annual count mismatch {year}: {observed}')
                near(r['text_coverage_pct'],observed[3]/observed[0]*100,f'Text coverage {year}',1e-6)
        require(sum(int(r['eligible']) for r in annual)==10485,'Eligible grand total != 10485')
    target=rows_of(3)
    expected_labels={2022:{'Down':1545,'Flat':591,'Up':1239},
                     2023:{'Down':1542,'Flat':699,'Up':1329},
                     2024:{'Down':1397,'Flat':705,'Up':1438}}
    require(len(target)==9,'Need 9 year-label target rows')
    for r in target:
        y=int(r['year']);label=r['target_label']
        require(y in expected_labels and label in expected_labels.get(y,{}),f'Unexpected class {r}')
        if y in expected_labels and label in expected_labels[y]:
            require(int(r['n'])==expected_labels[y][label],f'Target label count mismatch {y} {label}')
    source_audit=rows_of(5)
    require(len(source_audit)>=18,'Too few source checks')
    for r in source_audit:
        require(r['pass'].strip().lower()=='true',f'Failed source-audit row: {r["check"]}')
    perf=rows_of(8)
    require(len(perf)==6,'Expect six evaluation models')
    score_expected={'M_market':.4401060768,'A_availability':.4778335546,
                    'W_word':.4763365287,'C_character':.4826472223,
                    'H_hybrid':.474165,'F_extra_trees':.459374}
    scores={r['model']:float(r['macro_f1']) for r in perf}
    for m,value in score_expected.items():
        require(m in scores,f'Missing model {m}')
        if m in scores:
            near(scores[m],value,f'Macro-F1 {m}',2e-5)
    for r in perf:
        require(int(r['n'])==3540,f'Wrong test size for {r["model"]}')
        for col in ['log_loss','brier_multiclass','balanced_accuracy']:
            require(math.isfinite(float(r[col])),f'Invalid metric {col} for {r["model"]}')
    confusion=rows_of(10)
    require(len(confusion)==54,'Expected 6 models x 9 confusion cells')
    by_model={}
    for r in confusion:
        model=r['model'];by_model.setdefault(model,{}).setdefault(r['actual'],{})[r['predicted']]=int(r['n'])
    for model,inner in by_model.items():
        require(all(a in inner and all(b in inner[a] for b in LABELS) for a in LABELS),f'Incomplete confusion for {model}')
        if not all(a in inner and all(b in inner[a] for b in LABELS) for a in LABELS):continue
        cm=[[inner[a][b] for b in LABELS] for a in LABELS]
        require(sum(sum(row) for row in cm)==3540,f'Test sample size confusion {model}')
        require([sum(cm[i]) for i in range(3)]==[1397,705,1438],f'Confusion class denominator {model}')
        if model in scores:
            near(macro_from_confusion(cm),scores[model],f'Macro-F1 recomputed from confusion {model}',1e-8)
    boot=rows_of(17)
    chosen=[r for r in boot if r['block_length']=='10' and r['contrast']=='C_character minus A_availability']
    require(len(chosen)==1,'Missing 10-session character contrast')
    if chosen:
        r=chosen[0]
        near(r['effect_macro_f1'],scores['C_character']-scores['A_availability'],'Bootstrap effect',1e-8)
        require(float(r['CI95_low'])<0<float(r['CI95_high']),'Reported 95% CI must include zero')
        near(r['p_holm_three_contrasts'],.996,'Holm p',.00001)
        require(r['reject_at_005'].strip().lower()=='false','Wrong reject flag')
    hold=rows_of(20)
    require(len(hold)==3,'Need 3 stock-disjoint models')
    observed_hold={'M_market':.4357055092,'A_availability':.4679716026,'C_character':.470169}
    for r in hold:
        require(int(r['n'])==3540,f'Wrong held-out rows {r["model"]}')
        if r['model'] in observed_hold:
            near(r['macro_f1'],observed_hold[r['model']],f'Held-out {r["model"]}',2e-5)
    print(f'Static evidence audit: {checks} assertions, {len(failed)} failures.')
    if failed:
        for problem in failed:print('FAIL:',problem,file=sys.stderr)
        return 1
    print('PASS: exactly 20 CSV + 20 PNG, original hashes, DPI and cross-table metrics consistent.')
    print('LIMITATION: static check is not an independent re-training or a Scopus/Q1 certification.')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
