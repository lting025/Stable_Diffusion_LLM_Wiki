#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parent.parent
class Document(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.stack=[];self.references=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs); self.stack.append((tag,a)) if tag not in ('meta','link','br','img','input','hr') else None
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a':self.links.append(a.get('href',''))
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
 def handle_data(self,data):
  for r in re.findall(r'\[([1-5])\]',data):
   if any(tag=='a' and a.get('href')=='wiki.html#paper-'+r for tag,a in self.stack):self.references.append(r)
def parse(path):x=Document();x.feed(path.read_text(encoding='utf8'));return x
checks=[]; docs=root/'docs'; parsed={f.name:parse(f) for f in docs.glob('*.html')}
for name,doc in parsed.items():
 bad=[]
 for href in doc.links:
  if not href or href.startswith(('https:','http:','mailto:')):continue
  path,_,frag=href.partition('#'); target=docs/path if path else docs/name
  if not target.exists():bad.append(href)
  elif frag and target.suffix=='.html' and frag not in parsed[target.name].ids:bad.append(href)
 checks.append((not bad,f'{name} 相對連結及錨點：'+('通過' if not bad else '失敗 '+str(bad))))
refs=set(parsed['index.html'].references); checks.append((refs==set('12345'),'簡報可直接連到論文 1–5：'+''.join(sorted(refs))))
checks.append((len(list((root/'wiki/papers').glob('*.md')))==5,'Wiki 論文筆記數：'+str(len(list((root/'wiki/papers').glob('*.md'))))))
for f in sorted((root/'raw').glob('*.pdf')):checks.append((f.read_bytes()[:5]==b'%PDF-',f'{f.name} PDF 檔頭：'+('通過' if f.read_bytes()[:5]==b'%PDF-' else '失敗')))
checks.append((len(list((root/'raw').glob('*.pdf')))==5,'原文 PDF 數量：'+str(len(list((root/'raw').glob('*.pdf'))))))
for ok,msg in checks: print(('PASS ' if ok else 'FAIL ')+msg)
print('說明：此程式不評估文章內容正確性、外部連結即時可用性或網頁顯示效果。')
sys.exit(0 if all(x[0] for x in checks) else 1)
