"""Native Manim scenes for PCA — Dimensionality Reduction Explained Visually."""
from contextlib import contextmanager
from pathlib import Path
import numpy as np
from manim import *

try:
    from manim import register_font
except (ImportError, ModuleNotFoundError):
    @contextmanager
    def register_font(_):
        yield

BG=ManimColor("#FAF9F5"); INK=ManimColor("#3D3929"); ACC=ManimColor("#D97757")
WARN=ManimColor("#A44A32"); SOFT=ManimColor("#6E6A57"); PALE=ManimColor("#DED9CC"); WHITE=ManimColor("#FFFDF8")
SERIF="EB Garamond"
PTS=np.array([[-2.8,-1.55],[-2.25,-1.0],[-1.9,-1.18],[-1.35,-.48],[-.85,-.62],[-.35,.05],[.1,-.08],[.55,.48],[1.05,.36],[1.55,1.02],[2.05,.88],[2.55,1.55]])

def _font():
    for parent in (Path.cwd(),*Path(__file__).resolve().parents):
        p=parent/"runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"
        if p.exists(): return p
    return Path.cwd()/"runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"

def txt(v,size=34,color=INK,weight="NORMAL"):
    if color == ACC and v != "✦": color = INK
    with register_font(_font()): return Text(v,font=SERIF,font_size=size,color=color,weight=weight)

def spark(v): return VGroup(txt("✦",28,ACC),txt(v,40)).arrange(RIGHT,buff=.22).to_edge(UP,buff=.55).to_edge(LEFT,buff=.82)
def wordmark(): return txt("@sanjiv",24,SOFT).to_edge(RIGHT,buff=.82).to_edge(DOWN,buff=.48).set_opacity(.68)

def clock(scene,actual):
    factor=actual/10.0; old_play,old_wait=scene.play,scene.wait
    def play(*a,**k): k["run_time"]=k.get("run_time",1.0)*factor; return old_play(*a,**k)
    def wait(d=1.0,*a,**k): return old_wait(d*factor,*a,**k)
    scene.play,scene.wait=play,wait

def card(label,sub="",width=3.2,height=1.2,color=INK):
    box=RoundedRectangle(width=width,height=height,corner_radius=.14,color=PALE,stroke_width=4,fill_color=WHITE,fill_opacity=.97)
    copy=VGroup(txt(label,29,color,"BOLD"),*( [txt(sub,20,SOFT)] if sub else [])).arrange(DOWN,buff=.06)
    if copy.width>width-.3: copy.scale_to_fit_width(width-.3)
    return VGroup(box,copy.move_to(box))

def cloud(origin=ORIGIN,scale=.85):
    origin=np.array(origin,dtype=float)
    dots=VGroup(*[Dot(np.array([x*scale,y*scale,0.0])+origin,radius=.095,color=INK) for x,y in PTS])
    return dots

class Base(Scene):
    actual_duration=20
    def setup(self): self.camera.background_color=BG; clock(self,self.actual_duration); self.add(wordmark())

class B01_Scene(Base):
    actual_duration=22.72
    def construct(self):
        self.play(FadeIn(spark("Rotate, then compress.")),run_time=.45)
        cols=VGroup(*[RoundedRectangle(width=.42,height=3.2,corner_radius=.08,color=PALE,fill_color=WHITE,fill_opacity=1) for _ in range(8)]).arrange(RIGHT,buff=.12).move_to([-3.7,-.1,0])
        labels=VGroup(*[txt(f"x{i+1}",20,SOFT,"BOLD").move_to(c) for i,c in enumerate(cols)])
        self.play(LaggedStart(*[FadeIn(x,shift=UP*.12) for x in VGroup(cols,labels)],lag_ratio=.03),run_time=.75)
        axes=VGroup(Line(LEFT*2.3,RIGHT*2.3,color=INK),Line(DOWN*1.55,UP*1.55,color=INK)).move_to([3.35,-.1,0])
        dots=cloud([3.35,-.1,0],.7)
        self.play(Create(axes),FadeIn(dots),run_time=.75)
        pc1=Arrow([1.35,-1.55,0],[5.35,1.35,0],buff=0,color=ACC,stroke_width=7)
        pc2=Arrow([4.15,-1.3,0],[2.55,1.1,0],buff=0,color=WARN,stroke_width=5)
        self.play(GrowArrow(pc1),GrowArrow(pc2),run_time=.8)
        kept=VGroup(card("PC1","most variance",2.15,1.0,ACC),card("PC2","next, orthogonal",2.15,1.0,INK)).arrange(RIGHT,buff=.3).move_to([-3.7,-1.9,0])
        self.play(FadeOut(cols[2:]),FadeOut(labels[2:]),FadeIn(kept),run_time=.8)
        self.wait(4.0)

class B02_Scene(Base):
    actual_duration=21.23
    def construct(self):
        self.play(FadeIn(spark("Five moves, one projection.")),run_time=.45)
        stages=VGroup(*[card(a,b,2.25,1.2,c) for a,b,c in [
            ("1  CENTER","subtract means",ACC),("2  FIND PC1","maximum spread",INK),("3  FIND PC2","stay orthogonal",INK),("4  ROTATE","new coordinates",INK),("5  KEEP k","drop the rest",ACC)
        ]]).arrange(RIGHT,buff=.22).scale(.92).move_to([0,.55,0])
        for s in stages: self.play(FadeIn(s,shift=UP*.12),run_time=.42)
        line=Line(stages[0].get_bottom()+DOWN*.45,stages[-1].get_bottom()+DOWN*.45,color=PALE,stroke_width=7)
        pulse=Dot(line.get_left(),radius=.13,color=ACC)
        self.play(Create(line),FadeIn(pulse),run_time=.45)
        self.play(pulse.animate.move_to(line.get_right()),run_time=1.05)
        footer=txt("CENTER  →  FIND  →  ROTATE  →  PROJECT  →  CHOOSE k",31,SOFT,"BOLD").to_edge(DOWN,buff=.85)
        self.play(FadeIn(footer),run_time=.5); self.wait(3.5)

class B03_Scene(Base):
    actual_duration=20.07
    def construct(self):
        self.play(FadeIn(spark("Two coordinates become one.")),run_time=.45)
        axes=Axes(x_range=[-4,4,1],y_range=[-3,3,1],x_length=8,y_length=5,axis_config={"color":SOFT,"include_tip":False}).move_to([-1.1,-.3,0])
        dots=cloud([-1.1,-.3,0],1.05)
        self.play(Create(axes),FadeIn(dots),run_time=.75)
        p1=Line([-4.8,-2.9,0],[2.7,2.6,0],color=ACC,stroke_width=7)
        p2=Line([-2.0,-2.55,0],[-.2,.05,0],color=WARN,stroke_width=5)
        self.play(Create(p1),Create(p2),run_time=.75)
        unit=np.array([1,.73,0]); unit=unit/np.linalg.norm(unit); origin=np.array([-1.1,-.3,0])
        guides=VGroup(); projected=VGroup()
        for d in dots:
            v=d.get_center()-origin; q=origin+np.dot(v,unit)*unit
            guides.add(DashedLine(d.get_center(),q,color=PALE,dash_length=.08)); projected.add(Dot(q,radius=.09,color=ACC))
        self.play(LaggedStart(*[Create(g) for g in guides],lag_ratio=.04),FadeIn(projected),run_time=1.0)
        badge=card("2D TO 1D","keep only the PC1 score",3.25,1.2,ACC).move_to([4.8,-1.45,0])
        self.play(FadeIn(badge,scale=.9),run_time=.55); self.wait(4.0)

class B04_Scene(Base):
    actual_duration=23.59
    def construct(self):
        self.play(FadeIn(spark("The algebra finds the axes.")),run_time=.45)
        centered=card("CENTERED MATRIX","Xc = X − feature means",3.8,1.25,INK).move_to([-4.2,1.0,0])
        svd=txt("Xc  =  U  Σ  Vᵀ",44,INK,"BOLD").move_to([0,1.0,0])
        axes=card("COLUMNS OF V","principal directions",3.8,1.25,ACC).move_to([4.2,1.0,0])
        self.play(FadeIn(centered),run_time=.6); self.play(Write(svd),run_time=.8); self.play(FadeIn(axes),run_time=.6)
        a1=Arrow(centered.get_right(),svd.get_left(),buff=.18,color=PALE); a2=Arrow(svd.get_right(),axes.get_left(),buff=.18,color=ACC)
        self.play(GrowArrow(a1),GrowArrow(a2),run_time=.6)
        variance=card("MAXIMIZE","retained variance",4.3,1.3,ACC).move_to([-2.55,-1.05,0])
        error=card("MINIMIZE","squared reconstruction error",4.3,1.3,WARN).move_to([2.55,-1.05,0])
        self.play(FadeIn(variance),FadeIn(error),run_time=.75)
        eq=txt("SAME RANK-k LINEAR SUBSPACE",30,SOFT,"BOLD").to_edge(DOWN,buff=.65)
        self.play(FadeIn(eq),run_time=.5); self.wait(4.0)

class B05_Scene(Base):
    actual_duration=22.93
    def construct(self):
        self.play(FadeIn(spark("Rotation is not reduction.")),run_time=.45)
        raw=VGroup(*[card(f"x{i+1}","original",1.0,1.05,INK) for i in range(10)]).arrange(RIGHT,buff=.12).scale(.9).move_to([0,1.3,0])
        pcs=VGroup(*[card(f"PC{i+1}","score",1.0,1.05,ACC if i<2 else INK) for i in range(10)]).arrange(RIGHT,buff=.12).scale(.9).move_to([0,-.15,0])
        self.play(LaggedStart(*[FadeIn(x) for x in raw],lag_ratio=.03),run_time=.75)
        self.play(TransformFromCopy(raw,pcs),run_time=.9)
        count=txt("10 dimensions",37,INK,"BOLD").move_to([0,-1.3,0]); self.play(FadeIn(count),run_time=.45)
        self.play(FadeOut(pcs[2:]),Transform(count,txt("2 dimensions",37,ACC,"BOLD").move_to(count)),run_time=.85)
        note=txt("PC SCORES ARE WEIGHTED COMBINATIONS — NOT SELECTED COLUMNS",25,SOFT,"BOLD").to_edge(DOWN,buff=1.05)
        self.play(FadeIn(note),run_time=.5); self.wait(4.0)

class B06_Scene(Base):
    actual_duration=23.23
    def construct(self):
        self.play(FadeIn(spark("Choose k for the task.")),run_time=.45)
        vals=[.34,.24,.16,.10,.07,.04,.025,.015]
        bars=VGroup(*[Rectangle(width=.65,height=4*v/.34,color=ACC if i<3 else PALE,fill_color=ACC if i<3 else PALE,fill_opacity=.85).align_to(ORIGIN,DOWN) for i,v in enumerate(vals)]).arrange(RIGHT,buff=.25,aligned_edge=DOWN).move_to([-2.8,-.35,0])
        self.play(LaggedStart(*[GrowFromEdge(b,DOWN) for b in bars],lag_ratio=.08),run_time=1.0)
        labels=VGroup(*[txt(f"PC{i+1}",18,SOFT,"BOLD").next_to(b,DOWN,buff=.12) for i,b in enumerate(bars)])
        self.play(FadeIn(labels),run_time=.45)
        cum=np.cumsum(vals); pts=[[-5.95+i*.9,-1.55+3.4*c,0] for i,c in enumerate(cum)]
        curve=VMobject(color=WARN,stroke_width=6).set_points_smoothly(pts); self.play(Create(curve),run_time=.85)
        tasks=VGroup(card("VISUALIZE","try k = 2",3.25,1.15,ACC),card("ANOMALY CHECK","test more detail",3.25,1.15,INK),card("MODEL","cross-validate",3.25,1.15,WARN)).arrange(DOWN,buff=.3).move_to([4.6,-.15,0])
        self.play(LaggedStart(*[FadeIn(t,shift=LEFT*.12) for t in tasks],lag_ratio=.16),run_time=.9); self.wait(4.0)

class B07_Scene(Base):
    actual_duration=23.36
    def construct(self):
        self.play(FadeIn(spark("Loss has a distance.")),run_time=.45)
        dots=cloud([-1.0,-.25,0],1.05); line=Line([-4.8,-2.9,0],[2.8,2.65,0],color=ACC,stroke_width=7)
        self.play(FadeIn(dots),Create(line),run_time=.75)
        unit=np.array([1,.73,0]); unit=unit/np.linalg.norm(unit); origin=np.array([-1,-.25,0]); projections=[]; residuals=VGroup()
        for d in dots:
            v=d.get_center()-origin; q=origin+np.dot(v,unit)*unit; projections.append(q); residuals.add(DashedLine(d.get_center(),q,color=WARN,dash_length=.08))
        ghosts=dots.copy().set_opacity(.28); recon=VGroup(*[Dot(q,radius=.095,color=ACC) for q in projections])
        self.play(Transform(dots,recon),run_time=.8); self.play(FadeIn(ghosts),LaggedStart(*[Create(r) for r in residuals],lag_ratio=.04),run_time=.9)
        brace=Brace(residuals,RIGHT,color=WARN); label=txt("discarded direction",27,WARN,"BOLD").next_to(brace,RIGHT,buff=.18)
        self.play(FadeIn(brace),FadeIn(label),run_time=.55)
        restore=card("ADD PC2","toy cloud restores",3.25,1.15,INK).move_to([4.75,-1.75,0]); self.play(FadeIn(restore),run_time=.5); self.wait(4.0)

class B08_Scene(Base):
    actual_duration=23.15
    def construct(self):
        self.play(FadeIn(spark("Variance can mislead.")),run_time=.45)
        scale=card("SCALE","units rotate PC1",3.6,1.15,ACC).move_to([-4.45,1.55,0])
        curve=card("SHAPE","PCA stays linear",3.6,1.15,INK).move_to([0,1.55,0])
        out=card("OUTLIER","one point pulls",3.6,1.15,WARN).move_to([4.45,1.55,0])
        self.play(FadeIn(scale),FadeIn(curve),FadeIn(out),run_time=.75)
        e1=Ellipse(width=3.2,height=.85,color=WARN,stroke_width=6).move_to([-4.45,-.2,0]); axis1=Line([-5.9,-.6,0],[-3.0,.2,0],color=INK,stroke_width=5)
        moon=Arc(radius=1.35,start_angle=.15,angle=PI-.30,color=INK,stroke_width=12).move_to([0,-.45,0]); straight=Line([-1.55,-.45,0],[1.55,-.45,0],color=WARN,stroke_width=5)
        # Schematic observations make the outlier's influence explicit; an empty
        # enclosing ellipse looked like an overlapping label in pixel inspection.
        e3=VGroup(*[Dot([x,y,0],radius=.07,color=INK) for x,y in [(3.2,-.3),(3.6,-.65),(3.9,.05),(4.3,-.7),(4.6,-.2),(5.0,-.45)]])
        odd=Dot([5.75,1.0,0],radius=.16,color=WARN); pulled=Line([3.0,-.9,0],[5.7,.95,0],color=WARN,stroke_width=5)
        self.play(Create(e1),Create(axis1),run_time=.6); self.play(Create(moon),Create(straight),run_time=.6); self.play(Create(e3),FadeIn(odd),Create(pulled),run_time=.65)
        footer=txt("INSPECT SCALE · SHAPE · OUTLIERS",31,SOFT,"BOLD").to_edge(DOWN,buff=.65)
        self.play(FadeIn(footer),run_time=.45); self.wait(3.8)
