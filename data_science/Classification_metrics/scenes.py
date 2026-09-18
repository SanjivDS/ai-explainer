"""Native Manim illustrations for Precision vs Recall vs F1 Score."""
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
ACC = ManimColor("#D97757")
SOFT = ManimColor("#6E6A57")
PALE = ManimColor("#DED9CC")
WHITE = ManimColor("#FAF9F5")
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
    return VGroup(txt("✦", 28, ACC), txt(s, 42)).arrange(RIGHT, buff=.22).to_edge(UP, buff=.68).to_edge(LEFT, buff=.9)

def clock(scene, actual):
    factor = actual / 10.0
    play, wait = scene.play, scene.wait
    def p(*a, **k):
        k["run_time"] = k.get("run_time", 1.0) * factor
        return play(*a, **k)
    def w(d=1.0, *a, **k): return wait(d * factor, *a, **k)
    scene.play, scene.wait = p, w

def card(label, sub="", width=3.0, height=1.35, color=INK):
    box = RoundedRectangle(width=width, height=height, corner_radius=.16, color=color,
                           stroke_width=4, fill_color=WHITE, fill_opacity=.96)
    lines = [txt(label, 32, color, "BOLD")]
    if sub: lines.append(txt(sub, 23, SOFT))
    return VGroup(box, VGroup(*lines).arrange(DOWN, buff=.1).move_to(box))

def matrix_grid():
    cells = VGroup(*[Square(1.55, color=INK, stroke_width=3, fill_color=WHITE,
                            fill_opacity=.9).move_to([(c-.5)*1.55, (.5-r)*1.55, 0])
                     for r in range(2) for c in range(2)])
    labels = VGroup(
        txt("TP", 40, ACC, "BOLD").move_to(cells[0]), txt("FN", 40, WARN, "BOLD").move_to(cells[1]),
        txt("FP", 40, WARN, "BOLD").move_to(cells[2]), txt("TN", 40, SOFT, "BOLD").move_to(cells[3]))
    return VGroup(cells, labels)

class B01_ThreeQuestions(Scene):
    def construct(self):
        clock(self, 20.78); self.camera.background_color = BG
        matrix = matrix_grid().scale(.9).move_to([-3.9, -.15, 0])
        self.play(FadeIn(spark("Four metrics. Four questions.")), FadeIn(matrix, scale=.85), run_time=1.1)
        cards = VGroup(card("ACCURACY", "right overall", 3.0, 1.18),
                       card("PRECISION", "trust alerts", 3.0, 1.18, ACC),
                       card("RECALL", "catch positives", 3.0, 1.18),
                       card("F1", "balance P + R", 3.0, 1.18, ACC)).arrange_in_grid(rows=2, cols=2, buff=(.38,.42)).move_to([2.65, -.05, 0])
        arrows = VGroup(*[Arrow(matrix.get_right(), c.get_left(), buff=.18, color=PALE, stroke_width=5) for c in cards])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=.15), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT*.2) for c in cards], lag_ratio=.16), run_time=1.5)
        self.play(FadeIn(txt("CLASS BALANCE  ·  POSITIVE CLASS  ·  THRESHOLD  ·  COST", 28, SOFT, "BOLD").to_edge(DOWN, buff=.75)), run_time=.6); self.wait(5.0)

class B02_Denominators(Scene):
    def construct(self):
        clock(self, 22.49); self.camera.background_color = BG
        self.play(FadeIn(spark("Different denominators. Different questions.")), run_time=.7)
        matrix = matrix_grid().scale(1.05).move_to([-4.1, -.1, 0]); self.play(FadeIn(matrix), run_time=1.0)
        metrics = VGroup(card("ACCURACY", "(TP + TN) / ALL", 3.2, 1.25),
                         card("PRECISION", "TP / (TP + FP)", 3.2, 1.25, ACC),
                         card("RECALL", "TP / (TP + FN)", 3.2, 1.25),
                         card("F1", "2PR / (P + R)", 3.2, 1.25, ACC)).arrange_in_grid(rows=2, cols=2, buff=(.35,.4)).move_to([2.15, -.05, 0])
        col = SurroundingRectangle(VGroup(matrix[0][0], matrix[0][2]), color=ACC, buff=.12, stroke_width=7)
        row = SurroundingRectangle(VGroup(matrix[0][0], matrix[0][1]), color=INK, buff=.12, stroke_width=7)
        all_cells = SurroundingRectangle(matrix, color=SOFT, buff=.15, stroke_width=6)
        self.play(FadeIn(metrics[0], shift=LEFT*.2), Create(all_cells), run_time=.9)
        self.play(ReplacementTransform(all_cells, col), FadeIn(metrics[1], shift=LEFT*.2), run_time=.9)
        self.play(ReplacementTransform(col, row), FadeIn(metrics[2], shift=LEFT*.2), run_time=.9)
        self.play(FadeIn(metrics[3], shift=LEFT*.2), run_time=.8)
        self.play(FadeIn(txt("overall  ·  false alarms  ·  misses  ·  balance", 31, SOFT).to_edge(DOWN, buff=.75)), run_time=.6); self.wait(4.3)

class B03_WorkedExample(Scene):
    def construct(self):
        clock(self, 21.50); self.camera.background_color = BG
        self.play(FadeIn(spark("One matrix. Four summaries.")), run_time=.7)
        counts = VGroup(card("TP", "6", 2.25, 1.2, ACC), card("FN", "4", 2.25, 1.2, WARN),
                        card("FP", "2", 2.25, 1.2, WARN), card("TN", "88", 2.25, 1.2)).arrange(RIGHT, buff=.35).move_to([0, 1.25, 0])
        self.play(LaggedStart(*[FadeIn(c, scale=.85) for c in counts], lag_ratio=.12), run_time=1.4)
        scores = VGroup(card("ACCURACY", "94 / 100 = 0.94", 4.0, 1.35),
                        card("PRECISION", "6 / 8 = 0.75", 4.0, 1.35, ACC),
                        card("RECALL", "6 / 10 = 0.60", 4.0, 1.35),
                        card("F1", "≈ 0.667", 4.0, 1.35, ACC)).arrange_in_grid(rows=2, cols=2, buff=(.5,.38)).move_to([0, -1.0, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP*.18) for c in scores], lag_ratio=.16), run_time=2.2)
        self.play(FadeIn(txt("same predictions  ·  four different summaries", 29, SOFT).to_edge(DOWN, buff=.72)), run_time=.7); self.wait(4.5)

class B04_ThresholdSweep(Scene):
    def construct(self):
        clock(self, 21.57); self.camera.background_color = BG
        self.play(FadeIn(spark("The threshold chooses the operating point.")), run_time=.7)
        axis = NumberLine(x_range=[0, 1, .1], length=9.4, include_numbers=False, color=INK).move_to([0, 1.3, 0])
        axis_labels = VGroup(txt("0.0", 24, SOFT).next_to(axis.n2p(0), DOWN, buff=.14),
                             txt("SCORE", 24, SOFT, "BOLD").next_to(axis, DOWN, buff=.14),
                             txt("1.0", 24, SOFT).next_to(axis.n2p(1), DOWN, buff=.14))
        dots = VGroup(*[Dot(axis.n2p(v), radius=.13, color=ACC if v in [.91,.78,.66,.58] else SOFT) for v in [.95,.91,.78,.66,.58,.43,.31,.2,.08]])
        marker = Triangle(color=ACC, fill_color=ACC, fill_opacity=1).scale(.18).rotate(PI).next_to(axis.n2p(.82), UP, buff=.18)
        self.play(Create(axis), FadeIn(axis_labels), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=.05), FadeIn(marker), run_time=1.5)
        self.play(marker.animate.next_to(axis.n2p(.35), UP, buff=.18), run_time=1.5)
        plot = Axes(x_range=[0,1,.2], y_range=[0,1,.2], x_length=5.1, y_length=3.2, tips=False, axis_config={"color": INK}).move_to([0,-.9,0])
        curve = VMobject(color=ACC, stroke_width=7).set_points_as_corners([plot.c2p(x,y) for x,y in [(0,1),(.18,.94),(.38,.9),(.38,.76),(.62,.73),(.78,.58),(1,.42)]])
        self.play(Create(plot), Create(curve), run_time=1.8)
        self.play(FadeIn(txt("recall steps upward  ·  precision may fluctuate", 28, SOFT).to_edge(DOWN, buff=.75)), run_time=.6); self.wait(4.0)

class B05_HarmonicMean(Scene):
    def construct(self):
        clock(self, 20.57); self.camera.background_color = BG
        self.play(FadeIn(spark("Accuracy can hide the miss.")), run_time=.7)
        accuracy = card("ACCURACY", "94%", 4.2, 1.7, ACC).move_to([-3.25, .85, 0])
        recall = card("RECALL", "60%", 4.2, 1.7, WARN).move_to([3.25, .85, 0])
        self.play(FadeIn(accuracy, scale=.85), run_time=1.0)
        tn = VGroup(*[Square(.22, color=SOFT, fill_color=SOFT, fill_opacity=.8, stroke_width=0) for _ in range(22)]).arrange_in_grid(rows=2, cols=11, buff=.12).move_to([-3.25, -.75, 0])
        misses = VGroup(*[Circle(.25, color=WARN, fill_color=WARN, fill_opacity=.92) for _ in range(4)]).arrange(RIGHT, buff=.28).move_to([3.25, -.75, 0])
        self.play(LaggedStart(*[FadeIn(x) for x in tn], lag_ratio=.03), run_time=1.2)
        self.play(FadeIn(recall, scale=.85), LaggedStart(*[GrowFromCenter(x) for x in misses], lag_ratio=.15), run_time=1.2)
        self.play(FadeIn(txt("88 true negatives dominate", 27, SOFT).move_to([-3.25,-1.65,0])),
                  FadeIn(txt("4 of 10 positives missed", 27, WARN, "BOLD").move_to([3.25,-1.65,0])), run_time=.8)
        self.play(FadeIn(txt("CHECK CLASS BALANCE AND ERROR COST", 31, ACC, "BOLD").to_edge(DOWN, buff=.75)), run_time=.7); self.wait(4.2)

class B06_F1StressTest(Scene):
    def construct(self):
        clock(self, 22.63); self.camera.background_color = BG
        self.play(FadeIn(spark("F1 balances—then hides.")), run_time=.7)
        left = card("SYSTEM A", "TP 6 · FP 2 · FN 4 · TN 20", 5.0, 1.55).move_to([-3.0, 1.15, 0])
        right = card("SYSTEM B", "TP 6 · FP 2 · FN 4 · TN 2,000", 5.0, 1.55).move_to([3.0, 1.15, 0])
        self.play(FadeIn(left, shift=RIGHT*.2), FadeIn(right, shift=LEFT*.2), run_time=1.4)
        self.play(FadeIn(card("SAME BINARY F1", "0.667 · true negatives absent", 5.2, 1.45, ACC).move_to([0, -.45, 0]), scale=.86), run_time=1.0)
        caveats = VGroup(txt("UNEQUAL COSTS", 24, WARN, "BOLD"), txt("ZERO DIVISION", 24, WARN, "BOLD"), txt("MICRO · MACRO · PER CLASS", 24, WARN, "BOLD")).arrange(RIGHT, buff=.52).move_to([0, -1.75, 0])
        self.play(LaggedStart(*[FadeIn(x, shift=UP*.15) for x in caveats], lag_ratio=.2), run_time=1.5)
        self.play(FadeIn(txt("STATE THE POLICY BESIDE THE SCORE", 32, ACC, "BOLD").to_edge(DOWN, buff=.78)), run_time=.7); self.wait(4.5)
