"""Restore unchanged source chart workbooks dropped by the PPTX import/export cycle."""
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree as E
import copy, json, posixpath, sys, hashlib

source, candidate=map(Path,sys.argv[1:3])
C='http://schemas.openxmlformats.org/drawingml/2006/chart'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
P='http://schemas.openxmlformats.org/package/2006/relationships'
CT='http://schemas.openxmlformats.org/package/2006/content-types'
NS={'c':C}
def signature(root):
 return tuple(tuple(tuple(s.xpath(f'./c:{field}//c:v/text()',namespaces=NS)) for field in ['tx','cat','val']) for s in root.xpath('.//c:ser',namespaces=NS))
def relname(name):
 p=PurePosixPath(name);return str(p.parent/'_rels'/(p.name+'.rels'))
with ZipFile(source) as z:src={n:z.read(n) for n in z.namelist()}
with ZipFile(candidate) as z:dst={n:z.read(n) for n in z.namelist()}
known={}
for n,b in src.items():
 if '/charts/' in n and n.endswith('.xml') and '/_rels/' not in n:
  root=E.fromstring(b);ext=root.find(f'{{{C}}}externalData')
  if ext is not None:known[signature(root)]=(n,root,ext)
repairs=[]
for n,b in list(dst.items()):
 if '/charts/' not in n or not n.endswith('.xml') or '/_rels/' in n:continue
 root=E.fromstring(b);sig=signature(root)
 if sig not in known:raise ValueError('Chart data changed or source workbook missing: '+n)
 oldname,oldroot,ext=known[sig]
 # Preserve the exact formula references as well as the cached series values.
 assert root.xpath('.//c:ser//c:f/text()',namespaces=NS)==oldroot.xpath('.//c:ser//c:f/text()',namespaces=NS)
 oldrels=E.fromstring(src[relname(oldname)])
 rel=next(x for x in oldrels if x.get('Id')==ext.get(f'{{{R}}}id'))
 book=posixpath.normpath(posixpath.join(posixpath.dirname(oldname),rel.get('Target')))
 dst[book]=src[book]
 newrels=E.fromstring(dst[relname(n)]) if relname(n) in dst else E.Element(f'{{{P}}}Relationships',nsmap={None:P})
 newrel=copy.deepcopy(rel);newrel.set('Target',posixpath.relpath(book,posixpath.dirname(n)))
 assert not any(x.get('Id')==newrel.get('Id') for x in newrels)
 newrels.append(newrel);dst[relname(n)]=E.tostring(newrels,encoding='UTF-8',xml_declaration=True,standalone=True)
 for x in root.findall(f'{{{C}}}externalData'):root.remove(x)
 newext=copy.deepcopy(ext)
 # externalData precedes printSettings/userShapes/extLst in CT_ChartSpace.
 successors=[x for x in root if E.QName(x).localname in ['printSettings','userShapes','extLst']]
 root.insert(root.index(successors[0]) if successors else len(root),newext)
 dst[n]=E.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
 repairs.append({'chart':n,'source_chart':oldname,'workbook':book,'source_workbook_sha256':hashlib.sha256(src[book]).hexdigest(),'copied_bytes_unchanged':True})
assert len(repairs)==2,repairs
ct=E.fromstring(dst['[Content_Types].xml'])
if not any(x.get('Extension')=='xlsx' for x in ct):E.SubElement(ct,f'{{{CT}}}Default',Extension='xlsx',ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
dst['[Content_Types].xml']=E.tostring(ct,encoding='UTF-8',xml_declaration=True,standalone=True)
tmp=candidate.with_suffix('.repairing.pptx')
with ZipFile(tmp,'w',ZIP_DEFLATED) as z:
 for n,b in dst.items():z.writestr(n,b)
tmp.replace(candidate)
candidate.with_suffix('.workbook-repair.json').write_text(json.dumps(repairs,indent=2)+'\n')
print('Restored 2 source workbooks without changing their bytes, chart values or formulas.')
