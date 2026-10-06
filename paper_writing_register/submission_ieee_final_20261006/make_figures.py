import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
out=Path("figures")
out.mkdir(exist_ok=True)

geoms=["G01","G02","G03","G04"]
vp=[.92,.99,.94,.99]
s2c=[1.0,.97,.86,.95]
p2r=[1.0,1.0,.81,1.0]

fig,ax=plt.subplots(figsize=(5.2,2.8))
x=np.arange(4)
for y,label,marker in zip([vp,s2c,p2r],["Vis-Poly","S2C","P2R"],["o","s","^"]):
    ax.plot(x,y,marker=marker,label=label)
ax.set_xticks(x,geoms)
ax.set_ylim(.75,1.02)
ax.set_ylabel("Completion rate")
ax.set_xlabel("Geometry")
ax.grid(True,axis="y",alpha=.25)
ax.legend(ncol=3,fontsize=7,loc="lower left")
fig.tight_layout()
fig.savefig(out/"controller_completion.pdf",bbox_inches="tight")
plt.close(fig)

vp_r=[13.580956,17.939653,24.022424,20.577117]
s2c_r=[10.895183,17.274716,25.020928,20.070804]
p2r_r=[12.167485,18.113593,24.625614,20.796109]
fig,ax=plt.subplots(figsize=(5.2,2.8))
for y,label,marker in zip([vp_r,s2c_r,p2r_r],["Vis-Poly","S2C","P2R"],["o","s","^"]):
    ax.plot(x,y,marker=marker,label=label)
ax.set_xticks(x,geoms)
ax.set_ylabel("Mean resets / 100 m")
ax.set_xlabel("Geometry")
ax.grid(True,axis="y",alpha=.25)
ax.legend(ncol=3,fontsize=7,loc="upper left")
fig.tight_layout()
fig.savefig(out/"controller_reset_burden.pdf",bbox_inches="tight")
plt.close(fig)

fig,ax=plt.subplots(figsize=(4.8,2.8))
labels=["Vis-Poly","S2C","P2R"]
y=[251.448,2.022,3.938]
ax.bar(labels,y)
ax.set_ylabel("Median decision cost (us)")
ax.set_yscale("log")
ax.grid(True,axis="y",alpha=.25)
fig.tight_layout()
fig.savefig(out/"controller_cost.pdf",bbox_inches="tight")
plt.close(fig)

fig,ax=plt.subplots(figsize=(5.6,3.5))
ax.axis("off")
boxes=[
    (0.05,.78,.9,.15,"Verified evidence-library records\nn=174"),
    (0.05,.56,.9,.15,"After exact DOI deduplication\nCanonical reports n=173"),
    (0.05,.34,.9,.15,"Reports retrieved and assessed\nn=171"),
    (0.05,.08,.42,.17,"Direct eligible VR/XR\nn=165"),
    (.53,.08,.42,.17,"Supporting/context\nn=6")
]
from matplotlib.patches import FancyBboxPatch
for bx,by,bw,bh,t in boxes:
    p=FancyBboxPatch((bx,by),bw,bh,boxstyle="round,pad=0.01",fill=False,linewidth=1.0)
    ax.add_patch(p)
    ax.text(bx+bw/2,by+bh/2,t,ha="center",va="center",fontsize=9)
ax.annotate("",xy=(.5,.71),xytext=(.5,.78),arrowprops=dict(arrowstyle="->"))
ax.annotate("",xy=(.5,.49),xytext=(.5,.56),arrowprops=dict(arrowstyle="->"))
ax.annotate("",xy=(.29,.25),xytext=(.5,.34),arrowprops=dict(arrowstyle="->"))
ax.annotate("",xy=(.74,.25),xytext=(.5,.34),arrowprops=dict(arrowstyle="->"))
ax.text(.98,.45,"Reports not retrieved\nn=2",ha="right",va="center",fontsize=8)
ax.annotate("",xy=(.88,.44),xytext=(.95,.49),arrowprops=dict(arrowstyle="->"))
fig.tight_layout()
fig.savefig(out/"evidence_flow.pdf",bbox_inches="tight")
plt.close(fig)
