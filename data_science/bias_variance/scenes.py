"""Native Manim concept scenes for Bias vs. Variance, Oversimplified.

All plots are schematic: no fabricated values or performance claims.  Cream
ground, warm ink, and one terracotta focus per beat mirror the Claude skin.
"""
from manim import *
import numpy as np

BG = ManimColor("#F2F0E9")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
SOFT = ManimColor("#777261")
GHOST = ManimColor("#B9B4A4")

def label(text, size=30, color=INK, weight="NORMAL"):
    return Text(text, font_size=size, color=color, weight=weight)

def spark(text):
    return VGroup(Text("✦", font_size=28, color=ACC), Text(text, font="EB Garamond", font_size=38, color=INK)).arrange(RIGHT, buff=.22).to_edge(UP, buff=.82).to_edge(LEFT, buff=.9)

def axes():
    return Axes(x_range=[0, 10, 1], y_range=[0, 6, 1], x_length=11.6, y_length=5.2,
                axis_config={"color": GHOST, "include_tip": False, "include_numbers": False, "stroke_width": 2}).shift(DOWN*.45)

def truth(x): return .065*(x-5)**2 + 1.15
def dots(ax, offsets=(.30,-.20,.18,-.30,.15,-.16,.28,-.14)):
    xs = [1.1,2.1,3.2,4.2,5.25,6.3,7.45,8.65]
    return VGroup(*[Dot(ax.c2p(x, truth(x)+d), radius=.075, color=INK) for x,d in zip(xs,offsets)])

class B01_BigIdea(Scene):
    def construct(self):
        self.camera.background_color=BG; ax=axes(); s=spark("Learn signal, not noise.")
        curve=ax.plot(truth, x_range=[.7,9.3], color=SOFT, stroke_width=4)
        pts=dots(ax); self.play(FadeIn(s), Create(ax), Create(curve), FadeIn(pts), run_time=2)
        rigid=Line(ax.c2p(1,3.45), ax.c2p(9,1.55), color=INK, stroke_width=5)
        wiggle=ax.plot(lambda x: truth(x)+.45*np.sin(5*x), x_range=[.85,9.1], color=ACC, stroke_width=4)
        calm=ax.plot(lambda x: .075*(x-5)**2+1.22, x_range=[.85,9.1], color=INK, stroke_width=6)
        left=label("too rigid",30).next_to(ax.c2p(1.2,4.8),RIGHT); right=label("too reactive",30,ACC).next_to(ax.c2p(6.5,4.75),RIGHT)
        self.play(Create(rigid), Write(left), run_time=2); self.play(Create(wiggle), Write(right), run_time=2)
        self.play(FadeOut(rigid), FadeOut(wiggle), FadeOut(left), FadeOut(right), Create(calm), run_time=2)
        self.play(Write(label("useful flexibility",36,ACC,"BOLD").next_to(ax.c2p(5,5.25),UP)), run_time=1); self.wait(2)

class B02_TwoFailures(Scene):
    def construct(self):
        self.camera.background_color=BG; self.play(FadeIn(spark("Consistent or jumpy.")))
        panels=VGroup(*[RoundedRectangle(width=5.7,height=5.5,corner_radius=.18,color=GHOST,stroke_width=2) for _ in range(2)]).arrange(RIGHT,buff=.5).shift(DOWN*.45)
        titles=VGroup(label("BIAS",42,INK,"BOLD"),label("VARIANCE",42,ACC,"BOLD")).arrange(RIGHT,buff=3.55).move_to(panels.get_center()+UP*2.25)
        self.play(Create(panels),Write(titles),run_time=1.5)
        for i in range(3):
            y=1.2-i*1.4
            a=Line([-5.4,y-.15,0],[-.5,y+.15,0],color=SOFT,stroke_width=3); b=Line([.55,y-.35,0],[5.35,y+.35,0],color=ACC,stroke_width=3+2*i)
            self.play(Create(a),Create(b),run_time=.65)
        self.play(Write(label("consistently wrong",28).move_to([-3,-3.05,0])),Write(label("changes too much",28,ACC).move_to([3,-3.05,0])),run_time=1); self.wait(2)

class B03_HighBias(Scene):
    def construct(self):
        self.camera.background_color=BG; ax=axes(); self.play(FadeIn(spark("Too rigid.")),Create(ax))
        t=ax.plot(truth,x_range=[.7,9.3],color=SOFT,stroke_width=4); p=dots(ax)
        ruler=Line(ax.c2p(1,3.55),ax.c2p(9,1.7),color=INK,stroke_width=6)
        self.play(Create(t),FadeIn(p),Create(ruler),run_time=2)
        gaps=VGroup(DashedLine(ax.c2p(1.5,truth(1.5)),ax.c2p(1.5,3.43),color=ACC),DashedLine(ax.c2p(8.2,truth(8.2)),ax.c2p(8.2,1.87),color=ACC))
        self.play(Create(gaps),Write(label("underfit — too rigid",42,ACC,"BOLD").move_to([0, 1.85, 0])),run_time=2); self.wait(2)

class B04_HighVariance(Scene):
    def construct(self):
        self.camera.background_color=BG; ax=axes(); self.play(FadeIn(spark("Perfect fit, fragile guess.")),Create(ax))
        p=dots(ax); self.play(FadeIn(p),run_time=1)
        a=ax.plot(lambda x: truth(x)+.38*np.sin(5.1*x),x_range=[.8,9.1],color=INK,stroke_width=5)
        train_label=label("training: perfect",32).move_to([0,1.85,0])
        self.play(Create(a),Write(train_label),run_time=2)
        new=Dot(ax.c2p(6.3,truth(6.3)+.55),radius=.11,color=ACC); b=ax.plot(lambda x: truth(x)+.58*np.sin(4.0*x+.7),x_range=[.8,9.1],color=ACC,stroke_width=5)
        self.play(Transform(p[5],new),Transform(a,b),run_time=2)
        self.play(Transform(train_label,label("one changed point → new story",36,ACC,"BOLD").move_to([0,1.85,0])),run_time=1); self.wait(2)

class B05_Validation(Scene):
    def construct(self):
        self.camera.background_color=BG; ax=axes(); self.play(FadeIn(spark("Let validation judge.")),Create(ax))
        train=ax.plot(lambda x: 4.8-.35*x+.012*x*x,x_range=[.7,9.2],color=SOFT,stroke_width=5)
        valid=ax.plot(lambda x: .12*(x-4.8)**2+1.05,x_range=[.7,9.2],color=INK,stroke_width=6)
        self.play(Create(train),Write(label("training error",30,SOFT).move_to([-3.4,1.85,0])),run_time=1.5)
        self.play(Create(valid),Write(label("validation error",30).move_to([2.4,1.85,0])),run_time=1.5)
        dot=Dot(ax.c2p(4.8,1.05),radius=.13,color=ACC); arrow=Arrow(dot.get_center()+UP*.9,dot.get_center()+UP*.12,color=ACC,stroke_width=5)
        self.play(FadeIn(dot),GrowArrow(arrow),Write(label("choose here",38,ACC,"BOLD").next_to(arrow,UP)),run_time=1.5); self.wait(2)

class B06_Levers(Scene):
    def construct(self):
        self.camera.background_color=BG; self.play(FadeIn(spark("Diagnose, then intervene.")))
        title=label("The tradeoff is a diagnostic.",48,INK,"BOLD").shift(UP*2.25); self.play(Write(title))
        cards=VGroup(*[RoundedRectangle(width=3.7,height=2.65,corner_radius=.18,color=GHOST,stroke_width=2) for _ in range(3)]).arrange(RIGHT,buff=.4).shift(DOWN*.25)
        names=VGroup(*[label(txt,35).move_to(card.get_center()+UP*.45) for txt,card in zip(("More data","Regularize","Better features"),cards)])
        notes=VGroup(*[label(txt,25,SOFT).move_to(card.get_center()+DOWN*.45) for txt,card in zip(("steady the fit","smooth the fit","see the signal"),cards)])
        self.play(Create(cards),Write(names),Write(notes),run_time=2)
        underlines=VGroup(*[Line(card.get_bottom()+UP*.3+LEFT*.8, card.get_bottom()+UP*.3+RIGHT*.8, color=ACC, stroke_width=5) for card in cards])
        self.play(Create(underlines),run_time=1.2)
        line=label("Measure the validation behavior.",44,ACC,"BOLD").to_edge(DOWN,buff=.82); self.play(Write(line),run_time=1.2); self.wait(2)

class B07_Verdict(Scene):
    def construct(self):
        self.camera.background_color=BG; self.play(FadeIn(spark("The verdict.")))
        board=RoundedRectangle(width=11.4,height=5.35,corner_radius=.22,color=GHOST,stroke_width=2).shift(DOWN*.35)
        title=label("What survives the test?",54,INK,"BOLD").move_to(board.get_top()+DOWN*.65)
        rows=[("Bias", "consistently misses the pattern."),("Variance","lets the sample write the answer."),("Target","what generalizes to unseen data.")]
        self.play(Create(board),Write(title),run_time=1.5)
        for i,(head,body) in enumerate(rows):
            y=.65-i*1.25
            tag=label(head,32,ACC,"BOLD").move_to([-4.4,y,0]); txt=label(body,34).move_to([.35,y,0])
            rule=Line([-5.35,y-.48,0],[5.35,y-.48,0],color=GHOST,stroke_width=2)
            self.play(Create(rule),Write(tag),Write(txt),run_time=1.1)
        self.wait(2)

class B09_Outro(Scene):
    def construct(self):
        self.camera.background_color=BG
        field=RoundedRectangle(width=11.7,height=6.1,corner_radius=.3,color=INK,fill_color=INK,fill_opacity=.96,stroke_width=0).shift(DOWN*.05)
        sparkmark=Text("✦",font_size=88,color=ACC).shift(UP*1.55)
        title=Text("Bias vs. Variance.",font="EB Garamond",font_size=76,color=BG,weight="BOLD").shift(UP*.35)
        handle=label("@NikBearBrown",36,BG,"BOLD").shift(DOWN*1.15)
        rule=Line(LEFT*3.6+DOWN*.55,RIGHT*3.6+DOWN*.55,color=ACC,stroke_width=5)
        self.play(FadeIn(field),FadeIn(sparkmark,scale=.7),run_time=1)
        self.play(Write(title),Create(rule),run_time=1.2); self.play(Write(handle),run_time=.7); self.wait(2)
