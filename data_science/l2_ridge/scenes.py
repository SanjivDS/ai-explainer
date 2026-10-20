"""Native Manim scenes for L2 Regularization, Oversimplified.

All plots and coefficient paths are schematic. No numeric performance claim is made.
"""
from manim import *
import numpy as np

BG = ManimColor("#F2F0E9")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
SOFT = ManimColor("#777261")
GHOST = ManimColor("#B9B4A4")

def txt(s, size=34, color=INK, weight="NORMAL"):
    return Text(s, font="EB Garamond", font_size=size, color=color, weight=weight)

def ui(s, size=28, color=INK, weight="NORMAL"):
    return Text(s, font_size=size, color=color, weight=weight)

def spark(s):
    return VGroup(Text("✦", font_size=28, color=ACC), txt(s, 40)).arrange(RIGHT, buff=.22).to_edge(UP, buff=.7).to_edge(LEFT, buff=1.0)

def panel(w=3.6, h=3.8):
    return RoundedRectangle(width=w, height=h, corner_radius=.18, color=GHOST, stroke_width=2)

class B01_BigIdea(Scene):
    def construct(self):
        self.camera.background_color = BG
        s = spark("Fit, with restraint.")
        beam = Line(LEFT*4.7, RIGHT*4.7, color=INK, stroke_width=7).shift(UP*.3)
        pivot = Triangle(color=INK, fill_color=INK, fill_opacity=1).scale(.28).rotate(PI).next_to(beam, DOWN, buff=.02)
        left = VGroup(txt("training error", 38, weight="BOLD"), ui("prediction mistakes", 25, SOFT)).arrange(DOWN, buff=.18).move_to([-3.2,1.25,0])
        right = VGroup(txt("squared weights", 38, weight="BOLD"), ui("coefficient penalty", 25, SOFT)).arrange(DOWN, buff=.18).move_to([3.2,1.25,0])
        self.play(FadeIn(s), Create(beam), FadeIn(pivot), Write(left), run_time=2)
        self.play(Write(right), run_time=1.4)
        bars = VGroup(*[Rectangle(width=.65, height=h, color=INK, fill_color=INK, fill_opacity=.85, stroke_width=0) for h in (2.0,1.55,1.3,.95,.7)]).arrange(RIGHT,buff=.35,aligned_edge=DOWN).shift(DOWN*2)
        dial = ValueTracker(0)
        knob = Dot(LEFT*3.4+DOWN*2.55, radius=.13, color=ACC)
        track = Line(LEFT*3.4+DOWN*2.55, LEFT*.8+DOWN*2.55, color=GHOST, stroke_width=6)
        lam = txt("λ", 48, ACC, "BOLD").next_to(track, LEFT, buff=.28)
        self.play(Create(track), FadeIn(knob), Write(lam), LaggedStart(*[GrowFromEdge(b,DOWN) for b in bars], lag_ratio=.12), run_time=2)
        targets = VGroup(*[Rectangle(width=.65, height=h*.52, color=INK, fill_color=INK, fill_opacity=.85, stroke_width=0) for h in (2.0,1.55,1.3,.95,.7)]).arrange(RIGHT,buff=.35,aligned_edge=DOWN).move_to(bars,aligned_edge=DOWN)
        self.play(knob.animate.shift(RIGHT*2.6), Transform(bars,targets), beam.animate.rotate(-.05), run_time=2)
        verdict = txt("less variance  ·  more bias", 42, ACC, "BOLD").move_to([0, 2.25, 0])
        self.play(Write(verdict), run_time=1.2); self.wait(2)

class B02_Objective(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.play(FadeIn(spark("One objective. Two demands.")))
        rss = txt("Σᵢ (yᵢ − ŷᵢ)²", 52, INK, "BOLD").shift(LEFT*3.2+UP*.65)
        plus = txt("+", 58, INK, "BOLD").shift(UP*.65)
        pen = txt("λ Σⱼ βⱼ²", 52, ACC, "BOLD").shift(RIGHT*3.2+UP*.65)
        self.play(Write(rss), run_time=1.8)
        self.play(Write(ui("FIT",30,SOFT,"BOLD").next_to(rss,DOWN,buff=.32)), Write(plus), Write(pen), run_time=2)
        self.play(Write(ui("RESTRAINT",30,ACC,"BOLD").next_to(pen,DOWN,buff=.32)), run_time=.8)
        bars = VGroup(*[Rectangle(width=.78,height=h,color=INK,fill_color=INK,fill_opacity=.88,stroke_width=0) for h in (2.1,1.7,1.25,.9)]).arrange(RIGHT,buff=.45,aligned_edge=DOWN).shift(DOWN*2)
        self.play(LaggedStart(*[GrowFromEdge(b,DOWN) for b in bars],lag_ratio=.15),run_time=1.5)
        zero = ui("λ = 0   ordinary least squares",28,SOFT).move_to([-3.8,2.05,0])
        self.play(Write(zero),run_time=1)
        small = VGroup(*[Rectangle(width=.78,height=h*.38,color=INK,fill_color=INK,fill_opacity=.88,stroke_width=0) for h in (2.1,1.7,1.25,.9)]).arrange(RIGHT,buff=.45,aligned_edge=DOWN).move_to(bars,aligned_edge=DOWN)
        self.play(Transform(zero,ui("λ ↑   large weights cost more",30,ACC,"BOLD").move_to(zero)),Transform(bars,small),run_time=2); self.wait(2)

class B03_QuadraticPenalty(Scene):
    def construct(self):
        self.camera.background_color=BG
        self.play(FadeIn(spark("The square changes the price.")))
        b1=Rectangle(width=.85,height=1.25,color=INK,fill_color=INK,fill_opacity=.9,stroke_width=0).shift(LEFT*4+UP*.7)
        one=Square(.72,color=ACC,fill_color=ACC,fill_opacity=.9,stroke_width=0).shift(LEFT*4+DOWN*1.2)
        self.play(GrowFromEdge(b1,DOWN),FadeIn(one),Write(ui("β",34).next_to(b1,UP)),run_time=1.5)
        b2=Rectangle(width=.85,height=2.5,color=INK,fill_color=INK,fill_opacity=.9,stroke_width=0).shift(LEFT*1.7+UP*1.3)
        four=VGroup(*[Square(.72,color=ACC,fill_color=ACC,fill_opacity=.9,stroke_width=0) for _ in range(4)]).arrange_in_grid(2,2,buff=.1).shift(LEFT*1.7+DOWN*1.2)
        self.play(TransformFromCopy(b1,b2),Write(ui("2β",34).next_to(b2,RIGHT,buff=.2)),TransformFromCopy(one,four),run_time=2)
        self.play(Write(txt("2× weight → 4× penalty",34,ACC,"BOLD").move_to([2.25,-1.2,0])),run_time=1.3)
        axes=Axes(x_range=[-4,4,1],y_range=[-3,3,1],x_length=7,y_length=5,axis_config={"color":GHOST,"include_tip":False,"include_numbers":False}).shift(DOWN*.25)
        circle=Circle(radius=2.15,color=ACC,stroke_width=5).move_to(axes.c2p(0,0))
        contours=VGroup(*[Ellipse(width=5.8-i*.7,height=3.5-i*.42,color=SOFT,stroke_width=2).rotate(.28).shift(RIGHT*1.1+UP*.45) for i in range(3)])
        optimum=Dot(axes.c2p(2.3,1.7),color=INK,radius=.12); chosen=Dot(circle.point_at_angle(.55),color=ACC,radius=.14)
        self.remove(*list(self.mobjects))
        self.add(spark("The L2 boundary."),axes)
        self.play(Create(contours),FadeIn(optimum),Create(circle),run_time=2)
        self.play(TransformFromCopy(optimum,chosen),Write(txt("smooth shrinkage",30,ACC,"BOLD").move_to([-4.45,2.35,0])),run_time=1.4); self.wait(2)

class B04_CorrelatedPredictors(Scene):
    def construct(self):
        self.camera.background_color=BG
        opening = spark("Same signal. Unstable credit.")
        self.play(FadeIn(opening))
        cards=VGroup(panel(3.3,4.5),panel(3.3,4.5),panel(3.3,4.5)).arrange(RIGHT,buff=.45).shift(DOWN*.25)
        heads=VGroup(txt("Sample A",38,weight="BOLD"),txt("Sample B",38,weight="BOLD"),txt("Ridge",38,ACC,"BOLD"))
        for h,c in zip(heads,cards): h.move_to([c.get_center()[0],2.35,0])
        self.play(FadeOut(opening),Create(cards),Write(heads),run_time=1.5)
        def pair(center, heights, colors):
            base=Line(center+LEFT*1.05+DOWN*1.35,center+RIGHT*1.05+DOWN*1.35,color=GHOST)
            bs=VGroup(*[Rectangle(width=.68,height=abs(h),color=col,fill_color=col,fill_opacity=.9,stroke_width=0) for h,col in zip(heights,colors)]).arrange(RIGHT,buff=.38,aligned_edge=DOWN).move_to(center+DOWN*.28,aligned_edge=DOWN)
            labs=VGroup(ui("x₁",27),ui("x₂",27)).arrange(RIGHT,buff=.72).next_to(base,DOWN,buff=.18)
            return VGroup(base,bs,labs)
        a=pair(cards[0].get_center(),(2.15,.72),(INK,ACC)); b=pair(cards[1].get_center(),(.72,2.15),(INK,ACC)); r=pair(cards[2].get_center(),(1.15,1.02),(INK,ACC))
        self.play(LaggedStart(*[FadeIn(x) for x in a],lag_ratio=.15),run_time=1.5)
        self.play(TransformFromCopy(a,b),run_time=1.5)
        flip=DoubleArrow(cards[0].get_bottom()+UP*.18,cards[1].get_bottom()+UP*.18,color=ACC,stroke_width=4)
        flip_label=ui("roles flip",26,ACC,"BOLD").move_to([-1.88,-2.72,0])
        self.play(GrowArrow(flip),Write(flip_label),run_time=1)
        self.play(FadeIn(r),run_time=1.4)
        self.play(FadeOut(flip_label),FadeOut(heads),Write(txt("prediction steady · coefficients calm",34,ACC,"BOLD").move_to([0,2.38,0])),run_time=1.1); self.wait(2)

class B05_ChooseLambda(Scene):
    def construct(self):
        self.camera.background_color=BG
        self.play(FadeIn(spark("Tune restraint, do not guess.")))
        ax=Axes(x_range=[0,10,1],y_range=[0,6,1],x_length=11.2,y_length=5.1,axis_config={"color":GHOST,"include_tip":False,"include_numbers":False}).shift(DOWN*.38)
        self.play(Create(ax),run_time=1.5)
        paths=VGroup(*[ax.plot(lambda x,k=k: .7+(4.5-k*.65)*np.exp(-(.22+k*.015)*x),x_range=[.25,9.5],color=SOFT,stroke_width=2.5) for k in range(5)])
        self.play(LaggedStart(*[Create(p) for p in paths],lag_ratio=.12),run_time=2)
        curve=ax.plot(lambda x:.10*(x-5.4)**2+1.15,x_range=[.4,9.5],color=INK,stroke_width=6)
        cvlabel=ui("cross-validation error",30,INK,"BOLD").move_to([2.5,1.75,0])
        self.play(Create(curve),Write(cvlabel),run_time=1.8)
        point=Dot(ax.c2p(5.4,1.15),color=ACC,radius=.14); arrow=Arrow(point.get_center()+UP*1.0,point.get_center()+UP*.15,color=ACC,stroke_width=5)
        self.play(FadeOut(cvlabel),FadeIn(point),GrowArrow(arrow),Write(txt("choose near here",34,ACC,"BOLD").move_to([-2.9,2.25,0])),run_time=1.3)
        envelope=RoundedRectangle(width=2.2,height=1.15,corner_radius=.12,color=INK,fill_color=BG,fill_opacity=1,stroke_width=3)
        flap=VGroup(Line(envelope.get_corner(UL),envelope.get_center(),color=INK),Line(envelope.get_center(),envelope.get_corner(UR),color=INK))
        env=VGroup(envelope,flap).shift(RIGHT*4.65+UP*2.3)
        self.play(FadeIn(env),run_time=1); self.wait(2)

class B06_EdgeCases(Scene):
    def construct(self):
        self.camera.background_color=BG
        self.play(FadeIn(spark("Three checks before Ridge.")))
        cards=VGroup(*[panel(3.65,4.65) for _ in range(3)]).arrange(RIGHT,buff=.35).shift(DOWN*.3)
        names=("SCALE","INTERCEPT","SPARSITY")
        self.play(Create(cards),LaggedStart(*[Write(ui(n,29,ACC,"BOLD").move_to(c.get_top()+DOWN*.48)) for n,c in zip(names,cards)],lag_ratio=.15),run_time=1.8)
        left=VGroup(ui("meters",27),Rectangle(width=.75,height=2.1,color=INK,fill_color=INK,fill_opacity=.85,stroke_width=0),ui("millimeters",27),Rectangle(width=.75,height=.65,color=SOFT,fill_color=SOFT,fill_opacity=.85,stroke_width=0)).arrange(RIGHT,buff=.22,aligned_edge=DOWN).scale(.75).move_to(cards[0].get_center()+UP*.15)
        self.play(FadeIn(left),run_time=1)
        equal=VGroup(*[Rectangle(width=.65,height=1.25,color=INK,fill_color=INK,fill_opacity=.85,stroke_width=0) for _ in range(2)]).arrange(RIGHT,buff=.55,aligned_edge=DOWN).move_to(left)
        self.play(Transform(left,equal),Write(ui("standardize",28,ACC,"BOLD").move_to(cards[0].get_bottom()+UP*.5)),run_time=1.2)
        intercept=Rectangle(width=.85,height=2.2,color=INK,fill_color=INK,fill_opacity=.88,stroke_width=0).move_to(cards[1].get_center()+UP*.2)
        shield=SurroundingRectangle(intercept,buff=.2,color=ACC,corner_radius=.18)
        self.play(GrowFromEdge(intercept,DOWN),Create(shield),Write(ui("unpenalized",28,ACC,"BOLD").move_to(cards[1].get_bottom()+UP*.5)),run_time=1.3)
        ridge=Line(cards[2].get_left()+RIGHT*.55+UP*.8,cards[2].get_right()+LEFT*.55+DOWN*.2,color=INK,stroke_width=5)
        near=DashedLine(ridge.get_end(),ridge.get_end()+DOWN*.65,color=INK)
        lasso=Line(cards[2].get_left()+RIGHT*.55+UP*.1,cards[2].get_center()+DOWN*.95,color=ACC,stroke_width=5)
        zero=Dot(lasso.get_end(),color=ACC,radius=.11)
        self.play(Create(ridge),Create(near),Create(lasso),FadeIn(zero),run_time=1.5)
        self.play(Write(ui("Ridge: near 0",25).next_to(ridge,UP,buff=.15)),Write(ui("Lasso: 0",25,ACC,"BOLD").next_to(lasso,DOWN,buff=.15)),run_time=1)
        self.play(Write(txt("Stabilize, do not select.",42,ACC,"BOLD").move_to([0,-2.82,0])),run_time=1); self.wait(2)

class B07_Verdict(Scene):
    def construct(self):
        self.camera.background_color=BG
        self.play(FadeIn(spark("The verdict.")))
        board=RoundedRectangle(width=11.7,height=5.45,corner_radius=.22,color=GHOST,fill_color=BG,fill_opacity=1,stroke_width=2).shift(DOWN*.35)
        title=txt("What Ridge buys",54,INK,"BOLD").move_to(board.get_top()+DOWN*.62)
        self.play(Create(board),Write(title),run_time=1.5)
        for i,(a,b) in enumerate((("Large weights","charged"),("Variance","reduced"),("Lambda","cross-validated"))):
            y=.65-i*1.15
            rule=Line([-5.25,y-.48,0],[5.25,y-.48,0],color=GHOST,stroke_width=2)
            self.play(Create(rule),Write(txt(a,34,ACC,"BOLD").move_to([-3.75,y,0])),Write(txt(b,38,INK,"BOLD").move_to([2.0,y,0])),run_time=1.05)
        self.play(Write(txt("Steadier predictions beat dramatic coefficients.",38,ACC,"BOLD").move_to([0,-2.45,0])),run_time=1.2); self.wait(2)

class B09_Outro(Scene):
    def construct(self):
        self.camera.background_color=BG
        field=RoundedRectangle(width=11.8,height=6.15,corner_radius=.28,color=INK,fill_color=INK,fill_opacity=.97,stroke_width=0)
        mark=Text("✦",font_size=100,color=ACC).shift(UP*1.65)
        title=txt("L2 Regularization.",78,BG,"BOLD").shift(UP*.25)
        rule=Line(LEFT*4+DOWN*.55,RIGHT*4+DOWN*.55,color=ACC,stroke_width=6)
        handle=txt("@NikBearBrown",40,BG,"BOLD").shift(DOWN*1.35)
        self.play(FadeIn(field),FadeIn(mark,scale=.7),run_time=1)
        self.play(Write(title),Create(rule),run_time=1.3)
        self.play(Write(handle),run_time=.8); self.wait(2)
