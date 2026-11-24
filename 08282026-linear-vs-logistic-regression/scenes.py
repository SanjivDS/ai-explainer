"""Native schematic scenes for Linear vs. Logistic Regression."""
from manim import *
import numpy as np

BG=ManimColor("#F2F0E9"); INK=ManimColor("#3D3929"); ACC=ManimColor("#D97757")
SOFT=ManimColor("#777261"); GHOST=ManimColor("#B9B4A4")

def txt(s,n=32,c=INK,w="NORMAL"):
    return Text(s,font_size=n,color=c,weight=w)
def spark(s):
    return VGroup(Text("✦",font_size=28,color=ACC),Text(s,font="EB Garamond",font_size=38,color=INK)).arrange(RIGHT,buff=.2).to_edge(UP,buff=.75).to_edge(LEFT,buff=.9)
def box(label,w=3.2,h=1.35):
    r=RoundedRectangle(width=w,height=h,corner_radius=.16,color=GHOST,stroke_width=2)
    return VGroup(r,txt(label,30).move_to(r))

class B01_SharedSkeleton(Scene):
    def construct(self):
        self.camera.background_color=BG
        chips=VGroup(*[box(x,2.4,1.05) for x in ("size","income","history")]).arrange(DOWN,buff=.28).shift(LEFT*4)
        score=box("weighted score",3.4,1.6)
        num=box("$420k",2.8,1.6).shift(RIGHT*4+UP*1.45)
        prob=box("0.82 yes",2.8,1.6).shift(RIGHT*4+DOWN*1.45)
        arrows=VGroup(*[Arrow(c.get_right(),score.get_left(),buff=.15,color=SOFT) for c in chips])
        fork=VGroup(Arrow(score.get_right(),num.get_left(),buff=.15,color=SOFT),Arrow(score.get_right(),prob.get_left(),buff=.15,color=ACC))
        body=VGroup(chips,score,num,prob,arrows,fork).scale(1.10).stretch(1.20,1)
        self.play(FadeIn(spark("Same score. Different output.")),FadeIn(chips),Create(arrows),run_time=2)
        self.play(FadeIn(score),Create(fork),run_time=2); self.play(FadeIn(num),FadeIn(prob),run_time=1.5); self.wait(2)

class B02_TargetGate(Scene):
    def construct(self):
        self.camera.background_color=BG
        q=box("What kind of target?",4.2,1.45).shift(UP*2.15)
        left=box("CONTINUOUS\nprice · demand · temperature",5.2,2.25).shift(LEFT*3+DOWN*.35)
        right=box("CATEGORY\nchurn · fraud · approve",5.2,2.25).shift(RIGHT*3+DOWN*.35)
        a1=Arrow(q.get_bottom()+LEFT*.6,left.get_top(),buff=.15,color=SOFT); a2=Arrow(q.get_bottom()+RIGHT*.6,right.get_top(),buff=.15,color=ACC)
        footer=txt("probability  →  threshold  →  decision",38,ACC,"BOLD").to_edge(DOWN,buff=.7)
        self.play(FadeIn(spark("Choose from the target.")),FadeIn(q),run_time=1.2)
        self.play(Create(a1),FadeIn(left),run_time=1.5); self.play(Create(a2),FadeIn(right),run_time=1.5); self.play(Write(footer)); self.wait(2)

class B03_LinearExample(Scene):
    def construct(self):
        self.camera.background_color=BG
        ax=Axes(x_range=[0,10,1],y_range=[0,8,1],x_length=11,y_length=5.2,axis_config={"color":GHOST,"include_tip":False,"include_numbers":False}).shift(DOWN*.5)
        pts=[(1,1.4),(2,2.0),(3,2.4),(4,3.7),(5,3.8),(6,5.0),(7,5.1),(8,6.6)]
        dots=VGroup(*[Dot(ax.c2p(x,y),radius=.08,color=INK) for x,y in pts])
        line=ax.plot(lambda x:.67*x+.65,x_range=[.6,9.4],color=INK,stroke_width=5)
        residuals=VGroup(*[Line(ax.c2p(x,y),ax.c2p(x,.67*x+.65),color=ACC,stroke_width=3) for x,y in pts])
        new=Dot(ax.c2p(7.5,.67*7.5+.65),radius=.14,color=ACC)
        warning=txt("extrapolation needs evidence",34,ACC,"BOLD").to_edge(DOWN,buff=.55)
        self.play(FadeIn(spark("Fit the quantity.")),Create(ax),FadeIn(dots),run_time=2)
        self.play(Create(line),run_time=1.5); self.play(Create(residuals),run_time=1.5); self.play(FadeIn(new),Write(warning)); self.wait(2)

class B04_LogisticExample(Scene):
    def construct(self):
        self.camera.background_color=BG
        ax=Axes(x_range=[-6,6,1],y_range=[0,1.2,.2],x_length=11,y_length=5.1,axis_config={"color":GHOST,"include_tip":False,"include_numbers":False}).shift(DOWN*.45)
        raw=ax.plot(lambda x:.12*x+.5,x_range=[-5.3,5.3],color=SOFT,stroke_width=4)
        sig=ax.plot(lambda x:1/(1+np.exp(-x)),x_range=[-5.3,5.3],color=INK,stroke_width=6)
        band=VGroup(DashedLine(ax.c2p(-5.4,0),ax.c2p(5.4,0),color=GHOST),DashedLine(ax.c2p(-5.4,1),ax.c2p(5.4,1),color=GHOST))
        threshold=DashedLine(ax.c2p(-5.4,.5),ax.c2p(5.4,.5),color=ACC,stroke_width=4)
        self.play(FadeIn(spark("Bound the probability.")),Create(ax),Create(band),Create(raw),run_time=2)
        threshold_label=txt("0.5 threshold",34,ACC,"BOLD").move_to([-4.25,1.9,0])
        self.play(Transform(raw,sig),run_time=2); self.play(Create(threshold),Write(threshold_label)); self.wait(2)

class B05_Losses(Scene):
    def construct(self):
        self.camera.background_color=BG
        panels=VGroup(*[RoundedRectangle(width=5.6,height=5.2,corner_radius=.2,stroke_opacity=0,fill_color=GHOST,fill_opacity=.10) for _ in range(2)]).arrange(RIGHT,buff=.5).shift(DOWN*.35)
        heads=VGroup(txt("LINEAR · SQUARED ERROR",28,INK,"BOLD").move_to([-3,1.35,0]),txt("LOGISTIC · LOG LOSS",28,INK,"BOLD").move_to([3,1.35,0]))
        residuals=VGroup(*[Line([-4.5+i*.8,-.9,0],[-4.5+i*.8,-.9+h,0],color=ACC if i==3 else SOFT,stroke_width=5) for i,h in enumerate((.5,1,1.5,2.2,1.1))])
        probs=VGroup(*[box(x,1.5,.82) for x in ("0.9 ✓","0.8 ✓","0.1 ✕")]).arrange(DOWN,buff=.22).move_to([3,-.2,0])
        penalty=txt("confident + wrong = steep penalty",25,ACC,"BOLD").move_to([3,-2.55,0])
        self.play(FadeIn(spark("Different output, different loss.")),Create(panels),Write(heads),run_time=2)
        self.play(Create(residuals),run_time=1.3); self.play(FadeIn(probs),Write(penalty),run_time=1.5); self.wait(8)

class B06_StressTest(Scene):
    def construct(self):
        self.camera.background_color=BG
        cards=VGroup(*[RoundedRectangle(width=5.45,height=2.25,corner_radius=.18,color=GHOST,stroke_width=2) for _ in range(4)]).arrange_in_grid(rows=2,cols=2,buff=.38).shift(DOWN*.35)
        labels=("CURVE\nDoes a line miss the shape?","CALIBRATION\nDoes 0.8 mean about 80%?","THRESHOLD\nWhat do errors cost?","CAUSATION\nPrediction is not a cause.")
        copy=VGroup(*[txt(s,29,INK,"BOLD").move_to(c) for s,c in zip(labels,cards)])
        self.play(FadeIn(spark("Stress-test the shortcut.")),Create(cards),run_time=1.5)
        for i,t in enumerate(copy):
            self.play(Write(t),run_time=.65)
        marks=VGroup(*[Line(c.get_corner(DL)+RIGHT*.25+UP*.25,c.get_corner(DR)+LEFT*.25+UP*.25,color=ACC,stroke_width=5) for c in cards])
        self.play(Create(marks),run_time=1.2); self.wait(8)

class B07_Verdict(Scene):
    def construct(self):
        self.camera.background_color=BG
        board=RoundedRectangle(width=11.7,height=5.8,corner_radius=.22,color=GHOST,fill_color=WHITE,fill_opacity=.72,stroke_width=2).shift(DOWN*.25)
        title=txt("Choose from the target",54,INK,"BOLD").move_to(board.get_top()+DOWN*.65)
        rows=(("LINEAR","predict a continuous quantity"),("LOGISTIC","predict class probability"),("CHOICE","target first, then the decision"),("CHECK","assumptions and held-out data"))
        self.play(FadeIn(spark("The verdict.")),Create(board),Write(title),run_time=1.5)
        for i,(head,body) in enumerate(rows):
            y=.65-i*1.05
            tag=txt(head,29,ACC,"BOLD").move_to([-4.45,y,0]); copy=txt(body,34).move_to([.45,y,0])
            rule=Line([-5.35,y-.42,0],[5.35,y-.42,0],color=GHOST,stroke_width=2)
            self.play(Create(rule),Write(tag),Write(copy),run_time=.8)
        self.wait(8)

class B09_Outro(Scene):
    def construct(self):
        self.camera.background_color=BG
        field=RoundedRectangle(width=12.0,height=6.25,corner_radius=.28,color=INK,fill_color=INK,fill_opacity=.98,stroke_width=0)
        mark=Text("NBB",font="EB Garamond",font_size=116,color=ACC,weight="BOLD").shift(UP*1.7)
        title=Text("Linear vs. Logistic\nRegression.",font="EB Garamond",font_size=72,color=BG,weight="BOLD",line_spacing=.85).shift(UP*.05)
        rule=Line(LEFT*3.8+DOWN*1.15,RIGHT*3.8+DOWN*1.15,color=ACC,stroke_width=5)
        handle=txt("@NikBearBrown",38,BG,"BOLD").shift(DOWN*1.75)
        self.play(FadeIn(field),FadeIn(mark,scale=.75),run_time=1)
        self.play(Write(title),Create(rule),run_time=1.4); self.play(Write(handle),run_time=.8); self.wait(5)
