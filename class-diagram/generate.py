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
AREAS=[('① 모임 생성·신청',['1','2-1','2-2','3','4-2']),('② 모임 현장 운영',['5','6','7','8','18-1','18-2']),('③ 모임 종료·사후 관리',['9','10','11','12','13','15','19']),('④ 부가·연계 서비스',['16','17','20'])]
assert sorted(sum((a[1] for a in AREAS),[]))==sorted(cl[n]['fn'] for n in by['담당 객체']),'AREAS가 담당 객체와 맞지 않음'
fx=lambda L:', '.join(L)
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
out.append(f'{len(cl)}개 클래스의 이름만 종류별로 묶었다. 관계선은 3장에서 본다.\n')
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
out.append('| PPT | 절 | 내용 |\n|---|---|---|\n| 1장 | 2장 전체 그림, 통합 다이어그램 | '+str(len(cl))+'개, 이름만, 관계선 포함 |\n'+''.join(f'| {2+j}장 | 3.{1+j} | {a[0]} |\n' for j,a in enumerate(AREAS))+'| 6장 | 3.5, 3.6 | 공통 객체·외부, DB 회원·모임 |\n| 7장 | 3.7 | DB 모임 진행 |\n| 8장 | 3.8 | DB 평가·교류 |\n| 9장 | 3.9 | 사장님UI·엔티티 |\n| 10장 | 3.10 | 학생UI |\n| 슬라이드 아님 | 3.11 | 참고용: 공통 객체·DB·엔티티 사이의 관계선 |\n')
seen=set()
for title,names in [(f'3.{1+j} {a[0]} (기능 {fx(a[1])})',pick(a[1])) for j,a in enumerate(AREAS)]:
    c_,s=areafig(names); seen|=set(s); out.append(f'### {title}\n'); out.append(c_)
out.append('### 3.5 공통 객체·외부\n'); out.append(detail(by['공통 객체']+by['외부']))
for j,(t_,ns) in enumerate(DB):
    out.append(f'### 3.{6+j} DB: {t_}\n'); out.append(detail(ns))
out.append('### 3.9 사장님UI·엔티티\n'); out.append(detail(['사장님UI']+by['엔티티']))
out.append('### 3.10 학생UI\n'); out.append(detail(['학생UI']))
rest=sorted(edges-seen)
use=sorted({x for e in rest for x in e})
L=HEAD+['classDiagram','    direction LR']
for n in use: L.append(f'    class {cl[n]["id"]}["{n}"]')
for a,b in rest: L.append(f'    {cl[a]["id"]} -- {cl[b]["id"]}')
out.append('### 3.11 공통 객체·DB·엔티티 사이의 관계선 (참고용)\n'); out.append(code(L))
assert seen|set(rest)==edges
# StarUML 옮겨 적기 (CONVENTIONS 8.1, 8.2)
ENUMS=[]
_g=(ROOT/'GLOSSARY.md').read_text(encoding='utf-8').replace('\r','')
_m=re.search(r'^## 7\. enum.*?\n(.*?)(?=^## )',_g,re.M|re.S)
for _l in _m[1].split('\n'):
    _c=[x.strip() for x in _l.split('|')]
    if len(_c)>4 and _c[1] and _c[1] not in ('enum',) and not _c[1].startswith('-'): ENUMS.append(_c[1])
_ep=re.compile(r'(?<![가-힣A-Za-z0-9])('+'|'.join(map(re.escape,ENUMS))+r')(?![가-힣A-Za-z0-9])')
def su_type(x): return _ep.sub('String',x.strip())
def su_params(s):
    parts,depth,cur=[],0,''
    for ch in s:
        if ch=='<': depth+=1
        if ch=='>': depth-=1
        if ch==',' and depth==0: parts.append(cur); cur=''
        else: cur+=ch
    if cur.strip(): parts.append(cur)
    return ', '.join(su_type(x.split(':',1)[1] if ':' in x else x) for x in parts)
def su_op(sig):
    m=re.match(r'^([^()]+)\((.*)\)\s*(?::\s*(.+))?$',sig.strip())
    if not m: return sig
    r=f'{m[1].strip()}({su_params(m[2])})'
    return r+(f': {su_type(m[3])}' if m[3] else '')
out.append('## 4. StarUML 옮겨 적기\n')
out.append(f'StarUML에 옮길 때 그대로 적는 표기다 (CONVENTIONS 8.1, 8.2). 매개변수 이름을 빼고 자료형만 적으며, enum 타입({", ".join(ENUMS)})은 `String`으로 적는다. 속성 이름, 엔티티 이름, `List<타입>`은 그대로 둔다. 순서는 3장 영역별 그림과 같다.\n')
out.append('같은 내용을 StarUML에 한 번에 만드는 스크립트가 `class-diagram/staruml-script.js`에 있다. StarUML에서 **File → New**로 빈 프로젝트를 연 뒤, 파일 내용 전체를 복사해 **Script Console**(아래 창) 입력줄에 붙여 넣고 Enter를 누른다. 클래스 '+str(len(cl))+'개, 관계선, 다이어그램 10개(1 통합, 2~10 PPT 슬라이드 순서)가 만들어진다. 배치는 격자로만 놓이므로 손으로 정리한다.\n')
_done=set(); _cnt=[0,0]
_groups=[(f'4.{1+j} 담당 객체: {a[0]}',pick(a[1])) for j,a in enumerate(AREAS)]+[('4.5 공통 객체·외부',by['공통 객체']+by['외부'])]+[(f'4.{6+j} DB: {t_}',ns) for j,(t_,ns) in enumerate(DB)]+[('4.9 사장님UI·엔티티',['사장님UI']+by['엔티티']),('4.10 학생UI',['학생UI'])]
for _title,_names in _groups:
    out.append(f'### {_title}\n')
    for n in _names:
        _done.add(n); c=cl[n]; L=[n]
        for v,a,t_ in c['attrs']:
            s=su_type(t_); _cnt[1]+=s!=t_.strip(); L.append(f'{v}{a}: {s}')
        for v,s in c['ops']:
            r=su_op(s); _cnt[0]+=r!=s.strip(); L.append(f'{v}{r}')
        out.append('```text\n'+'\n'.join(L)+'\n```\n')
assert _done==set(cl),set(cl)-_done
print('staruml lines changed',_cnt[0],'attrs changed',_cnt[1])
# StarUML 스크립트 (Script Console에 붙여 넣으면 클래스와 다이어그램 10개를 만든다)
import json
names=list(cl)
idx={n:i for i,n in enumerate(names)}
def split_params(s): return su_params(s).split(', ') if s.strip() else []
C=[]
for n in names:
    c=cl[n]; A=[]; O=[]
    for v,a,t in c['attrs']: A.append([v,a,su_type(t)])
    for v,s in c['ops']:
        m=re.match(r'^([^()]+)\((.*)\)\s*(?::\s*(.+))?$',s.strip())
        assert m,s
        O.append([v,m[1].strip(),split_params(m[2]),su_type(m[3]) if m[3] else ''])
    C.append([n,A,O])
E=[[idx[a],idx[b]] for a,b in sorted(edges)]
def area(title,main,lines=True):
    S=set(main)
    others=sorted({x for e in edges if e[0] in S or e[1] in S for x in e}-S) if lines else []
    return [title,[idx[n] for n in main],[idx[n] for n in others],1 if lines else 0]
order=['담당 객체','공통 객체','DB','UI','외부','엔티티']
whole=[idx[n] for k in order for n in by[k]]
AR=[area(f'{2+j} {a[0]}',pick(a[1])) for j,a in enumerate(AREAS)]+[
    area('6 공통 객체·외부·DB 회원·모임',by['공통 객체']+by['외부']+DB[0][1],False),area('7 DB 모임 진행',DB[1][1],False),area('8 DB 평가·교류',DB[2][1],False),area('9 사장님UI·엔티티',['사장님UI']+by['엔티티'],False),area('10 학생UI',['학생UI'],False)]
data=json.dumps({'C':C,'E':E,'W':whole,'A':AR},ensure_ascii=False,separators=(',',':'))
js=r'''(function(D){
var F=app.factory,R=[],M=app.project.getProject().ownedElements.filter(function(e){return e instanceof type.UMLModel})[0],bad=0;
function vis(v){return v=="-"?"private":"public"}
function tw(s){var w=0;for(var i=0;i<s.length;i++)w+=s.charCodeAt(i)>255?14:8;return w}
var size=D.C.map(function(c){var L=[c[0]];c[1].forEach(function(a){L.push(a[0]+a[1]+": "+a[2])});c[2].forEach(function(o){L.push(o[0]+o[1]+"("+o[2].join(", ")+")"+(o[3]?": "+o[3]:""))});return{w:Math.max.apply(null,L.map(tw))+30,h:50+(c[1].length+c[2].length)*15+20,nw:tw(c[0])+40}});
var K=D.C.map(function(c){
 var k=F.createModel({id:"UMLClass",parent:M,modelInitializer:function(e){e.name=c[0]}});
 c[1].forEach(function(a){F.createModel({id:"UMLAttribute",parent:k,field:"attributes",modelInitializer:function(e){e.name=a[1];e.type=a[2];e.visibility=vis(a[0])}})});
 c[2].forEach(function(o){var op=F.createModel({id:"UMLOperation",parent:k,field:"operations",modelInitializer:function(e){e.name=o[1];e.visibility=vis(o[0])}});
  o[2].forEach(function(t){F.createModel({id:"UMLParameter",parent:op,field:"parameters",modelInitializer:function(e){e.name=t}})});
  if(o[3])F.createModel({id:"UMLParameter",parent:op,field:"parameters",modelInitializer:function(e){e.direction="return";e.type=o[3]}})});
 return k});
function dia(n){return F.createDiagram({id:"UMLClassDiagram",parent:M,diagramInitializer:function(d){d.name=n}})}
function put(d,i,x,y,full){var v=F.createViewOf({model:K[i],diagram:d,x:x,y:y});if(!full){app.engine.setProperty(v,"suppressAttributes",true);app.engine.setProperty(v,"suppressOperations",true)}return v}
var W=dia("1 통합 다이어그램 ("+D.C.length+"개)"),V={};
D.W.forEach(function(i,j){V[i]=put(W,i,40+(j%8)*230,40+Math.floor(j/8)*110,false)});
var AS=D.E.map(function(e){return F.createModelAndView({id:"UMLAssociation",parent:M,diagram:W,tailView:V[e[0]],headView:V[e[1]],tailModel:K[e[0]],headModel:K[e[1]]}).model});
D.A.forEach(function(a){var d=dia(a[0]),x=40,y=40,cw=0,on={};
 a[1].forEach(function(i){var s=size[i];if(y>40&&y+s.h>1400){x+=cw+60;y=40;cw=0}put(d,i,x,y,true);on[i]=1;y+=s.h+40;cw=Math.max(cw,s.w)});
 var ox=x+cw+120;a[2].forEach(function(i,j){put(d,i,ox+(j%3)*230,40+Math.floor(j/3)*110,false);on[i]=1});
 var mine={};a[1].forEach(function(i){mine[i]=1});
 if(a[3])D.E.forEach(function(e,j){if((mine[e[0]]||mine[e[1]])&&on[e[0]]&&on[e[1]]&&!d.getViewOf(AS[j])){try{F.createViewOf({model:AS[j],diagram:d})}catch(err){bad++}}});
 var ex=d.ownedViews.filter(function(v){if(!(v.model instanceof type.UMLAssociation))return false;var p=K.indexOf(v.model.end1.reference),q=K.indexOf(v.model.end2.reference);return !(a[3]&&(mine[p]||mine[q]))});
 if(ex.length){try{app.engine.deleteElements([],ex)}catch(err){bad+=ex.length}}});
console.log("클래스 "+K.length+"개, 관계 "+AS.length+"개, 다이어그램 "+(1+D.A.length)+"개 생성"+(bad?", 영역 그림에 못 그린 관계선 "+bad+"개":""));
})('''+data+');'
(ROOT/'class-diagram'/'staruml-script.js').write_text(js.replace('\n','')+'\n',encoding='utf-8',newline='\n')
(ROOT/'class-diagram'/'class-diagram.md').write_text('\n'.join(out),encoding='utf-8',newline='\n')
print('classes',len(cl),dict(ptn),'edges',len(edges),'rest',len(rest),'skipped',dict(skipped))
