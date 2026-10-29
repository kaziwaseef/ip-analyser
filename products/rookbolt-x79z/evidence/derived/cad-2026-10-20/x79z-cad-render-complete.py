from pathlib import Path
import json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
p=Path('products/rookbolt-x79z/evidence/derived/cad-2026-10-20');j=json.loads((p/'inspection-mesh.json').read_text());parts=j['parts']
def add(ax,part,shift=None):
 v=np.asarray(part['vertices']);tri=np.asarray(part['triangles']);stride=1;v=v+(np.asarray(shift) if shift is not None else 0)
 c=Poly3DCollection(v[tri[::stride]],facecolors=plt.cm.tab20((int(part['id'][-3:])-1)%20),edgecolors='none',alpha=1);ax.add_collection3d(c)
 b=np.asarray(part['bounds_mm']);mi=b[:3];ma=b[3:];center=(mi+ma)/2
 return center
fig=plt.figure(figsize=(13,11));
for k,(elev,azim) in enumerate([(25,-55),(25,125),(90,-90),(0,0)],1):
 ax=fig.add_subplot(2,2,k,projection='3d')
 for part in parts:add(ax,part)
 ax.set(xlim=(-45,45),ylim=(35,255),zlim=(-80,20),xlabel='X mm',ylabel='Y mm',zlabel='Z mm');ax.set_box_aspect((90,220,100));ax.view_init(elev=elev,azim=azim);ax.set_axis_off();ax.set_title('Final supplied CAD, view '+str(k))
fig.suptitle('X79Z CAD model. Colors identify solids, not materials. As-modelled pose only.');fig.savefig(p/'assembly-views.png',dpi=130);plt.close(fig)
fig=plt.figure(figsize=(16,15))
for k,part in enumerate(parts,1):
 ax=fig.add_subplot(4,6,k,projection='3d');center=add(ax,part);b=np.asarray(part['bounds_mm']);size=max(b[3:]-b[:3])*0.6
 ax.set(xlim=(center[0]-size,center[0]+size),ylim=(center[1]-size,center[1]+size),zlim=(center[2]-size,center[2]+size));ax.set_box_aspect((1,1,1));ax.view_init(elev=28,azim=-55);ax.set_axis_off();ax.set_title(part['id']+' '+str([round(x,1) for x in part['lengths_mm']])+' mm',fontsize=9)
fig.suptitle('Individual solid inspection. Each panel independently scaled. No material/polarity inference.');fig.savefig(p/'solid-inventory-views.png',dpi=130);plt.close(fig)
print('Saved assembly and22-solid inspection sheets')
