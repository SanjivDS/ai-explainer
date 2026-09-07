"""Native schematic scenes for L1 Regularization (Lasso).

Layout contract (audited by runtime/qc/manim_layout_audit.py --curve-strict):
  * safe area is +/-6.3 x, +/-3.4 y — every Text stays inside it
  * the spark line owns the top-left strip (y ~ 2.75..3.25); content stays below y 2.4
  * bars/panels carry stroke_opacity=0 so they can never "strike" a label
  * labels on plot beats live OFF the curve, in reserved clear space
"""
from manim import *
import numpy as np

BG = ManimColor("#F2F0E9")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
SOFT = ManimColor("#777261")
GHOST = ManimColor("#B9B4A4")


def txt(s, n=32, c=INK, w="NORMAL"):
    return Text(s, font_size=n, color=c, weight=w)


def spark(s):
    """Top-left spark + one short serif line (<=4 words)."""
    return VGroup(
        Text("✦", font_size=28, color=ACC),
        Text(s, font="EB Garamond", font_size=38, color=INK),
    ).arrange(RIGHT, buff=.2).to_edge(UP, buff=.75).to_edge(LEFT, buff=.9)


def bar(length, y, x0=-4.3, color=INK, h=.34):
    """A filled coefficient bar. stroke_opacity=0 keeps it out of the stroke audit."""
    L = max(float(length), 1e-3)
    r = Rectangle(width=L, height=h, fill_color=color, fill_opacity=1, stroke_opacity=0)
    r.move_to([x0 + L / 2.0, y, 0])
    return r


def card(tag, body, w, h, tag_fs=24, body_fs=26):
    """Bordered card: terracotta tag over ink body, arranged so they cannot overlap."""
    r = RoundedRectangle(width=w, height=h, corner_radius=.18, color=GHOST, stroke_width=2)
    inner = VGroup(
        txt(tag, tag_fs, ACC, "BOLD"),
        txt(body, body_fs, INK),
    ).arrange(DOWN, buff=.20).move_to(r.get_center())
    return VGroup(r, inner)


class BeatScene(Scene):
    """Timeline-aware scene.

    `T` is the beat's measured narration length (audio is the master clock), so each
    scene renders at its true beat duration and the compiler never has to slow the
    clip down to fill. `at(frac)` holds until a fraction of the beat has elapsed,
    which is how the beat sheet's `show` events land on the spoken word.
    """

    T = 20.0

    def _now(self):
        return float(getattr(getattr(self, "renderer", None), "time", 0.0) or 0.0)

    def at(self, frac):
        dt = (frac * self.T) - self._now()
        if dt > 0.02:
            self.wait(dt)

    def finish(self):
        dt = self.T - self._now()
        if dt > 0.02:
            self.wait(dt)


# ─────────────────────────────────────────────────────────── B01 · executive summary
class B01_ShrinkAndSelect(BeatScene):
    """Coefficients shrink; two of them land on exactly zero."""

    T = 19.65

    def construct(self):
        self.camera.background_color = BG
        names = ["income", "balance", "tenure", "age", "zip-code"]
        before = [3.10, 2.40, 1.70, 1.10, 0.60]
        after = [2.20, 1.60, 0.00, 0.55, 0.00]
        rows = [1.25, 0.50, -0.25, -1.00, -1.75]
        SCALE = 1.75

        head_l = txt("COEFFICIENT SIZE", 27, SOFT, "BOLD").move_to([-1.45, 2.15, 0])
        head_r = txt("VALUE", 27, SOFT, "BOLD").move_to([5.30, 2.15, 0])
        labels = VGroup(*[txt(n, 26).move_to([-5.30, y, 0]) for n, y in zip(names, rows)])
        bars_b = VGroup(*[bar(v * SCALE, y) for v, y in zip(before, rows)])
        vals_b = VGroup(*[txt(f"{v:.2f}", 26, SOFT).move_to([5.30, y, 0]) for v, y in zip(before, rows)])

        self.play(FadeIn(spark("Shrink some. Zero others.")),
                  FadeIn(head_l), FadeIn(head_r), FadeIn(labels), run_time=1.4)
        self.at(0.20)
        self.play(*[GrowFromEdge(b, LEFT) for b in bars_b], FadeIn(vals_b), run_time=1.6)

        bars_a = VGroup(*[bar(v * SCALE, y, color=INK if v > 0 else ACC)
                          for v, y in zip(after, rows)])
        vals_a = VGroup(*[txt(f"{v:.2f}", 26, ACC if v == 0 else SOFT, "BOLD" if v == 0 else "NORMAL")
                          .move_to([5.30, y, 0]) for v, y in zip(after, rows)])
        dropped = VGroup(*[txt("dropped", 24, ACC, "BOLD").move_to([-2.85, rows[i], 0])
                           for i, v in enumerate(after) if v == 0])

        self.at(0.50)
        self.play(Transform(bars_b, bars_a), Transform(vals_b, vals_a), run_time=2.4)
        self.at(0.72)
        self.play(FadeIn(dropped), run_time=1.0)
        footer = txt("two features removed — not just reduced", 30, ACC, "BOLD").move_to([0, -2.90, 0])
        self.at(0.90)
        self.play(Write(footer), run_time=1.2)
        self.finish()


# ───────────────────────────────────────────────────────────────── B02 · the objective
class B02_Objective(BeatScene):
    """One score = data fit + L1 penalty."""

    T = 19.70

    def construct(self):
        self.camera.background_color = BG
        a = card("DATA FIT", "squared error", 5.0, 1.9, 26, 30).move_to([-3.10, 1.30, 0])
        plus = txt("+", 46, SOFT, "BOLD").move_to([0, 1.30, 0])
        b = card("L1 PENALTY", "lambda × total |weight|", 5.0, 1.9, 26, 28).move_to([3.10, 1.30, 0])
        arrow = Arrow([0, 0.20, 0], [0, -0.60, 0], buff=0, color=SOFT)
        res = card("MINIMIZE", "the sum of both, together", 9.6, 1.5, 24, 32).move_to([0, -1.50, 0])
        footer = txt("more penalty  →  simpler model", 30, ACC, "BOLD").move_to([0, -2.95, 0])

        self.play(FadeIn(spark("One score. Two jobs.")), run_time=1.2)
        self.at(0.20)
        self.play(FadeIn(a), run_time=1.3)
        self.at(0.42)
        self.play(FadeIn(plus), FadeIn(b), run_time=1.4)
        self.at(0.68)
        self.play(Create(arrow), FadeIn(res), run_time=1.5)
        self.at(0.88)
        self.play(Write(footer), run_time=1.2)
        self.finish()


# ────────────────────────────────────────────────────────── B03 · why exact zeros
class B03_TheCorner(BeatScene):
    """L1's diamond has corners on the axes; L2's circle does not."""

    T = 19.90

    def construct(self):
        self.camera.background_color = BG
        cl, cr, cy = -3.60, 3.20, -0.30
        R = 1.30

        diamond = Polygon([cl, cy + R, 0], [cl + R, cy, 0], [cl, cy - R, 0], [cl - R, cy, 0],
                          color=INK, stroke_width=5)
        circle = Circle(radius=R, color=INK, stroke_width=5).move_to([cr, cy, 0])
        ax_l = VGroup(Line([cl - 1.75, cy, 0], [cl + 1.75, cy, 0], color=GHOST, stroke_width=2),
                      Line([cl, cy - 1.75, 0], [cl, cy + 1.75, 0], color=GHOST, stroke_width=2))
        ax_r = VGroup(Line([cr - 1.75, cy, 0], [cr + 1.75, cy, 0], color=GHOST, stroke_width=2),
                      Line([cr, cy - 1.75, 0], [cr, cy + 1.75, 0], color=GHOST, stroke_width=2))

        # loss contour touching the diamond's right-hand corner -> the other weight is 0
        cont_l = Ellipse(width=2.0, height=1.4, color=ACC, stroke_width=4).move_to([cl + R + 1.00, cy + 0.12, 0])
        # loss contour meeting the circle on a smooth arc -> both weights merely small
        cont_r = Ellipse(width=2.0, height=1.4, color=ACC, stroke_width=4).move_to([cr + 1.85, cy + 0.92, 0])

        hit_l = Dot([cl + R, cy, 0], radius=.11, color=ACC)
        hit_r = Dot([cr + R * 0.72, cy + R * 0.70, 0], radius=.11, color=ACC)

        head_l = txt("L1 · absolute value", 30, INK, "BOLD").move_to([cl, 2.20, 0])
        head_r = txt("L2 · squared value", 30, INK, "BOLD").move_to([cr, 2.20, 0])
        cap_l = txt("meets a corner → exactly zero", 28, ACC, "BOLD").move_to([cl, -2.85, 0])
        cap_r = txt("meets a smooth edge → just small", 28, SOFT).move_to([cr, -2.85, 0])

        self.play(FadeIn(spark("The corner is everything.")), run_time=1.0)
        self.at(0.16)
        self.play(FadeIn(head_l), FadeIn(head_r), run_time=1.2)
        self.at(0.36)
        self.play(Create(ax_l), Create(ax_r), Create(diamond), Create(circle), run_time=1.8)
        self.at(0.58)
        self.play(Create(cont_l), Create(cont_r), run_time=1.5)
        self.at(0.76)
        self.play(FadeIn(hit_l), FadeIn(hit_r), run_time=0.8)
        self.at(0.90)
        self.play(Write(cap_l), Write(cap_r), run_time=1.4)
        self.finish()


# ────────────────────────────────────────────────────── B04 · the regularization path
class B04_Path(BeatScene):
    """As the penalty grows, coefficients hit exactly zero one at a time."""

    T = 16.40

    def construct(self):
        self.camera.background_color = BG
        ax = Axes(x_range=[0, 10, 1], y_range=[-1.2, 3.2, 1], x_length=9.4, y_length=4.4,
                  axis_config={"color": GHOST, "include_tip": False, "include_numbers": False}
                  ).move_to([0.40, -0.35, 0])

        starts = [3.00, 2.20, 1.40, -0.90]
        zeros = [9.0, 6.5, 4.0, 2.5]
        names = ["income", "balance", "tenure", "zip-code"]

        def path_fn(s, z):
            return lambda x: s * (1 - x / z) if x < z else 0.0

        curves = VGroup(*[ax.plot(path_fn(s, z), x_range=[0, 10, .05], color=INK, stroke_width=4)
                          for s, z in zip(starts, zeros)])
        # labels sit LEFT of the y-axis, clear of every curve
        tags = VGroup(*[txt(n, 24, SOFT).move_to([-5.35, s - 1.35, 0]) for n, s in zip(names, starts)])
        hits = VGroup(*[Dot(ax.c2p(z, 0), radius=.10, color=ACC) for z in zeros])
        note = txt("each one lands on exactly zero", 28, ACC, "BOLD").move_to([3.30, 2.30, 0])
        xlab = txt("small penalty", 24, SOFT).move_to([-3.20, -3.05, 0])
        xlab2 = txt("large penalty", 24, SOFT).move_to([3.90, -3.05, 0])

        self.play(FadeIn(spark("Watch them drop out.")), run_time=1.0)
        self.at(0.18)
        self.play(Create(ax), FadeIn(tags), run_time=1.6)
        self.at(0.45)
        self.play(*[Create(c) for c in curves], run_time=2.4)
        self.at(0.72)
        self.play(FadeIn(hits), run_time=0.9)
        self.at(0.88)
        self.play(Write(note), FadeIn(xlab), FadeIn(xlab2), run_time=1.4)
        self.finish()


# ─────────────────────────────────────────────────────────────── B05 · choosing lambda
class B05_ChooseLambda(BeatScene):
    """Validation error is U-shaped; cross-validation picks the bottom."""

    T = 18.45

    def construct(self):
        self.camera.background_color = BG
        ax = Axes(x_range=[0, 10, 1], y_range=[0, 10, 1], x_length=9.0, y_length=3.6,
                  axis_config={"color": GHOST, "include_tip": False, "include_numbers": False}
                  ).move_to([0.20, -0.15, 0])
        u = ax.plot(lambda x: 2.2 + 0.28 * (x - 4.2) ** 2, x_range=[0.4, 9.2, .05],
                    color=INK, stroke_width=5)
        best = Dot(ax.c2p(4.2, 2.2), radius=.13, color=ACC)
        drop = DashedLine(ax.c2p(4.2, 2.2), ax.c2p(4.2, 0), color=ACC, stroke_width=3)

        note = txt("lowest validation error", 30, ACC, "BOLD").move_to([3.60, 2.15, 0])
        ylab = txt("validation error", 22, SOFT).rotate(PI / 2).move_to([-4.90, 0.20, 0])
        lo = txt("small penalty", 26, SOFT).move_to([-3.40, -2.50, 0])
        hi = txt("large penalty", 26, SOFT).move_to([3.80, -2.50, 0])
        foot = txt("standardize features first", 28, SOFT).move_to([0, -3.10, 0])

        self.play(FadeIn(spark("Tune it. Don't guess.")), run_time=1.0)
        self.at(0.20)
        self.play(Create(ax), FadeIn(ylab), run_time=1.5)
        self.at(0.45)
        self.play(Create(u), run_time=1.9)
        self.at(0.66)
        self.play(FadeIn(best), Create(drop), run_time=1.1)
        self.at(0.82)
        self.play(Write(note), FadeIn(lo), FadeIn(hi), run_time=1.3)
        self.at(0.94)
        self.play(FadeIn(foot), run_time=1.0)
        self.finish()


# ─────────────────────────────────────────────────────────────── B06 · falsifiability
class B06_EdgeCases(BeatScene):
    """Four ways the sparsity story breaks."""

    T = 20.35

    def construct(self):
        self.camera.background_color = BG
        specs = [
            ("CORRELATED TWINS", "keeps one, drops its twin"),
            ("UNSTABLE PICKS", "resample, get a new subset"),
            ("SHRINKAGE BIAS", "survivors are pulled down"),
            ("NOT CAUSATION", "selected is not the same as true"),
        ]
        cards = VGroup(*[card(t, b, 5.60, 2.30, 24, 26) for t, b in specs])
        cards.arrange_in_grid(rows=2, cols=2, buff=.38).move_to([0, -0.40, 0])

        self.play(FadeIn(spark("Where sparsity lies.")), run_time=1.1)
        for frac, c in zip((0.25, 0.45, 0.65, 0.85), cards):
            self.at(frac)
            self.play(FadeIn(c), run_time=1.1)
        self.finish()


# ─────────────────────────────────────────────────────────────────────── B07 · verdict
class B07_Verdict(BeatScene):
    """The one-page recap."""

    T = 19.40

    def construct(self):
        self.camera.background_color = BG
        board = RoundedRectangle(width=11.7, height=5.8, corner_radius=.22, color=GHOST,
                                 fill_color=WHITE, fill_opacity=.72, stroke_width=2).move_to([0, -0.25, 0])
        title = txt("Shrink, then select", 52, INK, "BOLD").move_to([0, 2.05, 0])
        rows = [
            ("SHRINK", "every weight is pulled toward zero"),
            ("SELECT", "some weights land exactly on zero"),
            ("TUNE", "cross-validate lambda, scale first"),
            ("CHECK", "correlated picks stay unstable"),
        ]
        self.play(FadeIn(spark("The verdict.")), Create(board), Write(title), run_time=1.6)
        for i, ((head, body), frac) in enumerate(zip(rows, (0.30, 0.50, 0.70, 0.90))):
            y = 0.85 - i * 1.05
            tag = txt(head, 27, ACC, "BOLD").move_to([-4.55, y, 0])
            copy = txt(body, 30).move_to([1.05, y, 0])
            rule = Line([-5.35, y - .44, 0], [5.35, y - .44, 0], color=GHOST, stroke_width=2)
            self.at(frac)
            self.play(Create(rule), Write(tag), Write(copy), run_time=1.0)
        self.finish()


# ───────────────────────────────────────────────────────────────────────── B09 · outro
class B09_Outro(BeatScene):
    """Locked title-restate card."""

    T = 8.00

    def construct(self):
        self.camera.background_color = BG
        field = RoundedRectangle(width=12.0, height=6.25, corner_radius=.28, color=INK,
                                 fill_color=INK, fill_opacity=.98, stroke_width=0)
        mark = Text("NBB", font="EB Garamond", font_size=112, color=ACC, weight="BOLD").move_to([0, 1.70, 0])
        title = Text("L1 Regularization.", font="EB Garamond", font_size=74, color=BG,
                     weight="BOLD").move_to([0, -0.10, 0])
        rule = Line([-3.8, -1.15, 0], [3.8, -1.15, 0], color=ACC, stroke_width=5)
        handle = txt("@NikBearBrown", 38, BG, "BOLD").move_to([0, -1.80, 0])

        self.play(FadeIn(field), FadeIn(mark, scale=.75), run_time=1.0)
        self.at(0.40)
        self.play(Write(title), Create(rule), run_time=1.4)
        self.at(0.75)
        self.play(Write(handle), run_time=.8)
        self.finish()
