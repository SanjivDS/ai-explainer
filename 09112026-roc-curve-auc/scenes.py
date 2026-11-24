"""Native Manim illustrations for ROC Curve and AUC Score, Oversimplified.

Everything is deterministic and Pango Text only. Safe area: |x| <= 6.3,
|y| <= 3.4. The six-case ranking P P N P N N is a schematic teaching
construction; its empirical AUC is exactly 8/9.
"""
from pathlib import Path
from contextlib import contextmanager
from manim import *
try:
    from manim import register_font
except (ImportError, ModuleNotFoundError):
    # The render-free gate replaces Manim with a geometry stub.
    @contextmanager
    def register_font(_font_file):
        yield

BG = ManimColor("#F2F0E9")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
WARN = ManimColor("#A44A32")
SOFT = ManimColor("#6E6A57")
GHOST = ManimColor("#A8A491")
WHITEISH = ManimColor("#FAF9F5")
SERIF = "EB Garamond"


def _bundled_serif():
    """Find the toolkit font even when a book is nested more deeply than usual."""
    for parent in (Path.cwd(), *Path(__file__).resolve().parents):
        candidate = parent / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"
        if candidate.exists():
            return candidate
    # Render-free QC imports an isolated copy, where no real font is needed.
    return Path.cwd() / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"


SERIF_FILE = _bundled_serif()


def txt(s, size=30, color=INK, weight="NORMAL"):
    # Register the bundled face in-process: a copied TTF is not reliably visible
    # to Manim/Pango until the macOS font cache refreshes.
    with register_font(SERIF_FILE):
        return Text(s, font=SERIF, font_size=size, color=color, weight=weight)


def spark(s):
    g = VGroup(txt("✦", 25, ACC), txt(s, 36)).arrange(RIGHT, buff=0.22)
    return g.to_edge(UP, buff=0.72).to_edge(LEFT, buff=0.9)


def cite(s):
    return txt(s, 21, GHOST).move_to([0, -3.15, 0])


def clock(scene, factor):
    """Scale all authored animation timings to the measured narration clock."""
    raw_play, raw_wait = scene.play, scene.wait

    def scaled_play(*animations, **kwargs):
        kwargs["run_time"] = kwargs.get("run_time", 1.0) * factor
        return raw_play(*animations, **kwargs)

    def scaled_wait(duration=1.0, *args, **kwargs):
        return raw_wait(duration * factor, *args, **kwargs)

    scene.play, scene.wait = scaled_play, scaled_wait


def roc_axes(origin=(-5.0, -2.15), size=4.35):
    ox, oy = origin
    x = Line([ox, oy, 0], [ox + size, oy, 0], color=INK, stroke_width=4)
    y = Line([ox, oy, 0], [ox, oy + size, 0], color=INK, stroke_width=4)
    labels = VGroup(
        txt("false positive rate", 24, SOFT).move_to([ox + size / 2, oy - 0.40, 0]),
        txt("true positive rate", 24, SOFT).rotate(PI / 2).move_to([ox - 0.55, oy + size / 2, 0]),
        txt("0", 22, SOFT).move_to([ox - 0.38, oy - 0.20, 0]),
        txt("1", 22, SOFT).move_to([ox + size, oy - 0.32, 0]),
        txt("1", 22, SOFT).move_to([ox - 0.28, oy + size, 0]),
    )
    return VGroup(x, y, labels)


def roc_point(x, y, origin=(-5.0, -2.15), size=4.35, color=ACC):
    return Dot([origin[0] + x * size, origin[1] + y * size, 0], radius=0.105, color=color)


def roc_poly(points, origin=(-5.0, -2.15), size=4.35, color=ACC):
    coords = [[origin[0] + x * size, origin[1] + y * size, 0] for x, y in points]
    return VMobject(color=color, stroke_width=7).set_points_as_corners(coords)


def pill(label, center, positive=True, scale=1.0):
    color = ACC if positive else INK
    box = RoundedRectangle(width=0.82 * scale, height=0.62 * scale,
                           corner_radius=0.18, color=color, stroke_width=4,
                           fill_color=WHITEISH, fill_opacity=0.9).move_to(center)
    mark = txt("P" if positive else "N", int(27 * scale), color, "BOLD").move_to(center)
    return VGroup(box, mark)


class B01_MapAndNumber(Scene):
    def construct(self):
        clock(self, 2.221)
        self.camera.background_color = BG
        s = spark("Map first. Number second.")
        self.play(FadeIn(s), run_time=0.5)

        # ranked score rail and moving threshold
        rail = Line([-5.55, 0.95, 0], [5.4, 0.95, 0], color=INK, stroke_width=5)
        cases = [(-4.7, True), (-3.0, True), (-1.3, False), (0.4, True), (2.1, False), (3.8, False)]
        marks = VGroup(*[pill("", [x, 1.55, 0], pos) for x, pos in cases])
        hi, lo = txt("higher score", 25, SOFT).move_to([-4.65, 2.16, 0]), txt("lower score", 25, SOFT).move_to([4.55, 2.16, 0])
        self.play(Create(rail), LaggedStart(*[FadeIn(m, scale=0.6) for m in marks], lag_ratio=0.08), FadeIn(hi), FadeIn(lo), run_time=1.4)
        threshold = Line([-5.30, 2.08, 0], [-5.30, 0.78, 0], color=ACC, stroke_width=8)
        th = txt("threshold", 25, ACC, "BOLD").next_to(threshold, DOWN, buff=0.12)
        self.play(FadeIn(threshold), FadeIn(th), run_time=0.4)
        self.play(threshold.animate.shift(RIGHT * 10.15), th.animate.shift(RIGHT * 10.15), run_time=2.2)

        caught = RoundedRectangle(width=3.35, height=1.18, corner_radius=0.15, color=INK).move_to([-2.0, -1.10, 0])
        alarms = RoundedRectangle(width=3.35, height=1.18, corner_radius=0.15, color=INK).move_to([2.0, -1.10, 0])
        c1 = txt("caught positives", 28).move_to([-2.0, -0.83, 0]); c2 = txt("false alarms", 28).move_to([2.0, -0.83, 0])
        n1 = txt("0  →  3", 39, ACC, "BOLD").move_to([-2.0, -1.32, 0]); n2 = txt("0  →  3", 39, ACC, "BOLD").move_to([2.0, -1.32, 0])
        self.play(Create(caught), Create(alarms), FadeIn(c1), FadeIn(c2), Write(n1), Write(n2), run_time=1.0)

        axes = roc_axes(origin=(-2.2, -2.8), size=2.25)
        points = [(0,0),(0,1/3),(0,2/3),(1/3,2/3),(1/3,1),(2/3,1),(1,1)]
        curve = roc_poly(points, origin=(-2.2, -2.8), size=2.25)
        self.play(FadeOut(VGroup(rail, marks, hi, lo, threshold, th, caught, alarms, c1, c2, n1, n2)), Create(axes), run_time=0.8)
        self.play(Create(curve), run_time=1.5)
        area = Polygon([-2.2,-2.8,0], [-2.2,-2.05,0], [-2.2,-1.3,0], [-1.45,-1.3,0], [-1.45,-0.55,0], [0.05,-0.55,0], [0.05,-2.8,0], color=ACC, fill_color=ACC, fill_opacity=0.18, stroke_width=0)
        auc = txt("AUC summarizes the ranking", 30, INK, "BOLD").move_to([3.00, -1.55, 0])
        policy = txt("threshold stays a separate decision", 25, SOFT).move_to([3.00, -2.35, 0])
        self.play(FadeIn(area), FadeIn(auc), FadeIn(policy), run_time=1.0)
        self.wait(1.2)


class B02_ThresholdFramework(Scene):
    def construct(self):
        clock(self, 2.654)
        self.camera.background_color = BG
        self.play(FadeIn(spark("One threshold. One point.")), run_time=0.5)
        ys = [2.15, 1.38, 0.61, -0.16, -0.93, -1.70]
        kinds = [True, True, False, True, False, False]
        stack = VGroup(*[pill("", [-4.75, y, 0], p, 0.9) for y, p in zip(ys, kinds)])
        score = txt("score ↓", 25, SOFT).move_to([-5.55, 0.2, 0])
        threshold = Line([-5.45, 0.2, 0], [-4.05, 0.2, 0], color=ACC, stroke_width=7)
        self.play(LaggedStart(*[FadeIn(m) for m in stack], lag_ratio=0.1), FadeIn(score), Create(threshold), run_time=1.2)

        tpr_box = RoundedRectangle(width=3.2, height=1.28, corner_radius=0.14, color=INK).move_to([-1.7, 1.2, 0])
        fpr_box = RoundedRectangle(width=3.2, height=1.28, corner_radius=0.14, color=INK).move_to([-1.7, -0.65, 0])
        tpr = VGroup(txt("TPR", 37, ACC, "BOLD"), txt("caught P / all P", 26)).arrange(DOWN, buff=0.12).move_to(tpr_box)
        fpr = VGroup(txt("FPR", 37, ACC, "BOLD"), txt("false alarms / all N", 26)).arrange(DOWN, buff=0.12).move_to(fpr_box)
        self.play(Create(tpr_box), FadeIn(tpr), Create(fpr_box), FadeIn(fpr), run_time=1.2)
        coord = txt("( FPR , TPR )", 34, INK, "BOLD").move_to([0.85, 0.28, 0])
        a1 = Arrow([-0.05,1.2,0], [0.65,0.55,0], color=ACC, buff=0.1); a2 = Arrow([-0.05,-0.65,0], [0.65,0.02,0], color=ACC, buff=0.1)
        self.play(GrowArrow(a1), GrowArrow(a2), FadeIn(coord), run_time=0.9)

        axes = roc_axes(origin=(3.15, -1.8), size=3.05)
        pts = [(0,0),(0,1/3),(0,2/3),(1/3,2/3),(1/3,1),(2/3,1),(1,1)]
        dots = [roc_point(x,y,origin=(3.15,-1.8),size=3.05) for x,y in pts]
        curve = roc_poly(pts, origin=(3.15,-1.8), size=3.05)
        self.play(Create(axes), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), Create(curve), run_time=1.6)
        self.play(FadeIn(cite("Definitions: scikit-learn roc_curve · binary classification")), run_time=0.6)
        self.wait(1.2)


class B03_SixCaseWalk(Scene):
    def construct(self):
        clock(self, 2.402)
        self.camera.background_color = BG
        framework = txt("threshold → counts → ( FPR , TPR )", 31, SOFT).move_to([0, 3.02, 0])
        self.play(FadeIn(framework), run_time=0.5)
        axes = roc_axes(origin=(-5.25, -2.25), size=4.45)
        self.play(Create(axes), run_time=0.7)

        order = [True, True, False, True, False, False]
        labels = VGroup(*[pill("", [1.35 + i * 0.84, 1.85, 0], p, 0.82) for i,p in enumerate(order)])
        rank = txt("higher score   →   lower score", 25, SOFT).move_to([3.45, 2.5, 0])
        self.play(FadeIn(rank), LaggedStart(*[FadeIn(x) for x in labels], lag_ratio=0.09), run_time=1.1)
        pts = [(0,0),(0,1/3),(0,2/3),(1/3,2/3),(1/3,1),(2/3,1),(1,1)]
        curve = roc_poly(pts, origin=(-5.25,-2.25), size=4.45)
        cursor = Line([1.0,2.35,0],[1.0,1.34,0],color=ACC,stroke_width=7)
        self.play(FadeIn(cursor), FadeIn(roc_point(0,0,origin=(-5.25,-2.25),size=4.45)), run_time=0.4)
        self.play(cursor.animate.shift(RIGHT*5.15), Create(curve), run_time=2.5)

        grid = VGroup()
        for r in range(3):
            for c in range(3):
                good = not (r == 2 and c == 0)
                box = RoundedRectangle(width=0.82,height=0.62,corner_radius=0.1,
                                       color=ACC if good else WARN, stroke_width=3,
                                       fill_color=ACC if good else WARN, fill_opacity=0.14)
                box.move_to([2.35+c*1.03, 0.45-r*0.82, 0])
                mark = txt("✓" if good else "×", 27, ACC if good else WARN, "BOLD").move_to(box)
                grid.add(VGroup(box,mark))
        cap = txt("positive × negative pairs", 27, SOFT).move_to([3.38,0.98,0])
        total = txt("8 correct  ·  1 inversion", 34, INK, "BOLD").move_to([3.38,-2.18,0])
        self.play(FadeOut(cursor), FadeIn(cap), LaggedStart(*[FadeIn(x) for x in grid], lag_ratio=0.06), run_time=1.2)
        self.play(FadeIn(total), run_time=0.6)
        self.play(FadeIn(cite("Schematic six-case example · exact pair count shown")), run_time=0.5)
        self.wait(1.3)


class B04_AreaMeansRanking(Scene):
    def construct(self):
        clock(self, 3.154)
        self.camera.background_color = BG
        self.play(FadeIn(spark("AUC judges the ranking.")), run_time=0.5)
        wrong = txt("percent correct", 48, SOFT).move_to([-3.65, 1.95, 0])
        right = txt("pair ranking", 52, INK, "BOLD").move_to([3.35, 1.95, 0])
        self.play(FadeIn(wrong), run_time=0.5)
        self.play(wrong.animate.set_color(WARN), TransformFromCopy(wrong, right), run_time=0.8)

        pair = VGroup(pill("",[-4.2,0.42,0],True,1.15), txt("score 0.82",27).move_to([-4.2,-0.35,0]),
                      txt(">",44,ACC,"BOLD").move_to([-2.8,0.4,0]),
                      pill("",[-1.45,0.42,0],False,1.15), txt("score 0.41",27).move_to([-1.45,-0.35,0]))
        self.play(LaggedStart(*[FadeIn(x) for x in pair],lag_ratio=0.1),run_time=1.1)

        grid = VGroup()
        for r in range(3):
            for c in range(3):
                good = not (r == 2 and c == 0)
                sq = Square(0.57,color=ACC if good else WARN,stroke_width=3,
                            fill_color=ACC if good else WARN,fill_opacity=0.18)
                sq.move_to([1.25+c*0.76,0.76-r*0.76,0])
                grid.add(VGroup(sq,txt("✓" if good else "×",23,ACC if good else WARN,"BOLD").move_to(sq)))
        calc = txt("8 ÷ 9  =  0.89", 45, INK, "BOLD").move_to([-2.70,-1.35,0])
        self.play(LaggedStart(*[FadeIn(x) for x in grid],lag_ratio=0.05),FadeIn(calc),run_time=1.1)

        line = Line([-4.8,-2.25,0],[4.8,-2.25,0],color=INK,stroke_width=5)
        r = Dot([-4.8,-2.25,0],color=GHOST,radius=0.12); e = Dot([4.8,-2.25,0],color=ACC,radius=0.12)
        lab1=txt("0.5  random",28,SOFT).next_to(r,UP,buff=0.18); lab2=txt("1.0  perfect",28,ACC,"BOLD").next_to(e,UP,buff=0.18)
        here=Dot([2.69,-2.25,0],color=ACC,radius=0.16); lab3=txt("0.89",30,INK,"BOLD").next_to(here,DOWN,buff=0.16)
        self.play(Create(line),FadeIn(r),FadeIn(e),FadeIn(here),FadeIn(lab1),FadeIn(lab2),FadeIn(lab3),run_time=1.0)
        self.play(FadeIn(cite("AUC pair-ranking interpretation: Google ML Crash Course")),run_time=0.5)
        self.wait(1.3)


class B05_OperatingPoint(Scene):
    def construct(self):
        clock(self, 3.348)
        self.camera.background_color = BG
        self.play(FadeIn(spark("The curve needs a policy.")), run_time=0.5)
        axes = roc_axes(origin=(-5.55,-2.2),size=4.45)
        pts=[(0,0),(0.04,0.38),(0.13,0.7),(0.3,0.86),(0.58,0.96),(1,1)]
        curve=roc_poly(pts,origin=(-5.55,-2.2),size=4.45)
        choices=VGroup(roc_point(.04,.38,origin=(-5.55,-2.2),size=4.45),roc_point(.13,.7,origin=(-5.55,-2.2),size=4.45),roc_point(.3,.86,origin=(-5.55,-2.2),size=4.45))
        self.play(Create(axes),Create(curve),LaggedStart(*[FadeIn(x) for x in choices],lag_ratio=.18),run_time=1.5)

        screen = RoundedRectangle(width=5.0,height=1.55,corner_radius=.16,color=INK).move_to([3.25,1.15,0])
        queue = RoundedRectangle(width=5.0,height=1.55,corner_radius=.16,color=INK).move_to([3.25,-1.05,0])
        st=VGroup(txt("DISEASE SCREEN",25,SOFT,"BOLD"),txt("protect recall",39,INK,"BOLD"),txt("accept more false alarms",26,SOFT)).arrange(DOWN,buff=.1).move_to(screen)
        qt=VGroup(txt("MANUAL REVIEW",25,SOFT,"BOLD"),txt("protect capacity",39,INK,"BOLD"),txt("inspect the far-left slice",26,SOFT)).arrange(DOWN,buff=.1).move_to(queue)
        self.play(Create(screen),FadeIn(st),Create(queue),FadeIn(qt),run_time=1.2)
        a1=Arrow([.1,1.3,0],[.75,1.3,0],color=ACC,buff=.05); a2=Arrow([-.75,-.9,0],[.75,-.9,0],color=ACC,buff=.05)
        self.play(GrowArrow(a1),GrowArrow(a2),run_time=.7)
        policy=VGroup(txt("cost",30),txt("+",28,SOFT),txt("capacity",30),txt("+",28,SOFT),txt("prevalence",30)).arrange(RIGHT,buff=.25).move_to([3.15,-2.65,0])
        self.play(FadeIn(policy),run_time=.8)
        self.wait(1.4)


class B06_DeploymentStressTest(Scene):
    def construct(self):
        clock(self, 3.479)
        self.camera.background_color = BG
        self.play(FadeIn(spark("Ranking is not deployment.")),run_time=.5)
        badge=RoundedRectangle(width=3.2,height=1.15,corner_radius=.2,color=ACC,stroke_width=5,fill_color=ACC,fill_opacity=.14).move_to([0,1.95,0])
        btxt=txt("AUC  0.89",48,ACC,"BOLD").move_to(badge)
        self.play(Create(badge),FadeIn(btxt),run_time=.8)

        names=[("CALIBRATION","scores misstate risk"),("CAPACITY","queue overflows"),("SUBGROUP","group falls behind")]
        panels=VGroup()
        for i,(head,body) in enumerate(names):
            x=-4.25+i*4.25
            box=RoundedRectangle(width=3.55,height=2.05,corner_radius=.16,color=INK,stroke_width=4,fill_color=WHITEISH,fill_opacity=.7).move_to([x,-.15,0])
            h=txt(head,25,SOFT,"BOLD").move_to([x,.42,0]); body_t=txt(body,23,INK,"BOLD").move_to([x,-.12,0]); fail=txt("×",45,WARN,"BOLD").move_to([x,-.72,0])
            panels.add(VGroup(box,h,body_t,fail))
        self.play(LaggedStart(*[FadeIn(p,shift=UP*.18) for p in panels],lag_ratio=.18),run_time=1.4)
        self.play(Indicate(badge,color=ACC),run_time=.7)

        strip=VGroup(*[pill("",[-4.9+i*.62,-2.22,0],i==1,.58) for i in range(8)])
        pr=txt("also inspect precision–recall",30,INK,"BOLD").move_to([3.0,-2.22,0])
        self.play(LaggedStart(*[FadeIn(x) for x in strip],lag_ratio=.03),FadeIn(pr),run_time=1.0)
        verdict=txt("separation evidence — not safety",33,ACC,"BOLD").move_to([0,-3.05,0])
        self.play(FadeOut(VGroup(strip,pr)),Transform(btxt,verdict),FadeOut(badge),run_time=1.0)
        self.wait(1.4)
