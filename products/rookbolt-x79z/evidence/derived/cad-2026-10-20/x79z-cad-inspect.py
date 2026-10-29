import FreeCAD,Part,Import,json,os
root='/Users/kaziwaseef/Documents/WORK/ip-analyser/products/rookbolt-x79z'
out=root+'/evidence/derived/cad-2026-10-20'
os.makedirs(out,exist_ok=True)
doc=FreeCAD.newDocument('X79ZInspection')
Import.insert(root+'/evidence/raw/supplier-package/X79Z 3D File.stp',doc.Name)
rows=[]
for obj in doc.Objects:
 if not hasattr(obj,'Shape') or obj.Shape.isNull():continue
 sh=obj.Shape;b=sh.BoundBox
 rows.append({'name':obj.Name,'label':obj.Label,'type':obj.TypeId,'solids':len(sh.Solids),'faces':len(sh.Faces),'volume_mm3':sh.Volume,'bounds_mm':[b.XMin,b.YMin,b.ZMin,b.XMax,b.YMax,b.ZMax],'lengths_mm':[b.XLength,b.YLength,b.ZLength],'children':[x.Name for x in obj.OutList]})
with open(out+'/shape-inventory.json','w') as f:json.dump({'FreeCAD':FreeCAD.Version(),'objects':rows},f,indent=2)
print('X79Z_SHAPES',len(rows))
for row in rows:print(json.dumps(row))
doc.saveAs(out+'/X79Z-inspection.FCStd')
