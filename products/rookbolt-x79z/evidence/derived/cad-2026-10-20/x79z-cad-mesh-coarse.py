import FreeCAD,MeshPart,json
p='/Users/kaziwaseef/Documents/WORK/ip-analyser/products/rookbolt-x79z/evidence/derived/cad-2026-10-20'
doc=FreeCAD.openDocument(p+'/X79Z-inspection.FCStd');root=doc.getObject('_413_02_ASM');parts=[]
for i,s in enumerate(root.Shape.Solids,1):
 mesh=MeshPart.meshFromShape(Shape=s,LinearDeflection=0.3,AngularDeflection=0.35,Relative=False);v,tri=mesh.Topology;b=s.BoundBox
 parts.append({'id':'CAD-%03d'%i,'bounds_mm':[b.XMin,b.YMin,b.ZMin,b.XMax,b.YMax,b.ZMax],'lengths_mm':[b.XLength,b.YLength,b.ZLength],'volume_mm3':s.Volume,'vertices':[[a.x,a.y,a.z] for a in v],'triangles':tri})
with open(p+'/inspection-mesh.json','w') as f:json.dump({'version':FreeCAD.Version(),'root':root.Label,'units':'mm','linear_deflection_mm':0.3,'angular_deflection_radians':0.35,'parts':parts},f)
print('CAD solids',len(parts),'triangles',sum(len(x['triangles']) for x in parts))
