"""Native Manim scenes for Random Forest: Why Multiple Trees Beat One."""
from contextlib import contextmanager
from pathlib import Path
from manim import *

try:
    from manim import register_font
except (ImportError, ModuleNotFoundError):
    @contextmanager
    def register_font(_):
        yield

BG = ManimColor("#FAF9F5")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
SOFT = ManimColor("#6E6A57")
PALE = ManimColor("#DED9CC")
WHITE = ManimColor("#FFFDF8")
WARN = ManimColor("#A44A32")
SERIF = "EB Garamond"

def _font():
    for parent in (Path.cwd(), *Path(__file__).resolve().parents):
        p = parent / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"
        if p.exists(): return p
    return Path.cwd() / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"

def txt(s, size=34, color=INK, weight="NORMAL"):
    with register_font(_font()):
        return Text(s, font=SERIF, font_size=size, color=color, weight=weight)

def spark(s):
    return VGroup(txt("✦", 28, ACC), txt(s, 40)).arrange(RIGHT, buff=.22).to_edge(UP, buff=.55).to_edge(LEFT, buff=.82)

def wordmark():
    return txt("@Sanjiv", 24, SOFT).to_edge(RIGHT, buff=.82).to_edge(DOWN, buff=.48).set_opacity(.68)

def clock(scene, actual):
    factor = actual / 10.0
    op, ow = scene.play, scene.wait
    def play(*a, **k):
        k["run_time"] = k.get("run_time", 1.0) * factor
        return op(*a, **k)
    def wait(d=1.0, *a, **k): return ow(d * factor, *a, **k)
    scene.play, scene.wait = play, wait

def card(label, sub="", width=3.0, height=1.25, color=INK):
    box = RoundedRectangle(width=width, height=height, corner_radius=.14, color=color,
                           stroke_width=4, fill_color=WHITE, fill_opacity=.97)
    lines = [txt(label, 30, color, "BOLD")]
    if sub: lines.append(txt(sub, 22, SOFT))
    copy = VGroup(*lines).arrange(DOWN, buff=.08)
    if copy.width > width - .28:
        copy.scale_to_fit_width(width - .28)
    if copy.height > height - .18:
        copy.scale_to_fit_height(height - .18)
    return VGroup(box, copy.move_to(box))

def tree(scale=1.0, color=INK, root="ROOT"):
    r = card(root, "", 1.9, .85, color)
    l = card("L", "", 1.25, .7, color).move_to([-1.15,-1.2,0])
    rr = card("R", "", 1.25, .7, color).move_to([1.15,-1.2,0])
    e = VGroup(Line(r.get_bottom(),l.get_top(),color=PALE,stroke_width=6), Line(r.get_bottom(),rr.get_top(),color=PALE,stroke_width=6))
    return VGroup(e,r,l,rr).scale(scale)

class Base(Scene):
    actual_duration = 20
    def setup(self):
        self.camera.background_color = BG
        clock(self, self.actual_duration)
        self.add(wordmark())

class B01_Scene(Base):
    actual_duration = 20.59
    def construct(self):
        self.play(FadeIn(spark("Different mistakes. Steadier average.")), run_time=.55)
        one = tree(.95, ACC, "ONE TREE").move_to([-4.85,-.15,0])
        self.play(FadeIn(one, scale=.85), run_time=.75)
        forest = VGroup(*[tree(.55, ACC if i==2 else INK, f"T{i+1}") for i in range(5)]).arrange(RIGHT,buff=.25).move_to([2.25,.1,0])
        self.play(LaggedStart(*[FadeIn(t,shift=UP*.15) for t in forest],lag_ratio=.12),run_time=1.35)
        needles = VGroup(*[Line([x,-2.15,0],[x+dx,-1.65,0],color=ACC if i==2 else INK,stroke_width=7) for i,(x,dx) in enumerate(zip([-1.1,.5,2.1,3.7,5.3],[-.35,.25,-.3,.18,.28]))])
        self.play(LaggedStart(*[Create(n) for n in needles],lag_ratio=.1),run_time=.9)
        avg = card("AVERAGE", "lower variance", 3.6, 1.2, ACC).move_to([2.1,-2.55,0])
        self.play(ReplacementTransform(needles,avg),run_time=.9); self.wait(5.0)

class B02_Scene(Base):
    actual_duration = 22.34
    def construct(self):
        self.play(FadeIn(spark("Perturb. Grow. Combine.")),run_time=.55)
        data = card("TRAINING ROWS", "1 2 3 4 5 6",3.2,1.3,INK).move_to([-5,1.0,0])
        bags = VGroup(card("BAG A","1 1 3 5",2.4,1.1,ACC),card("BAG B","2 3 3 6",2.4,1.1,INK),card("BAG C","1 4 5 6",2.4,1.1,INK)).arrange(DOWN,buff=.25).move_to([-1.8,.45,0])
        trees = VGroup(*[tree(.55,ACC if i==0 else INK,f"T{i+1}") for i in range(3)]).arrange(DOWN,buff=.15).move_to([1.6,.45,0])
        out = card("AVERAGE", "probability or value",3.5,1.45,ACC).move_to([5,.45,0])
        self.play(FadeIn(data),run_time=.7)
        a1=Arrow(data.get_right(),bags.get_left(),buff=.18,color=PALE); a2=Arrow(bags.get_right(),trees.get_left(),buff=.18,color=PALE); a3=Arrow(trees.get_right(),out.get_left(),buff=.18,color=ACC)
        self.play(GrowArrow(a1),LaggedStart(*[FadeIn(b) for b in bags],lag_ratio=.14),run_time=1.1)
        self.play(GrowArrow(a2),LaggedStart(*[FadeIn(t) for t in trees],lag_ratio=.14),run_time=1.1)
        self.play(GrowArrow(a3),FadeIn(out,scale=.86),run_time=.8)
        self.play(FadeIn(txt("STRONG TREES  +  LOWER ERROR CORRELATION",28,SOFT,"BOLD").to_edge(DOWN,buff=.75)),run_time=.55); self.wait(4.6)

class B03_Scene(Base):
    actual_duration = 20.12
    def construct(self):
        self.play(FadeIn(spark("One tree can wobble.")),run_time=.5)
        tables=VGroup(card("SAMPLE A","rows 1–8",3.2,1.15),card("SAMPLE B","rows 1–7, 9",3.2,1.15,ACC)).arrange(RIGHT,buff=4.2).move_to([0,1.65,0])
        self.play(FadeIn(tables[0]),FadeIn(tables[1]),run_time=.8)
        t1=tree(.9,INK,"FEATURE X").move_to([-3.7,-.35,0]); t2=tree(.9,ACC,"FEATURE Y").move_to([3.7,-.35,0])
        arrows=VGroup(Arrow(tables[0].get_bottom(),t1.get_top(),buff=.15,color=PALE),Arrow(tables[1].get_bottom(),t2.get_top(),buff=.15,color=PALE))
        self.play(GrowArrow(arrows[0]),GrowArrow(arrows[1]),FadeIn(t1),FadeIn(t2),run_time=1.4)
        p1=card("TEST POINT","CLASS A",2.7,1.05,INK).move_to([-3.7,-2.25,0]); p2=card("SAME POINT","CLASS B",2.7,1.05,WARN).move_to([3.7,-2.25,0])
        self.play(FadeIn(p1),FadeIn(p2),run_time=.8)
        self.play(FadeIn(txt("SMALL DATA CHANGE  →  DIFFERENT TREE",31,ACC,"BOLD").to_edge(DOWN,buff=.63)),run_time=.55); self.wait(4.8)

class B04_Scene(Base):
    actual_duration = 21.46
    def construct(self):
        self.play(FadeIn(spark("Manufacture useful disagreement.")),run_time=.5)
        bags=VGroup(card("ROWS A","1 1 3 5",2.6,1.0,ACC),card("ROWS B","2 3 3 6",2.6,1.0),card("ROWS C","1 4 5 6",2.6,1.0)).arrange(RIGHT,buff=.55).move_to([0,1.65,0])
        self.play(LaggedStart(*[FadeIn(b,shift=UP*.12) for b in bags],lag_ratio=.14),run_time=1.0)
        feats=VGroup(card("X · Z","feature subset",2.6,1.0,ACC),card("Y · Z","feature subset",2.6,1.0),card("X · Y","feature subset",2.6,1.0)).arrange(RIGHT,buff=.55).move_to([0,.25,0])
        self.play(LaggedStart(*[FadeIn(f) for f in feats],lag_ratio=.14),run_time=1.0)
        ts=VGroup(*[tree(.62,ACC if i==0 else INK,f"T{i+1}") for i in range(3)]).arrange(RIGHT,buff=1.1).move_to([0,-1.45,0])
        self.play(LaggedStart(*[FadeIn(t,scale=.85) for t in ts],lag_ratio=.14),run_time=1.2)
        gauge=VGroup(txt("ERROR CORRELATION",25,SOFT,"BOLD"),Line(LEFT*2.2,RIGHT*2.2,color=PALE,stroke_width=10),Dot(LEFT*.9,color=ACC,radius=.16)).arrange(DOWN,buff=.12).to_edge(DOWN,buff=.55)
        self.play(FadeIn(gauge),run_time=.65); self.wait(4.65)

class B05_Scene(Base):
    actual_duration = 21.16
    def construct(self):
        self.play(FadeIn(spark("Average the probabilities.")),run_time=.5)
        vals=[.9,.8,.2,.7,.4]
        cards=VGroup(*[card(f"TREE {i+1}",f"P(A) = {v:.1f}",2.35,1.25,ACC if i==2 else INK) for i,v in enumerate(vals)]).arrange(RIGHT,buff=.24).move_to([0,1.25,0])
        self.play(LaggedStart(*[FadeIn(c,shift=UP*.15) for c in cards],lag_ratio=.12),run_time=1.45)
        sumline=txt("0.9 + 0.8 + 0.2 + 0.7 + 0.4 = 3.0",40,INK,"BOLD").move_to([0,-.25,0])
        self.play(Write(sumline),run_time=1.0)
        mean=card("MEAN P(A)","3.0 ÷ 5 = 0.60",4.4,1.5,ACC).move_to([0,-1.55,0])
        self.play(FadeIn(mean,scale=.84),run_time=.8)
        cutoff=txt("0.60 > 0.50  →  CLASS A",36,ACC,"BOLD").to_edge(DOWN,buff=.62)
        self.play(FadeIn(cutoff),run_time=.55); self.wait(4.9)

class B06_Scene(Base):
    actual_duration = 21.65
    def construct(self):
        self.play(FadeIn(spark("A crowd can echo.")),run_time=.5)
        row=VGroup(*[tree(.4,WARN,"SAME") for _ in range(7)]).arrange(RIGHT,buff=.22).move_to([0,1.45,0])
        self.play(LaggedStart(*[FadeIn(t,shift=UP*.1) for t in row],lag_ratio=.08),run_time=1.25)
        wrong=card("CORRELATED ERROR","seven trees · same mistake",5.1,1.35,WARN).move_to([0,-.15,0])
        self.play(FadeIn(wrong,scale=.88),run_time=.8)
        weak=VGroup(card("WEAK SIGNAL","averaging cannot create it",4.6,1.25),card("MORE COMPUTE","fit time and complexity",4.6,1.25)).arrange(RIGHT,buff=.6).move_to([0,-1.85,0])
        self.play(FadeIn(weak[0]),FadeIn(weak[1]),run_time=.9)
        self.play(FadeIn(txt("VALIDATION + OUT-OF-BAG > TREE COUNT",30,ACC,"BOLD").to_edge(DOWN,buff=.58)),run_time=.55); self.wait(4.9)
