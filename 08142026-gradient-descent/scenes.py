"""scenes.py — Manim scenes for claude-liam-gradient-descent.

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene;
warn #A44A32 only for the divergent case in B05). Schematic curves carry NO
invented axis units and NO fabricated loss numbers — loss is shown as height.
Text is Pango `Text` only (never Tex/MathTex) so these render without LaTeX.
No slant=ITALIC on multi-word text (Pango collapses spaces).

Scenes: B01_BigIdea B02_Landscape B03_StepDownhill B04_Gradient
        B05_LearningRate B06_LocalMinima
"""
from manim import *
import numpy as np

# ── Palette ───────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")   # the one terracotta accent
WARN  = ManimColor("#A44A32")   # divergence only (B05)
SOFT  = ManimColor("#6E6A57")
GHOST = ManimColor("#A8A491")
CARD  = ManimColor("#FFFFFF")


def _label(text, size=26, color=None, weight="NORMAL"):
    return Text(text, font_size=size, color=color or INK, weight=weight)


def _spark(text):
    """≤4-word serif line, top-left (SPARK-LINE LAW), with the terracotta spark."""
    star = Text("✦", font_size=26, color=ACC)
    line = Text(text, font="EB Garamond", font_size=34, color=INK)
    g = VGroup(star, line).arrange(RIGHT, buff=0.25).to_edge(UP, buff=0.82).to_edge(LEFT, buff=0.9)
    return g


# smooth single valley used by B02/B03/B04
def _valley(x):
    return 0.20 * x ** 2 + 0.4


# ─────────────────────────────────────────────────────────────────────────────
#  B01_BigIdea — the BLUF: loss (a tall bar) is driven down by a repeated nudge
# ─────────────────────────────────────────────────────────────────────────────
class B01_BigIdea(Scene):
    def construct(self):
        self.camera.background_color = BG
        spark = _spark("Make mistakes smaller.")
        self.play(FadeIn(spark), run_time=0.6)

        base_y = -2.6
        baseline = Line(LEFT * 5.4, RIGHT * 5.4, color=GHOST, stroke_width=2).move_to([0, base_y, 0])
        loss_lbl = _label("loss", size=30, color=SOFT).next_to([-3.6, base_y, 0], DOWN, buff=0.25)
        self.play(Create(baseline), FadeIn(loss_lbl), run_time=0.6)

        # the loss bar, tall
        def bar(h):
            b = Rectangle(width=1.5, height=h, color=ACC, fill_color=ACC,
                          fill_opacity=0.9, stroke_width=0)
            b.move_to([-3.6, base_y + h / 2, 0])
            return b

        heights = [5.0, 3.3, 2.0, 1.1, 0.5]
        b = bar(heights[0])
        self.play(GrowFromEdge(b, DOWN), run_time=0.7)

        # a downhill arrow sweeping down-right over the shrinking bar
        arrow = Arrow([-2.2, base_y + 4.6, 0], [4.6, base_y + 0.5, 0],
                      color=INK, stroke_width=6, buff=0.1, max_tip_length_to_length_ratio=0.06)
        self.play(Create(arrow), run_time=0.8)

        for h in heights[1:]:
            self.play(Transform(b, bar(h)), run_time=0.7)

        stamp = _label("×  thousands of steps", size=30, color=INK, weight="BOLD")
        stamp.move_to([2.1, base_y + 1.15, 0])   # inside the safe area, near the arrow's lower run
        self.play(Write(stamp), run_time=0.8)
        self.wait(1.2)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Landscape — height = loss; goal = low ground; fog hides the far map
# ─────────────────────────────────────────────────────────────────────────────
class B02_Landscape(Scene):
    def construct(self):
        self.camera.background_color = BG
        spark = _spark("Height is the loss.")
        self.play(FadeIn(spark), run_time=0.6)

        ax = Axes(x_range=[-5, 5, 1], y_range=[0, 6, 1], x_length=12.2, y_length=5.4,
                  axis_config={"color": GHOST, "stroke_width": 1.2, "include_tip": False,
                               "include_numbers": False}).shift(DOWN * 0.4)
        curve = ax.plot(_valley, x_range=[-4.9, 4.9], color=INK, stroke_width=5)
        self.play(Create(ax), run_time=0.5)
        self.play(Create(curve), run_time=1.3)

        # you are here — a marker high on the left shoulder
        px = -4.2
        dot = Dot(ax.input_to_graph_point(px, curve), color=INK, radius=0.13)
        here = _label("you are here", size=26, color=INK).next_to(dot, UP, buff=0.2)
        self.play(FadeIn(dot, scale=0.6), FadeIn(here), run_time=0.8)

        # valley floor glows
        low = Dot(ax.input_to_graph_point(0, curve), color=ACC, radius=0.16)
        low_lbl = _label("low loss", size=28, color=ACC, weight="BOLD").next_to(low, DOWN, buff=0.3)
        self.play(FadeIn(low, scale=0.6), FadeIn(low_lbl), run_time=0.8)

        self.wait(0.6)
        # fog wipes across the far (right) side of the map
        fog = Rectangle(width=6.6, height=6.2, fill_color=BG, fill_opacity=0.82,
                        stroke_width=0).move_to(ax.c2p(2.4, 3))
        fog_lbl = _label("you can't see the bottom", size=26, color=SOFT).move_to(ax.c2p(2.4, 3))
        self.play(FadeIn(fog), FadeIn(fog_lbl), run_time=1.1)
        self.wait(1.3)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_StepDownhill — measure the slope, step against it, look again (the loop)
# ─────────────────────────────────────────────────────────────────────────────
class B03_StepDownhill(Scene):
    def construct(self):
        self.camera.background_color = BG
        spark = _spark("Measure, step, repeat.")
        self.play(FadeIn(spark), run_time=0.6)

        ax = Axes(x_range=[-5, 5, 1], y_range=[0, 6, 1], x_length=12.2, y_length=5.4,
                  axis_config={"color": GHOST, "stroke_width": 1.2, "include_tip": False,
                               "include_numbers": False}).shift(DOWN * 0.4)
        curve = ax.plot(_valley, x_range=[-4.9, 4.9], color=INK, stroke_width=5)
        self.play(Create(ax), Create(curve), run_time=1.2)

        xs = [-4.2, -2.5, -1.3, -0.55, -0.2]
        ball = Dot(ax.input_to_graph_point(xs[0], curve), color=ACC, radius=0.17)
        self.play(FadeIn(ball, scale=0.6), run_time=0.5)

        def tangent_at(x):
            return TangentLine(curve, alpha=(x + 4.9) / 9.8, length=2.6, color=SOFT, stroke_width=5)

        def arrow_at(x):
            # downhill = toward the minimum at x=0; draw straight between two graph points
            x2 = min(max((x + 0.9) if x < 0 else (x - 0.9), -4.8), 4.8)
            return Arrow(ax.input_to_graph_point(x, curve),
                         ax.input_to_graph_point(x2, curve),
                         color=ACC, buff=0.05, stroke_width=6,
                         max_tip_length_to_length_ratio=0.4)

        tan = tangent_at(xs[0])
        arr = arrow_at(xs[0])
        self.play(Create(tan), run_time=0.6)
        self.play(GrowArrow(arr), run_time=0.5)

        for x in xs[1:]:
            new_tan, new_arr = tangent_at(x), arrow_at(x)
            self.play(ball.animate.move_to(ax.input_to_graph_point(x, curve)),
                      Transform(tan, new_tan), Transform(arr, new_arr), run_time=1.0)

        done = _label("which way is down — right here", size=28, color=INK)
        done.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(done), run_time=0.7)
        self.wait(1.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Gradient — steepest ascent; we step the opposite. Long arrow = steep.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Gradient(Scene):
    def construct(self):
        self.camera.background_color = BG
        spark = _spark("Which way is up?")
        self.play(FadeIn(spark), run_time=0.6)

        ax = Axes(x_range=[-5, 5, 1], y_range=[0, 6, 1], x_length=12.2, y_length=5.4,
                  axis_config={"color": GHOST, "stroke_width": 1.2, "include_tip": False,
                               "include_numbers": False}).shift(DOWN * 0.4)
        curve = ax.plot(_valley, x_range=[-4.9, 4.9], color=INK, stroke_width=5)
        self.play(Create(ax), Create(curve), run_time=1.1)

        def uphill(x, color):
            # uphill = away from the minimum at x=0; steeper ground => longer arrow
            x2 = min(max((x - 0.9) if x < 0 else (x + 0.9), -4.85), 4.85)
            return Arrow(ax.input_to_graph_point(x, curve),
                         ax.input_to_graph_point(x2, curve),
                         color=color, buff=0.05, stroke_width=6,
                         max_tip_length_to_length_ratio=0.4)

        def downhill(x, color):
            x2 = min(max((x + 0.9) if x < 0 else (x - 0.9), -4.8), 4.8)
            return Arrow(ax.input_to_graph_point(x, curve),
                         ax.input_to_graph_point(x2, curve),
                         color=color, buff=0.05, stroke_width=6,
                         max_tip_length_to_length_ratio=0.4)

        px = -3.4
        up = uphill(px, SOFT)
        up_lbl = _label("gradient = steepest up", size=26, color=SOFT).next_to(up, UP, buff=0.2)
        self.play(GrowArrow(up), FadeIn(up_lbl), run_time=0.9)
        self.wait(0.6)

        # flip to downhill terracotta — the opposite direction
        dn = downhill(px, ACC)
        dn_lbl = _label("step the opposite way", size=28, color=ACC, weight="BOLD").next_to(dn, DOWN, buff=0.2)
        self.play(Transform(up, dn), FadeTransform(up_lbl, dn_lbl), run_time=1.0)
        self.wait(0.6)

        # steep vs flat: the geometry makes steep ground a longer arrow, flat a stub
        steep = uphill(-4.4, INK)
        flat = uphill(-0.7, INK)
        steep_lbl = _label("steep → big step", size=24, color=INK).next_to(steep, UP, buff=0.15)
        flat_lbl = _label("flat → tiny step", size=24, color=INK).next_to(flat, RIGHT, buff=0.25)
        self.play(GrowArrow(steep), FadeIn(steep_lbl), run_time=0.8)
        self.play(GrowArrow(flat), FadeIn(flat_lbl), run_time=0.8)

        note = _label("a compass — direction, not destination", size=26, color=INK)
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_LearningRate — three step-sizes, same valley, side by side (held ≥2s)
# ─────────────────────────────────────────────────────────────────────────────
class B05_LearningRate(Scene):
    def construct(self):
        self.camera.background_color = BG
        spark = _spark("Step size is everything.")
        self.play(FadeIn(spark), run_time=0.6)

        def panel(cx, title, color):
            ax = Axes(x_range=[-3, 3, 1], y_range=[0, 4, 1], x_length=3.6, y_length=2.8,
                      axis_config={"color": GHOST, "stroke_width": 1.0, "include_tip": False,
                                   "include_numbers": False})
            ax.move_to([cx, -0.6, 0])
            g = ax.plot(lambda x: 0.42 * x ** 2 + 0.2, x_range=[-2.9, 2.9], color=INK, stroke_width=4)
            t = Text(title, font="EB Garamond", font_size=28, color=color).next_to(ax, UP, buff=0.35)
            return ax, g, t

        ax1, g1, t1 = panel(-4.4, "too small", GHOST)
        ax2, g2, t2 = panel(0.0, "too big", WARN)
        ax3, g3, t3 = panel(4.4, "just right", ACC)
        self.play(*[Create(a) for a in (ax1, ax2, ax3)],
                  *[Create(g) for g in (g1, g2, g3)],
                  *[FadeIn(t) for t in (t1, t2, t3)], run_time=1.4)

        f = lambda x: 0.42 * x ** 2 + 0.2

        # too small — inches down, stalls high
        small_xs = [-2.6, -2.25, -1.98, -1.78, -1.63]
        d1 = Dot(ax1.input_to_graph_point(small_xs[0], g1), color=GHOST, radius=0.11)
        # too big — overshoots, bounces HIGHER each time (diverges)
        big_xs = [-1.4, 1.9, -2.5, 2.8]
        d2 = Dot(ax2.input_to_graph_point(big_xs[0], g2), color=WARN, radius=0.11)
        # just right — a few clean steps into the valley
        good_xs = [-2.6, -1.2, -0.4, -0.05]
        d3 = Dot(ax3.input_to_graph_point(good_xs[0], g3), color=ACC, radius=0.12)
        self.play(FadeIn(d1), FadeIn(d2), FadeIn(d3), run_time=0.5)

        steps = max(len(small_xs), len(big_xs), len(good_xs))
        for i in range(1, steps):
            anims = []
            if i < len(small_xs):
                anims.append(d1.animate.move_to(ax1.input_to_graph_point(small_xs[i], g1)))
            if i < len(big_xs):
                anims.append(d2.animate.move_to(ax2.input_to_graph_point(big_xs[i], g2)))
            if i < len(good_xs):
                anims.append(d3.animate.move_to(ax3.input_to_graph_point(good_xs[i], g3)))
            self.play(*anims, run_time=0.9)

        # verdicts under each panel
        v1 = _label("crawls, never arrives", size=22, color=SOFT).next_to(ax1, DOWN, buff=0.3)
        v2 = _label("loss explodes ↑", size=22, color=WARN, weight="BOLD").next_to(ax2, DOWN, buff=0.3)
        v3 = _label("lands in the valley", size=22, color=ACC, weight="BOLD").next_to(ax3, DOWN, buff=0.3)
        self.play(FadeIn(v1), FadeIn(v2), FadeIn(v3), run_time=0.8)
        self.wait(1.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_LocalMinima — nearest bottom, not the lowest
# ─────────────────────────────────────────────────────────────────────────────
class B06_LocalMinima(Scene):
    def construct(self):
        self.camera.background_color = BG
        spark = _spark("Nearest, not lowest.")
        self.play(FadeIn(spark), run_time=0.6)

        def f(x):
            return (0.08 * x ** 2
                    - 0.60 * np.exp(-((x + 2.2) ** 2) / 0.8)   # shallow left well
                    - 0.90 * np.exp(-((x - 2.4) ** 2) / 0.8)   # deep right well
                    + 1.4)

        ax = Axes(x_range=[-5, 5, 1], y_range=[0, 2.4, 1], x_length=12.2, y_length=5.2,
                  axis_config={"color": GHOST, "stroke_width": 1.2, "include_tip": False,
                               "include_numbers": False}).shift(DOWN * 0.3)
        curve = ax.plot(f, x_range=[-4.6, 4.6], color=INK, stroke_width=5)
        self.play(Create(ax), Create(curve), run_time=1.4)

        # ball rolls from the left into the shallow left well and stops
        path_xs = [-3.9, -3.2, -2.6, -2.25, -2.2]
        ball = Dot(ax.input_to_graph_point(path_xs[0], curve), color=INK, radius=0.16)
        self.play(FadeIn(ball, scale=0.6), run_time=0.5)
        for x in path_xs[1:]:
            self.play(ball.animate.move_to(ax.input_to_graph_point(x, curve)), run_time=0.7)

        stuck = _label("slope = 0  →  done?", size=28, color=INK, weight="BOLD")
        stuck.next_to(ax.input_to_graph_point(-2.2, curve), UP, buff=0.5)
        self.play(FadeIn(stuck), run_time=0.8)
        self.wait(0.6)

        # the deeper global valley glows, unreached, one ridge over
        deep = Dot(ax.input_to_graph_point(2.4, curve), color=ACC, radius=0.18)
        deep_lbl = _label("deeper valley, never reached", size=26, color=ACC, weight="BOLD")
        deep_lbl.next_to(deep, DOWN, buff=0.35)
        self.play(FadeIn(deep, scale=0.5), FadeIn(deep_lbl), run_time=1.0)

        verdict = _label("local, not global", size=32, color=INK, weight="BOLD").to_edge(DOWN, buff=0.5)
        self.play(Write(verdict), run_time=0.9)
        self.wait(1.3)
