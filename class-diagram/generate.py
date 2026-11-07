"""classes/ 파일로 class-diagram/class-diagram.md를 만든다.

실행: python class-diagram/generate.py (macOS는 python3)
표준 라이브러리만 쓰므로 설치할 것이 없다.
"""
import re,os,sys,collections
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding='utf-8')
cl={}
for f in sorted((ROOT/'classes').glob('*.md')):
    t=f.read_text(encoding='utf-8').replace('\r','')
    name=re.search(r'^#\s*클래스:\s*(.+?)\s*$',t,re.M)[1]
    kind=re.search(r'^\| 종류 \| (.*?) \|$',t,re.M)[1]
    def sec(n):
        m=re.search(rf'^## {n}\n(.*?)(?=^## |\Z)',t,re.M|re.S); return m[1] if m else ''
    attrs=[[x.strip() for x in l.split('|')][1:4] for l in sec('속성').split('\n') if re.match(r'\| [+-] \|',l)]
    ops=[[x.strip() for x in l.split('|')][1:3] for l in sec('연산').split('\n') if re.match(r'\| [+-] \|',l)]
    rel=[l.split('|')[1].strip() for l in sec('관계').split('\n') if l.startswith('|') and not l.startswith('|---') and '연결 대상' not in l]
    m=re.search(r'\(기능 ([\d-]+)\)',kind)
    cl[name]=dict(id=f.stem,file=f.name,kind=kind.split(' (')[0],fn=m[1] if m else None,attrs=attrs,ops=ops,rel=rel)
edges=set(); skipped=collections.Counter()
for n,c in cl.items():
    for r in c['rel']:
        if r in cl and r!=n: edges.add(tuple(sorted((n,r))))
        elif r not in cl: skipped[r]+=1
G=lambda s:s.replace('<','~').replace('>','~')
def box(n):
    c=cl[n]; L=[f'    class {c["id"]}["{n}"] {{']
    for v,a,t_ in c['attrs']: L.append(f'        {v}{a}: {G(t_)}')
    for v,s in c['ops']: L.append('        '+v+G(s.replace('): ',') ')))
    L.append('    }'); return L
def code(lines): return '```mermaid\n'+'\n'.join(lines)+'\n```\n'
def detail(names):
    L=['classDiagram','    direction LR']
    for n in names: L+=box(n)
    return code(L)
def relfig(names):
    S=set(names); shown=[e for e in sorted(edges) if e[0] in S or e[1] in S]
    use=sorted({x for e in shown for x in e}|S)
    L=['classDiagram','    direction LR']
    for n in use: L.append(f'    class {cl[n]["id"]}["{n}"]')
    for a,b in shown: L.append(f'    {cl[a]["id"]} -- {cl[b]["id"]}')
    return code(L),shown
by=collections.defaultdict(list)
for n,c in cl.items(): by[c['kind']].append(n)
order=['담당 객체','공통 객체','DB','UI','외부','엔티티']
def fnkey(n):
    return [int(x) for x in cl[n]['fn'].split('-')]
by['담당 객체'].sort(key=fnkey)
PRE=['1','2-1','2-2','3','4-2'];MID=['5','6','7','8','16','17','18-1','18-2'];POST=['9','10','11','12','13','15','19','20']
pick=lambda L:[n for n in by['담당 객체'] if cl[n]['fn'] in L]
DB=[('회원·모임',['프로필DB','정지DB','가게DB','모임DB','신청DB','결제DB']),('모임 진행',['관심등록DB','배치DB','출석DB','주문DB','질문카드DB','화장실대기열DB']),('평가·교류',['평가DB','신고DB','기부DB','품앗이DB','2차공지DB','2차기록DB'])]
assert sum(len(x[1]) for x in DB)==len(by['DB']) and set(sum((x[1] for x in DB),[]))==set(by['DB'])
# 전체 그림
L=['flowchart TB']; prev=None; COL=5
for k in order:
    ns=by[k]; sid={'담당 객체':'G1','공통 객체':'G2','DB':'G3','UI':'G4','외부':'G5','엔티티':'G6'}[k]
    L.append(f'    subgraph {sid}["{k} {len(ns)}개"]')
    for n in ns: L.append(f'        {cl[n]["id"]}["{n}"]')
    for i in range(len(ns)-COL): L.append(f'        {cl[ns[i]]["id"]} ~~~ {cl[ns[i+COL]]["id"]}')
    L.append('    end')
    if prev: L.append(f'    {prev} ~~~ {sid}')
    prev=sid
overall=code(L)
ptn=collections.Counter(c['kind'] for c in cl.values())
out=[]
out.append('# 통합 클래스 다이어그램\n')
out.append('> 이 파일은 스크립트로 만든다. 직접 고치지 말고 `classes/`를 고친 뒤 다시 생성한다. 실행: `python class-diagram/generate.py` (macOS는 `python3`)\n')
out.append('`classes/`의 클래스 파일을 모은 그림이다 (CONVENTIONS 6.5). **원본은 `classes/` 파일이다.** 제출할 때는 CONVENTIONS 8.2에 따라 StarUML 한 장으로 옮긴다.\n')
out.append('## 1. 클래스 개수 대조\n')
out.append('| 종류 | 개수 |\n|---|---|')
for k in order: out.append(f'| {k} | {ptn[k]} |')
out.append(f'| **합계** | **{len(cl)}** |\n')
out.append(f'`classes/` 파일 {len(cl)}개와 1:1로 대응한다. 관계선은 두 클래스 사이에 하나씩, 모두 {len(edges)}개다.\n')
out.append('| 번호 | 클래스 | 종류 | 파일 |\n|---|---|---|---|')
i=0
for k in order:
    for n in by[k]:
        i+=1; ex=f' (기능 {cl[n]["fn"]})' if cl[n]['fn'] else ''
        out.append(f'| {i} | {n} | {k}{ex} | [{cl[n]["file"]}](../classes/{cl[n]["file"]}) |')
out.append('\n## 2. 전체 그림\n')
out.append('53개 클래스의 이름만 종류별로 묶었다. 관계선은 3장에서 본다.\n')
out.append(overall)
HEAD=['---','config:','  class:','    hideEmptyMembersBox: true','---']
def areafig(names):
    S=set(names); shown=[e for e in sorted(edges) if e[0] in S or e[1] in S]
    others=sorted({x for e in shown for x in e}-S)
    L=HEAD+['classDiagram','    direction LR']
    for n in names: L+=box(n)
    for n in others: L.append(f'    class {cl[n]["id"]}["{n}"]')
    for a,b in shown:
        if a not in S: a,b=b,a  # 담당 객체를 왼쪽에 모은다
        L.append(f'    {cl[a]["id"]} -- {cl[b]["id"]}')
    return code(L),shown
out.append('## 3. 영역별 그림\n')
out.append('PPT 2장부터 쓰는 그림이다. StarUML에서는 영역마다 다이어그램을 따로 만들고, Model Explorer의 기존 클래스를 끌어다 놓는다. 표기는 Mermaid 규칙에 따라 `List<int>`를 `List~int~`로 적지만 그림에는 `List<int>`로 나온다.\n')
out.append('| PPT | 절 | 내용 |\n|---|---|---|\n| 1장 | 2장 전체 그림, 통합 다이어그램 | 53개, 이름만, 관계선 포함 |\n| 2장 | 3.1 | 모임 전 |\n| 3장 | 3.2 | 모임 중: 출석·교류 |\n| 4장 | 3.3 | 모임 중: 기부·품앗이·화장실 |\n| 5장 | 3.4 | 모임 후: 정산·평가·신고 |\n| 6장 | 3.5 | 모임 후: 귀가·예보·2차 |\n| 7장 | 3.6~3.9 | 공통 객체, 외부, DB |\n| 8장 | 3.10~3.11 | UI, 엔티티 |\n')
seen=set()
for title,names in [('3.1 모임 전 (기능 1, 2-1, 2-2, 3, 4-2)',pick(PRE)),('3.2 모임 중: 출석·교류 (기능 5, 6, 7, 8)',pick(['5','6','7','8'])),('3.3 모임 중: 기부·품앗이·화장실 (기능 16, 17, 18-1, 18-2)',pick(['16','17','18-1','18-2'])),('3.4 모임 후: 정산·평가·신고 (기능 9, 10, 11, 12, 13)',pick(['9','10','11','12','13'])),('3.5 모임 후: 귀가·예보·2차 (기능 15, 19, 20)',pick(['15','19','20']))]:
    c_,s=areafig(names); seen|=set(s); out.append(f'### {title}\n'); out.append(c_)
out.append('### 3.6 공통 객체·외부\n'); out.append(detail(by['공통 객체']+by['외부']))
for j,(t_,ns) in enumerate(DB):
    out.append(f'### 3.{7+j} DB: {t_}\n'); out.append(detail(ns))
out.append('### 3.10 사장님UI·엔티티\n'); out.append(detail(['사장님UI']+by['엔티티']))
out.append('### 3.11 학생UI\n'); out.append(detail(['학생UI']))
rest=sorted(edges-seen)
use=sorted({x for e in rest for x in e})
L=HEAD+['classDiagram','    direction LR']
for n in use: L.append(f'    class {cl[n]["id"]}["{n}"]')
for a,b in rest: L.append(f'    {cl[a]["id"]} -- {cl[b]["id"]}')
out.append('### 3.12 공통 객체·DB·엔티티 사이의 관계선\n'); out.append(code(L))
assert seen|set(rest)==edges
(ROOT/'class-diagram'/'class-diagram.md').write_text('\n'.join(out),encoding='utf-8',newline='\n')
print('classes',len(cl),dict(ptn),'edges',len(edges),'rest',len(rest),'skipped',dict(skipped))
