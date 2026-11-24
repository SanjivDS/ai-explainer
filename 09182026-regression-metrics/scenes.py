"""Native Manim concept illustrations for Regression Metrics, Oversimplified."""
from pathlib import Path
from contextlib import contextmanager
from manim import *
try:
    from manim import register_font
except (ImportError, ModuleNotFoundError):
    @contextmanager
    def register_font(_):
        yield

BG = ManimColor("#F2F0E9")
INK = ManimColor("#3D3929")
ACC = ManimColor("#A44A32")
WARN = ManimColor("#A44A32")
SOFT = ManimColor("#6E6A57")
PALE = ManimColor("#DED9CC")
WHITE = ManimColor("#FAF9F5")
SERIF = "EB Garamond"

def _font():
    for parent in (Path.cwd(), *Path(__file__).resolve().parents):
        p = parent / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"
        if p.exists(): return p
    return Path.cwd() / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"

def txt(s, size=34, color=INK, weight="NORMAL"):
    if color == ACC and s != "✦":
        color = INK
    size = max(size, 28)
    with register_font(_font()):
        return Text(s, font=SERIF, font_size=size, color=color, weight=weight)

def spark(s):
    return VGroup(txt("✦", 28, ACC), txt(s, 42)).arrange(RIGHT, buff=.22).to_edge(UP, buff=.6).to_edge(LEFT, buff=.92)

def clock(scene, actual):
    factor = actual / 10.0
    play, wait = scene.play, scene.wait
    def p(*a, **k):
        k["run_time"] = k.get("run_time", 1.0) * factor
        return play(*a, **k)
    def w(d=1.0, *a, **k): return wait(d * factor, *a, **k)
    scene.play, scene.wait = p, w

def card(label, sub="", width=2.2, height=1.35, color=INK):
    box = RoundedRectangle(width=width, height=height, corner_radius=.16, color=PALE, stroke_width=4, fill_color=WHITE, fill_opacity=.94)
    lines = [txt(label, 34, color, "BOLD")]
    if sub: lines.append(txt(sub, 25, SOFT))
    body = VGroup(*lines).arrange(DOWN, buff=.12).move_to(box)
    return VGroup(box, body)

def bar(h, x, color=INK, width=.62):
    return Rectangle(width=width, height=h, color=color, fill_color=color, fill_opacity=.88, stroke_width=0).move_to([x, -2.2+h/2, 0])

class B01_FiveLenses(Scene):
    def construct(self):
        clock(self, 22.70); self.camera.background_color = BG
        title = spark("One residual. Five lenses.")
        actual = Dot([-5.1,.75,0], radius=.16, color=INK); pred = Dot([-5.1,-1.0,0], radius=.16, color=ACC)
        gap = DoubleArrow([-5.1,-.8,0],[-5.1,.55,0],buff=0,color=ACC,stroke_width=6)
        residual = txt("residual = actual − prediction",31).move_to([-4.0,-1.75,0])
        self.play(FadeIn(title), FadeIn(actual), FadeIn(pred), GrowArrow(gap), FadeIn(residual), run_time=1.4)
        labels = [("MAE","steady"),("MSE","squared"),("RMSE","units"),("R²","baseline"),("MAPE","relative")]
        cards = VGroup(*[card(a,b,2.0,1.3,ACC if i==1 else INK) for i,(a,b) in enumerate(labels)]).arrange_in_grid(rows=2, cols=3, buff=(.45,.55)).move_to([2.15,-.25,0])
        arrows = VGroup(*[Arrow([-3.0,-.25,0],c.get_left(),buff=.14,color=PALE,stroke_width=4) for c in cards])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.08), run_time=1.3)
        self.play(LaggedStart(*[FadeIn(c,scale=.8) for c in cards],lag_ratio=.12), run_time=1.8)
        verdict = txt("MATCH THE METRIC TO THE COST",38,ACC,"BOLD").to_edge(DOWN,buff=.55)
        self.play(FadeIn(verdict), run_time=.7); self.wait(4.8)

class B02_ResidualFramework(Scene):
    def construct(self):
        clock(self, 22.95); self.camera.background_color = BG
        self.play(FadeIn(spark("Residuals come first.")), run_time=.7)
        eq = txt("residual  =  actual  −  prediction",48,INK,"BOLD").move_to([0,2.0,0])
        self.play(Write(eq), run_time=1.1)
        items = [card("MAE","average |error|",3.5,1.35),card("MSE","average error²",3.5,1.35,ACC),card("RMSE","√ average error²",3.5,1.35),card("R²","1 − model / mean",3.5,1.35),card("MAPE","average |error/actual|",3.5,1.35,WARN)]
        grid=VGroup(*items).arrange_in_grid(rows=2,cols=3,buff=(.55,.48)).move_to([0,-.55,0])
        self.play(LaggedStart(*[FadeIn(x,shift=DOWN*.2) for x in grid],lag_ratio=.12), run_time=2.2)
        z = txt("actual = 0: ordinary MAPE undefined",30,WARN,"BOLD").to_edge(DOWN,buff=.38)
        self.play(FadeIn(z),run_time=.8); self.wait(5.2)

class B03_WorkedExample(Scene):
    def construct(self):
        clock(self, 20.93); self.camera.background_color=BG
        self.play(FadeIn(spark("One dataset. Three answers.")),run_time=.6)
        heads=VGroup(*[txt(s,31,SOFT,"BOLD") for s in ["CASE","ACTUAL","PREDICTED","|ERROR|","ERROR²"]]).arrange(RIGHT,buff=.92).move_to([0,2.15,0])
        self.play(FadeIn(heads),run_time=.7)
        vals=[("A","2","3","1","1"),("B","4","5","1","1"),("C","6","5","1","1"),("D","8","11","3","9")]
        rows=VGroup()
        for r,row in enumerate(vals):
            cells=VGroup(*[txt(v,35,ACC if (r==3 and c>=3) else INK,"BOLD" if c>=3 else "NORMAL") for c,v in enumerate(row)]).arrange(RIGHT,buff=1.45).move_to([0,1.25-r*.72,0]); rows.add(cells)
        self.play(LaggedStart(*[FadeIn(r,shift=RIGHT*.18) for r in rows],lag_ratio=.16),run_time=2.0)
        metrics=VGroup(card("MAE = 1.50","(1+1+1+3) / 4",3.7,1.25),card("MSE = 3.00","(1+1+1+9) / 4",3.7,1.25,ACC),card("RMSE ≈ 1.73","√3, original units",3.7,1.25)).arrange(RIGHT,buff=.48).to_edge(DOWN,buff=.48)
        self.play(LaggedStart(*[FadeIn(m,scale=.82) for m in metrics],lag_ratio=.18),run_time=1.8); self.wait(4.9)

class B04_SameMaeSplit(Scene):
    def construct(self):
        clock(self,22.02); self.camera.background_color=BG
        self.play(FadeIn(spark("Same MAE. Different risk.")),run_time=.6)
        labA=txt("MODEL A",38,INK,"BOLD").move_to([-3.4,2.05,0]); labB=txt("MODEL B",38,INK,"BOLD").move_to([3.4,2.05,0])
        self.play(FadeIn(labA),FadeIn(labB),run_time=.6)
        a=VGroup(*[bar(1.25,-5.0+i*1.05,INK) for i in range(4)])
        b=VGroup(*[bar(.08,1.8+i*1.05,PALE) for i in range(3)],bar(3.8,4.95,ACC))
        base=Line([-5.7,-2.2,0],[5.7,-2.2,0],color=INK,stroke_width=3)
        self.play(Create(base),LaggedStart(*[GrowFromEdge(x,DOWN) for x in a],lag_ratio=.1),run_time=1.5)
        self.play(LaggedStart(*[GrowFromEdge(x,DOWN) for x in b],lag_ratio=.1),run_time=1.5)
        errors=VGroup(txt("errors: 2, 2, 2, 2",31).move_to([-3.4,-2.72,0]),txt("errors: 0, 0, 0, 8",31).move_to([3.4,-2.72,0]))
        self.play(FadeIn(errors),run_time=.6)
        score_a=VGroup(txt("MAE 2  ·  RMSE 2",35,INK,"BOLD"),txt("steady misses",27,SOFT)).arrange(DOWN,buff=.12)
        score_b=VGroup(txt("MAE 2  ·  RMSE 4",35,ACC,"BOLD"),txt("one costly miss",27,SOFT)).arrange(DOWN,buff=.12)
        left_bg=RoundedRectangle(width=5.4,height=4.8,corner_radius=.2,stroke_width=0,fill_color=PALE,fill_opacity=.48).move_to([-3.05,-.25,0])
        right_bg=RoundedRectangle(width=5.4,height=4.8,corner_radius=.2,stroke_width=0,fill_color=ACC,fill_opacity=.16).move_to([3.05,-.25,0])
        score_a.move_to(left_bg); score_b.move_to(right_bg)
        scores=VGroup(left_bg,right_bg,score_a,score_b)
        self.play(FadeOut(VGroup(a,b,base,errors,labA,labB)),FadeIn(scores),run_time=1.0); self.wait(4.2)

class B05_R2Baseline(Scene):
    def construct(self):
        clock(self,20.69); self.camera.background_color=BG
        self.play(FadeIn(spark("Beat the baseline.")),run_time=.6)
        formula=txt("R²  =  1  −  model squared error / mean-baseline squared error",32,INK,"BOLD").move_to([0,2.05,0])
        self.play(Write(formula),run_time=1.25)
        base=VGroup(txt("MEAN BASELINE",30,SOFT,"BOLD"),VGroup(*[bar(h,-5.0+i*.8,SOFT,.48) for i,h in enumerate([2.8,1.7,.9,2.2])])).arrange(DOWN,buff=.25).move_to([-3.7,-.15,0])
        model=VGroup(txt("MODEL",30,ACC,"BOLD"),VGroup(*[bar(h,1.8+i*.8,ACC,.48) for i,h in enumerate([1.1,.6,.35,.9])])).arrange(DOWN,buff=.25).move_to([3.1,-.15,0])
        self.play(FadeIn(base),run_time=1.1); self.play(TransformFromCopy(base,model),run_time=1.2)
        scale=Line([-4.4,-2.65,0],[4.4,-2.65,0],color=INK,stroke_width=4)
        ticks=VGroup(*[Line([x,-2.78,0],[x,-2.52,0],color=INK,stroke_width=3) for x in [-4.4,0,4.4]])
        nums=VGroup(txt("−1",25,SOFT).move_to([-4.4,-3.02,0]),txt("0",25,SOFT).move_to([0,-3.02,0]),txt("1",25,SOFT).move_to([4.4,-3.02,0]))
        dot=Dot([3.17,-2.65,0],radius=.15,color=ACC); tag=txt("1 perfect   ·   0 mean baseline   ·   below 0 worse",28,SOFT).next_to(scale,UP,buff=.18)
        self.play(Create(scale),FadeIn(ticks),FadeIn(nums),FadeIn(dot),FadeIn(tag),run_time=1.1); self.wait(4.15)

class B06_MapeStress(Scene):
    def construct(self):
        clock(self,22.74); self.camera.background_color=BG
        self.play(FadeIn(spark("Percent can explode.")),run_time=.6)
        left=card("ACTUAL 1","miss by 1: 100%",4.2,1.55,ACC).move_to([-3.25,1.15,0])
        right=card("ACTUAL 100","miss by 1: 1%",4.2,1.55).move_to([3.25,1.15,0])
        self.play(FadeIn(left,shift=RIGHT*.2),FadeIn(right,shift=LEFT*.2),run_time=1.3)
        frac=txt("| actual − prediction |  /  | actual |",44,INK,"BOLD").move_to([0,-.45,0])
        self.play(Write(frac),run_time=1.0)
        zeros=VGroup(card("NEAR ZERO","tiny denominator, huge weight",5.0,1.45,WARN),card("ZERO","ordinary MAPE undefined",5.0,1.45,WARN)).arrange(RIGHT,buff=.55).move_to([0,-1.8,0])
        self.play(FadeIn(zeros[0],scale=.85),run_time=1.0); self.play(FadeIn(zeros[1],scale=.85),run_time=1.0)
        footer=txt("USE ONLY WHEN RELATIVE ERROR IS MEANINGFUL",31,ACC,"BOLD").to_edge(DOWN,buff=.58)
        self.play(FadeIn(footer),run_time=.7); self.wait(4.4)
