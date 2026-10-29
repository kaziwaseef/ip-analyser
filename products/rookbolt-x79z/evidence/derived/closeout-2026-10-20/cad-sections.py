import FreeCAD,Part,json
from pathlib import Path
r=Path('/Users/kaziwaseef/Documents/WORK/ip-analyser/products/rookbolt-x79z/evidence/derived')
doc=FreeCAD.openDocument(str(r/'cad-2026-10-20/X79Z-inspection.FCStd'))
root=doc.getObjectsByLabel('0413-02_ASM')[0]
solids=root.Shape.Solids;out={'source':'S-017, preserved FreeCAD import','sections':[],'head_faces':[]}
for x in [0,5,15]:
 plane=Part.Plane(FreeCAD.Vector(x,100,0),FreeCAD.Vector(1,0,0)).toShape(-400,400,-400,400)
 parts=[]
 for i,s in enumerate(solids):
  sec=s.section(plane)
  curves=[]
  for e in sec.Edges:
   curves.append([[v.x,v.y,v.z] for v in e.discretize(Deflection=0.02)])
  parts.append({'solid':i+1,'curves':curves})
 out['sections'].append({'x_mm':x,'parts':parts})
for i in [20,21]:
 s=solids[i]
 for j,f in enumerate(s.Faces):
  if f.Area<15:continue
  su=f.Surface;row={'solid':i+1,'face':j+1,'surface':type(su).__name__,'area_mm2':f.Area,'center_mm':[f.CenterOfMass.x,f.CenterOfMass.y,f.CenterOfMass.z]}
  for attr in ['Radius','Axis','Position']:
   if hasattr(su,attr):
    v=getattr(su,attr);row[attr]=[v.x,v.y,v.z] if hasattr(v,'x') else v
  out['head_faces'].append(row)
(r/'closeout-2026-10-20/cad-sections.json').write_text(json.dumps(out,indent=2))
print('Exported sections and head face inventory')
