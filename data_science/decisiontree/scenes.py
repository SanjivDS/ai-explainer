"""Native Manim illustrations for Decision Trees: How Splits Actually Work."""
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
        path = parent / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"
        if path.exists():
            return path
    return Path.cwd() / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"


def txt(value, size=34, color=INK, weight="NORMAL"):
    with register_font(_font()):
        return Text(value, font=SERIF, font_size=size, color=color, weight=weight)


def spark(value):
    return VGroup(txt("✦", 28, ACC), txt(value, 40)).arrange(RIGHT, buff=.22).to_edge(UP, buff=.55).to_edge(LEFT, buff=.82)


def wordmark():
    return txt("@Sanjiv", 24, SOFT).to_edge(RIGHT, buff=.82).to_edge(DOWN, buff=.48).set_opacity(.68)


def clock(scene, actual):
    factor = actual / 10.0
    original_play, original_wait = scene.play, scene.wait
    def play(*args, **kwargs):
        kwargs["run_time"] = kwargs.get("run_time", 1.0) * factor
        return original_play(*args, **kwargs)
    def wait(duration=1.0, *args, **kwargs):
        return original_wait(duration * factor, *args, **kwargs)
    scene.play, scene.wait = play, wait


def card(label, sub="", width=3.0, height=1.25, color=INK):
    box = RoundedRectangle(width=width, height=height, corner_radius=.14, color=color,
                           stroke_width=4, fill_color=WHITE, fill_opacity=.96)
    lines = [txt(label, 30, color, "BOLD")]
    if sub:
        lines.append(txt(sub, 22, SOFT))
    return VGroup(box, VGroup(*lines).arrange(DOWN, buff=.08).move_to(box))


def node(label, sub="", color=INK, width=3.0):
    return card(label, sub, width, 1.28, color)


def sample_row(scale=.78):
    values = [("1", "A"), ("2", "A"), ("3", "A"), ("4", "B"), ("5", "B"), ("6", "B")]
    items = VGroup()
    for value, label in values:
        circle = Circle(.38, color=ACC if label == "A" else INK, stroke_width=5,
                        fill_color=WHITE, fill_opacity=1)
        pair = VGroup(circle, txt(label, 28, ACC if label == "A" else INK, "BOLD").move_to(circle),
                      txt(value, 22, SOFT).next_to(circle, DOWN, buff=.12))
        items.add(pair)
    return items.arrange(RIGHT, buff=.48).scale(scale)


class Base(Scene):
    actual_duration = 20.0
    def setup(self):
        self.camera.background_color = BG
        clock(self, self.actual_duration)
        self.add(wordmark())


class B01_Scene(Base):
    actual_duration = 18.79
    def construct(self):
        self.play(FadeIn(spark("Score. Split. Repeat.")), run_time=.55)
        root = node("MIXED NODE", "A A A · B B B", ACC, 3.5).move_to([0, 1.35, 0])
        self.play(FadeIn(root, scale=.88), run_time=.7)
        row = sample_row(1.0).move_to([0, -.25, 0])
        # Candidate thresholds belong halfway between adjacent sorted samples.
        centers = [item.get_center()[0] for item in row]
        cut_x = [(centers[i] + centers[i + 1]) / 2 for i in range(len(centers) - 1)]
        cuts = VGroup(*[DashedLine([x, .35, 0], [x, -.75, 0], color=SOFT, dash_length=.12) for x in cut_x])
        self.play(FadeIn(row), LaggedStart(*[Create(c) for c in cuts], lag_ratio=.1), run_time=1.25)
        left = node("LEFT", "A A A", ACC, 3.0).move_to([-3, -1.85, 0])
        right = node("RIGHT", "B B B", INK, 3.0).move_to([3, -1.85, 0])
        # Clear the candidate row before drawing the selected split branches.
        self.play(FadeOut(cuts), FadeOut(row), run_time=.4)
        arrows = VGroup(Arrow(root.get_bottom(), left.get_top(), buff=.15, color=ACC),
                        Arrow(root.get_bottom(), right.get_top(), buff=.15, color=INK))
        self.play(GrowArrow(arrows[0]), GrowArrow(arrows[1]), FadeIn(left), FadeIn(right), run_time=1.25)
        stop = txt("STOP: depth · samples · minimum gain · pruning", 29, WARN, "BOLD").to_edge(DOWN, buff=.75)
        self.play(FadeIn(stop, shift=UP*.15), run_time=.65); self.wait(5.6)


class B02_Scene(Base):
    actual_duration = 19.80
    def construct(self):
        self.play(FadeIn(spark("Purity is the scoreboard.")), run_time=.55)
        formula = txt("Gini = 1 − Σ pₖ²", 56, INK, "BOLD").move_to([0, 1.45, 0])
        self.play(Write(formula), run_time=1.0)
        pure = card("PURE", "6A · Gini = 0", 4.0, 1.45, ACC).move_to([-3.3, -.2, 0])
        mixed = card("MIXED", "3A + 3B · Gini = 0.5", 4.3, 1.45, INK).move_to([3.05, -.2, 0])
        self.play(FadeIn(pure, shift=RIGHT*.2), FadeIn(mixed, shift=LEFT*.2), run_time=1.2)
        weighted = txt("G children = (nL / n) GL + (nR / n) GR", 43, ACC, "BOLD").move_to([0, -1.75, 0])
        self.play(Write(weighted), run_time=1.0)
        self.play(FadeIn(txt("LOWER CHILD IMPURITY  →  LARGER DECREASE", 28, SOFT, "BOLD").to_edge(DOWN, buff=.72)), run_time=.55); self.wait(5.25)


class B03_Scene(Base):
    actual_duration = 21.25
    def construct(self):
        self.play(FadeIn(spark("Candidates live between values.")), run_time=.55)
        row = sample_row(1.13).move_to([0, .7, 0]); self.play(FadeIn(row, shift=UP*.15), run_time=.8)
        xs = [row[i].get_center()[0] for i in range(6)]
        mids = [1.5,2.5,3.5,4.5,5.5]
        lines = VGroup(); labels = VGroup()
        for i, midpoint in enumerate(mids):
            x = (xs[i]+xs[i+1])/2
            lines.add(DashedLine([x,1.35,0],[x,-.55,0],color=ACC if midpoint==3.5 else PALE,stroke_width=5))
            labels.add(txt(str(midpoint), 25, ACC if midpoint==3.5 else SOFT, "BOLD").move_to([x,-.85,0]))
        self.play(LaggedStart(*[Create(line) for line in lines], lag_ratio=.12),
                  LaggedStart(*[FadeIn(label) for label in labels], lag_ratio=.12), run_time=1.6)
        rule = txt("x ≤ threshold  →  LEFT     x > threshold  →  RIGHT", 39, INK, "BOLD").move_to([0,-1.75,0])
        self.play(Write(rule), run_time=.9)
        self.play(FadeIn(txt("SCIKIT-LEARN BEST SPLITTER · IMPLEMENTATIONS VARY", 25, SOFT, "BOLD").to_edge(DOWN, buff=.7)), run_time=.55); self.wait(5.0)


class B04_Scene(Base):
    actual_duration = 18.43
    def construct(self):
        self.play(FadeIn(spark("Threshold 2.5 helps—but loses.")), run_time=.5)
        parent = txt("G parent = 1 − (3/6)² − (3/6)² = 0.5", 42, INK, "BOLD").move_to([0,1.55,0])
        self.play(Write(parent), run_time=.9)
        left = card("x ≤ 2.5", "A A · Gini 0", 4.2, 1.45, ACC).move_to([-3.05,.05,0])
        right = card("x > 2.5", "A B B B · Gini 0.375", 4.7, 1.45, INK).move_to([2.8,.05,0])
        self.play(FadeIn(left, shift=RIGHT*.2), FadeIn(right, shift=LEFT*.2), run_time=1.1)
        weighted = txt("G children = (2/6)(0) + (4/6)(0.375) = 0.25", 38, INK, "BOLD").move_to([0,-1.25,0])
        gain = txt("decrease = 0.5 − 0.25 = 0.25", 45, ACC, "BOLD").move_to([0,-2.15,0])
        self.play(Write(weighted), run_time=.9); self.play(Write(gain), run_time=.75); self.wait(5.15)


class B05_Scene(Base):
    actual_duration = 20.35
    def construct(self):
        self.play(FadeIn(spark("Threshold 3.5 wins the node.")), run_time=.5)
        row = sample_row(1.0).move_to([0,1.35,0]); self.play(FadeIn(row), run_time=.75)
        cut = DashedLine([0,2,0],[0,.65,0],color=ACC,stroke_width=7)
        self.play(Create(cut), run_time=.55)
        children = VGroup(card("LEFT", "A A A · Gini 0", 4.3, 1.35, ACC),
                          card("RIGHT", "B B B · Gini 0", 4.3, 1.35, INK)).arrange(RIGHT,buff=.85).move_to([0,-.15,0])
        self.play(FadeIn(children[0],shift=RIGHT*.18),FadeIn(children[1],shift=LEFT*.18),run_time=1.0)
        table = VGroup(card("t = 2.5", "decrease 0.25", 3.8, 1.2),
                       card("t = 3.5", "decrease 0.50 · WINNER", 4.5, 1.2, ACC)).arrange(RIGHT,buff=.55).move_to([0,-1.75,0])
        self.play(FadeIn(table[0]),FadeIn(table[1],scale=.88),run_time=1.05)
        self.play(Create(SurroundingRectangle(table[1],color=ACC,buff=.14,stroke_width=6)),run_time=.55); self.wait(5.05)


class B06_Scene(Base):
    actual_duration = 21.33
    def construct(self):
        self.play(FadeIn(spark("Best now is not best forever.")), run_time=.5)
        greedy = node("GREEDY ROOT", "best immediate decrease", ACC, 4.0).move_to([0,1.65,0])
        self.play(FadeIn(greedy,scale=.88),run_time=.7)
        level1 = VGroup(node("LEFT", "keep splitting", INK, 3.1),node("RIGHT", "keep splitting", INK, 3.1)).arrange(RIGHT,buff=2.1).move_to([0,.15,0])
        arrows = VGroup(*[Arrow(greedy.get_bottom(),n.get_top(),buff=.12,color=PALE,stroke_width=5) for n in level1])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.15),FadeIn(level1),run_time=1.1)
        leaves = VGroup(*[card(f"LEAF {i+1}","1–2 samples",2.15,1.0,WARN) for i in range(4)]).arrange(RIGHT,buff=.35).move_to([0,-1.35,0])
        leaf_arrows = VGroup(*[Arrow(level1[i//2].get_bottom(),leaves[i].get_top(),buff=.1,color=PALE,stroke_width=4) for i in range(4)])
        self.play(LaggedStart(*[GrowArrow(a) for a in leaf_arrows],lag_ratio=.08),LaggedStart(*[FadeIn(l,scale=.82) for l in leaves],lag_ratio=.1),run_time=1.35)
        controls = txt("MAX DEPTH · MIN SAMPLES · MIN GAIN · PRUNING",28,ACC,"BOLD").to_edge(DOWN,buff=.68)
        self.play(FadeIn(controls),FadeOut(leaves[1]),FadeOut(leaves[3]),run_time=.8)
        self.play(FadeIn(txt("VALIDATE THE WHOLE TREE", 31, WARN, "BOLD").move_to([0,-2.25,0])),run_time=.5); self.wait(4.2)
