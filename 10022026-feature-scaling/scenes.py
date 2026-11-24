"""Native Manim scenes for Feature Scaling: Standardization vs Normalization."""
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
        if p.exists():
            return p
    return Path.cwd() / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"

def txt(value, size=34, color=INK, weight="NORMAL"):
    if color == ACC and value != "✦": color = INK
    with register_font(_font()):
        return Text(value, font=SERIF, font_size=size, color=color, weight=weight)

def spark(value):
    return VGroup(txt("✦", 28, ACC), txt(value, 40)).arrange(RIGHT, buff=.22).to_edge(UP, buff=.55).to_edge(LEFT, buff=.82)

def wordmark():
    return txt("@sanjiv", 24, SOFT).to_edge(RIGHT, buff=.82).to_edge(DOWN, buff=.48).set_opacity(.68)

def clock(scene, actual):
    factor = actual / 10.0
    old_play, old_wait = scene.play, scene.wait
    def play(*args, **kwargs):
        kwargs["run_time"] = kwargs.get("run_time", 1.0) * factor
        return old_play(*args, **kwargs)
    def wait(duration=1.0, *args, **kwargs):
        return old_wait(duration * factor, *args, **kwargs)
    scene.play, scene.wait = play, wait

def card(label, sub="", width=3.0, height=1.25, color=INK):
    box = RoundedRectangle(width=width, height=height, corner_radius=.14, color=PALE,
                           stroke_width=4, fill_color=WHITE, fill_opacity=.97)
    lines = [txt(label, 30, color, "BOLD")]
    if sub:
        lines.append(txt(sub, 21, SOFT))
    copy = VGroup(*lines).arrange(DOWN, buff=.08)
    if copy.width > width - .28:
        copy.scale_to_fit_width(width - .28)
    if copy.height > height - .18:
        copy.scale_to_fit_height(height - .18)
    return VGroup(box, copy.move_to(box))

def number_line(left_label, mid_label, right_label, color=INK, width=7.6):
    line = Line(LEFT * width / 2, RIGHT * width / 2, color=PALE, stroke_width=8)
    dots = VGroup(Dot(line.get_left(), color=color, radius=.14), Dot(line.get_center(), color=ACC, radius=.14), Dot(line.get_right(), color=color, radius=.14))
    labels = VGroup(txt(left_label, 28, color, "BOLD").next_to(dots[0], DOWN, buff=.18),
                    txt(mid_label, 28, ACC, "BOLD").next_to(dots[1], DOWN, buff=.18),
                    txt(right_label, 28, color, "BOLD").next_to(dots[2], DOWN, buff=.18))
    return VGroup(line, dots, labels)

class Base(Scene):
    actual_duration = 20
    def setup(self):
        self.camera.background_color = BG
        clock(self, self.actual_duration)
        self.add(wordmark())

class B01_Scene(Base):
    actual_duration = 22.04
    def construct(self):
        self.play(FadeIn(spark("Change units, not information.")), run_time=.5)
        raw = VGroup(
            Arrow(LEFT*3.2, RIGHT*3.2, color=INK, buff=0),
            Arrow(DOWN*1.15, UP*1.15, color=INK, buff=0),
            Ellipse(width=5.4, height=1.25, color=INK, stroke_width=6),
            txt("RAW UNITS", 28, SOFT, "BOLD").move_to([0,-1.65,0])
        ).move_to([-3.0,.05,0])
        self.play(FadeIn(raw, scale=.9), run_time=.9)
        balanced = VGroup(
            Arrow(LEFT*2.25, RIGHT*2.25, color=INK, buff=0),
            Arrow(DOWN*1.7, UP*1.7, color=INK, buff=0),
            Circle(1.3, color=INK, stroke_width=6),
            txt("SCALED", 28, SOFT, "BOLD").move_to([0,-2.0,0])
        ).move_to([3.55,.05,0])
        self.play(FadeIn(balanced, shift=LEFT*.15), run_time=1.0)
        choices = VGroup(card("STANDARDIZE", "mean 0 · deviation units",4.5,1.2,ACC),
                         card("MIN–MAX", "training range → 0 to 1",4.5,1.2,INK)).arrange(RIGHT,buff=.65).to_edge(DOWN,buff=.72)
        self.play(FadeIn(choices[0],shift=UP*.15),FadeIn(choices[1],shift=UP*.15),run_time=.85)
        self.wait(4.7)

class B02_Scene(Base):
    actual_duration = 22.68
    def construct(self):
        self.play(FadeIn(spark("Units change the geometry.")),run_time=.5)
        knn=card("DISTANCE","large units dominate",4.15,1.35,ACC).move_to([-3.7,1.35,0])
        grad=card("GRADIENTS","zigzag in a narrow valley",4.15,1.35,INK).move_to([3.7,1.35,0])
        reg=card("REGULARIZATION","penalties meet unequal scales",4.15,1.35,INK).move_to([-3.7,-.65,0])
        tree=card("TREES","usually scale-insensitive",4.15,1.35,ACC).move_to([3.7,-.65,0])
        self.play(FadeIn(knn,scale=.88),run_time=.7)
        self.play(FadeIn(grad,scale=.88),run_time=.7)
        self.play(FadeIn(reg,scale=.88),run_time=.7)
        self.play(FadeIn(tree,scale=.88),run_time=.7)
        footer=txt("SCALE WHEN THE MODEL USES MAGNITUDE",31,SOFT,"BOLD").to_edge(DOWN,buff=.65)
        self.play(FadeIn(footer),run_time=.55); self.wait(4.35)

class B03_Scene(Base):
    actual_duration = 21.55
    def construct(self):
        self.play(FadeIn(spark("Center. Then scale.")),run_time=.5)
        formula=txt("z = (x − mean) / standard deviation",48,INK,"BOLD").move_to([0,1.65,0])
        self.play(Write(formula),run_time=.9)
        raw=number_line("10","20","30",INK,7.8).move_to([0,.35,0])
        self.play(FadeIn(raw),run_time=.75)
        stats=VGroup(card("MEAN","20",3.0,1.05,ACC),card("STD DEV","≈ 8.16",3.0,1.05,INK)).arrange(RIGHT,buff=.5).move_to([0,-.75,0])
        self.play(FadeIn(stats[0]),FadeIn(stats[1]),run_time=.8)
        scaled=number_line("−1.22","0","+1.22",ACC,7.8).move_to([0,-1.85,0])
        self.play(FadeIn(scaled, shift=UP*.12),run_time=.9)
        warning=txt("STANDARDIZED ≠ NORMALLY DISTRIBUTED",27,WARN,"BOLD").to_edge(DOWN,buff=.48)
        self.play(FadeIn(warning),run_time=.5); self.wait(4.05)

class B04_Scene(Base):
    actual_duration = 19.31
    def construct(self):
        self.play(FadeIn(spark("Anchor to the endpoints.")),run_time=.5)
        formula=txt("scaled = (x − min) / (max − min)",47,INK,"BOLD").move_to([0,1.65,0])
        self.play(Write(formula),run_time=.9)
        raw=number_line("10","20","30",INK,7.6).move_to([0,.45,0])
        scaled=number_line("0","0.5","1",ACC,7.6).move_to([0,-.75,0])
        self.play(FadeIn(raw),run_time=.65); self.play(FadeIn(scaled, shift=UP*.12),run_time=.8)
        outlier=card("ADD OUTLIER: 100","10 · 20 · 30 compress near zero",7.0,1.25,WARN).move_to([0,-2.15,0])
        self.play(FadeIn(outlier,scale=.88),run_time=.75); self.wait(4.45)

class B05_Scene(Base):
    actual_duration = 22.66
    def construct(self):
        self.play(FadeIn(spark("Both defaults can bend.")),run_time=.5)
        std=card("STANDARDIZATION","centered · unbounded",5.0,1.35,ACC).move_to([-3.25,1.25,0])
        mm=card("MIN–MAX","training observations → 0…1",5.0,1.35,INK).move_to([3.25,1.25,0])
        self.play(FadeIn(std),FadeIn(mm),run_time=.85)
        out1=card("OUTLIER","moves mean and deviation",4.7,1.2,WARN).move_to([-3.25,-.2,0])
        out2=card("OUTLIER","moves both endpoints",4.7,1.2,WARN).move_to([3.25,-.2,0])
        self.play(FadeIn(out1),FadeIn(out2),run_time=.75)
        new=card("NEW VALUE","may transform below 0 or above 1",5.3,1.25,ACC).move_to([3.25,-1.65,0])
        robust=card("ROBUST SCALER","median and quantiles",5.3,1.25,INK).move_to([-3.25,-1.65,0])
        self.play(FadeIn(robust),FadeIn(new),run_time=.8)
        self.wait(4.55)

class B06_Scene(Base):
    actual_duration = 23.23
    def construct(self):
        self.play(FadeIn(spark("Fit train. Reuse everywhere.")),run_time=.5)
        raw=card("RAW DATA","split first",2.6,1.2,INK).move_to([-4.8,.65,0])
        train=card("TRAIN","fit scaler",2.8,1.2,ACC).move_to([-1.75,1.4,0])
        test=card("TEST","transform only",2.8,1.2,INK).move_to([-1.75,-.15,0])
        model=card("MODEL","same stored parameters",4.0,1.35,ACC).move_to([3.55,.65,0])
        a1=Arrow(raw.get_right(),train.get_left(),buff=.2,color=INK)
        a2=Arrow(raw.get_right(),test.get_left(),buff=.2,color=PALE)
        a3=Arrow(train.get_right(),model.get_left(),buff=.2,color=INK)
        a4=Arrow(test.get_right(),model.get_left(),buff=.2,color=INK)
        self.play(FadeIn(raw),run_time=.55)
        self.play(GrowArrow(a1),GrowArrow(a2),FadeIn(train),FadeIn(test),run_time=.95)
        self.play(GrowArrow(a3),GrowArrow(a4),FadeIn(model),run_time=.85)
        leak=card("BLOCKED","fit scaler before split = leakage",5.6,1.1,WARN).move_to([0,-1.55,0])
        self.play(FadeIn(leak,scale=.9),run_time=.7)
        names=VGroup(card("MIN–MAX","feature-wise range",4.4,1.05,ACC),card("UNIT NORM","sample-wise length",4.4,1.05,INK)).arrange(RIGHT,buff=.65).to_edge(DOWN,buff=.55)
        self.play(FadeIn(names[0]),FadeIn(names[1]),run_time=.75); self.wait(4.1)
