"""Native Manim scenes for Bagging vs Boosting."""
from contextlib import contextmanager
from pathlib import Path
from manim import *

try:
    from manim import register_font
except (ImportError, ModuleNotFoundError):
    @contextmanager
    def register_font(_):
        yield

BG=ManimColor("#FAF9F5"); INK=ManimColor("#3D3929"); ACC=ManimColor("#D97757")
SOFT=ManimColor("#6E6A57"); PALE=ManimColor("#DED9CC"); WHITE=ManimColor("#FFFDF8"); WARN=ManimColor("#A44A32")
SERIF="EB Garamond"

def _font():
    for parent in (Path.cwd(), *Path(__file__).resolve().parents):
        p=parent/"runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"
        if p.exists(): return p
    return Path.cwd()/"runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"

def txt(value,size=34,color=INK,weight="NORMAL"):
    if color == ACC and value != "✦": color = INK
    with register_font(_font()): return Text(value,font=SERIF,font_size=size,color=color,weight=weight)

def spark(value):
    return VGroup(txt("✦",28,ACC),txt(value,40)).arrange(RIGHT,buff=.22).to_edge(UP,buff=.55).to_edge(LEFT,buff=.82)

def wordmark(): return txt("@sanjiv",24,SOFT).to_edge(RIGHT,buff=.82).to_edge(DOWN,buff=.48).set_opacity(.68)

def clock(scene,actual):
    factor=actual/10.0; old_play,old_wait=scene.play,scene.wait
    def play(*args,**kwargs): kwargs["run_time"]=kwargs.get("run_time",1.0)*factor; return old_play(*args,**kwargs)
    def wait(duration=1.0,*args,**kwargs): return old_wait(duration*factor,*args,**kwargs)
    scene.play,scene.wait=play,wait

def card(label,sub="",width=3.0,height=1.2,color=INK):
    box=RoundedRectangle(width=width,height=height,corner_radius=.14,color=PALE,stroke_width=4,fill_color=WHITE,fill_opacity=.97)
    lines=[txt(label,29,color,"BOLD")]
    if sub: lines.append(txt(sub,20,SOFT))
    copy=VGroup(*lines).arrange(DOWN,buff=.07)
    if copy.width>width-.3: copy.scale_to_fit_width(width-.3)
    if copy.height>height-.18: copy.scale_to_fit_height(height-.18)
    return VGroup(box,copy.move_to(box))

def tree(scale=.75,color=INK):
    root=Dot(UP*.8,radius=.1,color=color); left=Dot(DOWN*.15+LEFT*.45,radius=.1,color=color); right=Dot(DOWN*.15+RIGHT*.45,radius=.1,color=color)
    leaves=VGroup(Dot(DOWN*.95+LEFT*.72,radius=.1,color=color),Dot(DOWN*.95+LEFT*.18,radius=.1,color=color),Dot(DOWN*.95+RIGHT*.18,radius=.1,color=color),Dot(DOWN*.95+RIGHT*.72,radius=.1,color=color))
    edges=VGroup(Line(root,left,color=color),Line(root,right,color=color),Line(left,leaves[0],color=color),Line(left,leaves[1],color=color),Line(right,leaves[2],color=color),Line(right,leaves[3],color=color))
    return VGroup(edges,root,left,right,leaves).scale(scale)

class Base(Scene):
    actual_duration=20
    def setup(self): self.camera.background_color=BG; clock(self,self.actual_duration); self.add(wordmark())

class B01_Scene(Base):
    actual_duration=22.17
    def construct(self):
        self.play(FadeIn(spark("Two ways to build a team.")),run_time=.45)
        seed=tree(.9,INK).move_to([0,1.62,0]); self.play(FadeIn(seed,scale=.85),run_time=.65)
        labels=VGroup(card("BAGGING","diversify, then combine",4.7,1.15,ACC),card("BOOSTING","correct, then accumulate",4.7,1.15,INK)).arrange(RIGHT,buff=.8).move_to([0,-.2,0])
        self.play(FadeIn(labels[0],shift=LEFT*.2),FadeIn(labels[1],shift=RIGHT*.2),run_time=.8)
        bag=VGroup(tree(.48,ACC),tree(.48,ACC),tree(.48,ACC)).arrange(RIGHT,buff=.55).move_to([-3.0,-1.65,0])
        boost=VGroup(tree(.48,INK),txt("+",34,ACC,"BOLD"),tree(.48,INK),txt("+",34,ACC,"BOLD"),tree(.48,INK)).arrange(RIGHT,buff=.25).move_to([3.0,-1.65,0])
        self.play(FadeIn(bag,shift=DOWN*.15),run_time=.75); self.play(FadeIn(boost,shift=DOWN*.15),run_time=.75)
        verdict=txt("VALIDATE THE STRATEGY — NOT THE LABEL",28,SOFT,"BOLD").to_edge(DOWN,buff=.6)
        self.play(FadeIn(verdict),run_time=.45); self.wait(3.85)

class B02_Scene(Base):
    actual_duration=21.29
    def construct(self):
        self.play(FadeIn(spark("Committee versus relay.")),run_time=.45)
        split=Line(UP*2.2,DOWN*2.15,color=PALE,stroke_width=3); self.add(split)
        dataL=card("DATA","randomized views",2.4,1.0,ACC).move_to([-5.1,1.1,0])
        models=VGroup(*[card(f"M{i+1}","independent",1.8,.95,INK) for i in range(3)]).arrange(DOWN,buff=.28).move_to([-1.9,1.05,0])
        agg=card("VOTE / AVERAGE","combine once",3.0,1.1,ACC).move_to([-3.35,-1.55,0])
        self.play(FadeIn(dataL),run_time=.45)
        arrows=VGroup(*[Arrow(dataL.get_right(),m.get_left(),buff=.12,color=PALE,stroke_width=4) for m in models])
        self.play(*[GrowArrow(a) for a in arrows],FadeIn(models),run_time=.9)
        convergence=Arrow(models.get_bottom(),agg.get_top(),buff=.14,color=INK,stroke_width=5)
        self.play(GrowArrow(convergence),FadeIn(agg),run_time=.8)
        chain=VGroup(card("M1","fit",1.7,.9,INK),card("ERROR","focus",1.8,.9,ACC),card("M2","fit",1.7,.9,INK),card("ERROR","focus",1.8,.9,ACC),card("M3","fit",1.7,.9,INK)).arrange(DOWN,buff=.16).move_to([3.55,.25,0])
        links=VGroup(*[Arrow(chain[i].get_bottom(),chain[i+1].get_top(),buff=.05,color=INK,stroke_width=4) for i in range(4)])
        self.play(FadeIn(chain[0]),run_time=.35)
        for i in range(4): self.play(GrowArrow(links[i]),FadeIn(chain[i+1]),run_time=.35)
        self.wait(3.6)

class B03_Scene(Base):
    actual_duration=22.23
    def construct(self):
        self.play(FadeIn(spark("Resample. Fit. Aggregate.")),run_time=.45)
        rows=VGroup(*[card(str(i+1),"",.72,.65,ACC if i in (1,5) else INK) for i in range(8)]).arrange(RIGHT,buff=.18).move_to([0,1.75,0])
        self.play(LaggedStart(*[FadeIn(r,scale=.8) for r in rows],lag_ratio=.08),run_time=.8)
        samples=["1 2 2 4 6 6 7 8","1 1 3 4 5 7 7 8","2 3 3 4 5 5 6 8"]
        boots=VGroup(*[card(f"BOOTSTRAP {i+1}",s,3.9,1.05,ACC if i==0 else INK) for i,s in enumerate(samples)]).arrange(RIGHT,buff=.42).move_to([0,.4,0])
        self.play(LaggedStart(*[FadeIn(b,shift=DOWN*.12) for b in boots],lag_ratio=.2),run_time=.9)
        trees=VGroup(*[tree(.5,ACC if i!=1 else INK) for i in range(3)]).arrange(RIGHT,buff=2.75).move_to([0,-.9,0])
        self.play(FadeIn(trees),run_time=.65)
        votes=VGroup(card("BLUE","tree 1",2.2,.9,ACC),card("ORANGE","tree 2",2.2,.9,INK),card("BLUE","tree 3",2.2,.9,ACC)).arrange(RIGHT,buff=1.0).move_to([0,-1.85,0])
        self.play(FadeIn(votes),run_time=.65)
        result=txt("CLASSIFICATION: BLUE WINS 2–1  ·  REGRESSION: AVERAGE",26,SOFT,"BOLD").to_edge(DOWN,buff=.95)
        self.play(FadeIn(result),run_time=.45); self.wait(3.45)

class B04_Scene(Base):
    actual_duration=24.44
    def construct(self):
        self.play(FadeIn(spark("Diversity must be useful.")),run_time=.45)
        left=card("UNALIGNED ERRORS","some cancel",4.8,1.1,ACC).move_to([-3.3,1.5,0]); right=card("CORRELATED ERRORS","they stack",4.8,1.1,WARN).move_to([3.3,1.5,0])
        self.play(FadeIn(left),FadeIn(right),run_time=.7)
        originL=Dot([-3.3,.15,0],color=INK)
        free=VGroup(Arrow(originL.get_center(),[-4.7,-.7,0],buff=.08,color=INK),Arrow(originL.get_center(),[-3.2,-.95,0],buff=.08,color=ACC),Arrow(originL.get_center(),[-1.9,-.45,0],buff=.08,color=INK))
        originR=Dot([3.3,.15,0],color=INK)
        aligned=VGroup(*[Arrow(originR.get_center(),[4.7,-.55+i*.16,0],buff=.08,color=WARN) for i in range(3)])
        self.play(FadeIn(originL),*[GrowArrow(a) for a in free],run_time=.8)
        self.play(FadeIn(originR),*[GrowArrow(a) for a in aligned],run_time=.8)
        rf=card("RANDOM FOREST","bootstrap rows + random feature candidates",7.2,1.2,ACC).move_to([0,-1.55,0])
        self.play(FadeIn(rf,scale=.9),run_time=.65)
        footer=txt("MORE TREES ≠ A CURE FOR SYSTEMATIC BIAS",28,SOFT,"BOLD").to_edge(DOWN,buff=.5)
        self.play(FadeIn(footer),run_time=.45); self.wait(3.9)

class B05_Scene(Base):
    actual_duration=22.98
    def construct(self):
        self.play(FadeIn(spark("The next learner studies the miss.")),run_time=.45)
        pts=VGroup(*[Dot([-4.9+i*1.4,1.35,0],radius=.15,color=ACC if i in (2,6) else INK) for i in range(8)])
        labels=VGroup(*[txt(str(i+1),20,SOFT).next_to(p,DOWN,buff=.32) for i,p in enumerate(pts)])
        self.play(FadeIn(pts),FadeIn(labels),run_time=.65)
        rings=VGroup(*[Circle(.32,color=WARN,stroke_width=5).move_to(pts[i]) for i in (2,6)])
        self.play(Create(rings),run_time=.65)
        stages=VGroup(card("STUMP 1","misses 3 and 7",3.1,1.05,INK),card("STUMP 2","focuses on misses",3.1,1.05,ACC),card("STUMP 3","shifts attention",3.1,1.05,INK)).arrange(RIGHT,buff=.5).move_to([0,-.15,0])
        self.play(FadeIn(stages[0]),run_time=.45); self.play(FadeIn(stages[1]),run_time=.45); self.play(FadeIn(stages[2]),run_time=.45)
        weights=VGroup(card("0.5 × M1","",2.4,.85,INK),txt("+",34,ACC,"BOLD"),card("0.8 × M2","",2.4,.85,ACC),txt("+",34,ACC,"BOLD"),card("0.6 × M3","",2.4,.85,INK)).arrange(RIGHT,buff=.25).move_to([0,-1.42,0])
        self.play(FadeIn(weights,shift=UP*.12),run_time=.75)
        note=txt("GRADIENT BOOSTING: ADD LOSS-REDUCING CORRECTIONS",26,SOFT,"BOLD").to_edge(DOWN,buff=.95)
        self.play(FadeIn(note),run_time=.45); self.wait(3.6)

class B06_Scene(Base):
    actual_duration=22.66
    def construct(self):
        self.play(FadeIn(spark("Independence changes the clock.")),run_time=.45)
        bag=card("BAGGING","parallel-ready",4.4,1.0,ACC).move_to([-3.35,1.55,0]); boost=card("BOOSTING","dependency chain",4.4,1.0,INK).move_to([3.35,1.55,0])
        self.play(FadeIn(bag),FadeIn(boost),run_time=.65)
        lanes=VGroup(*[RoundedRectangle(width=4.2,height=.48,corner_radius=.1,color=PALE,fill_color=WHITE,fill_opacity=1) for _ in range(4)]).arrange(DOWN,buff=.25).move_to([-3.35,-.35,0])
        fills=VGroup(*[Rectangle(width=3.7,height=.28,color=ACC,fill_color=ACC,fill_opacity=.8,stroke_width=0).align_to(l,LEFT).move_to(l.get_center()+LEFT*.12) for l in lanes])
        self.play(FadeIn(lanes),FadeIn(fills),run_time=.75)
        chain=VGroup(*[card(f"S{i+1}","after prior",1.25,.8,INK if i%2==0 else ACC) for i in range(4)]).arrange(RIGHT,buff=.16).move_to([3.35,.15,0])
        self.play(LaggedStart(*[FadeIn(c,shift=DOWN*.1) for c in chain],lag_ratio=.25),run_time=1.0)
        costs=VGroup(card("MEMORY","many fitted models",4.4,1.0,INK),card("TUNING","rate · depth · stages · stop",4.4,1.0,ACC)).arrange(RIGHT,buff=.85).move_to([0,-2.25,0])
        self.play(FadeIn(costs),run_time=.65)
        footer=txt("COMPARE VALIDATION QUALITY + TOTAL RUNTIME",27,SOFT,"BOLD").to_edge(DOWN,buff=.48)
        self.play(FadeIn(footer),run_time=.45); self.wait(3.55)

class B07_Scene(Base):
    actual_duration=22.87
    def construct(self):
        self.play(FadeIn(spark("Ensemble is not a warranty.")),run_time=.45)
        axes=Axes(x_range=[0,10,2],y_range=[0,6,2],x_length=6.3,y_length=3.6,axis_config={"color":SOFT,"stroke_width":3,"include_tip":False}).move_to([-2.8,-.1,0])
        train=axes.plot(lambda x:4.8*.72**x+.3,x_range=[0,10],color=INK,stroke_width=6)
        val=axes.plot(lambda x:.75+.11*(x-4.5)**2,x_range=[0,10],color=WARN,stroke_width=6)
        self.play(Create(axes),run_time=.55); self.play(Create(train),Create(val),run_time=.85)
        # Compact, vertically aligned legend between the chart and callout cards.
        train_label=txt("TRAIN LOSS",12,ACC,"BOLD").move_to([.15,-.98,0])
        validation_label=txt("VALIDATION LOSS",12,WARN,"BOLD").move_to([.15,.88,0]).align_to(train_label,LEFT)
        labels=VGroup(validation_label,train_label)
        self.play(FadeIn(labels),run_time=.45)
        noise=card("MISLABELED POINT","keeps attracting correction",4.8,1.15,WARN).move_to([3.9,1.15,0])
        corr=card("CORRELATED TREES","preserve the same error",4.8,1.15,INK).move_to([3.9,-.25,0])
        guard=card("GUARDRAIL","untouched validation + learning curves",4.8,1.15,ACC).move_to([3.9,-1.65,0])
        self.play(FadeIn(noise),run_time=.55); self.play(FadeIn(corr),run_time=.55); self.play(FadeIn(guard),run_time=.55); self.wait(3.55)
