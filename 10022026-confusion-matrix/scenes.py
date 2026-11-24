"""Native-4K Confusion Matrix teaching diagrams. Data: evidence/result.json (from evidence/example.py)."""
import json, re
from pathlib import Path
from manim import *

R = Path(__file__).parent
BS = json.loads((R / 'beat_sheet.json').read_text())
D = json.loads((R / 'evidence/result.json').read_text())
M, L = D['model'], D['lazy']
BG = '#FAF9F5'; INK = '#3D3929'; ACC = '#D97757'; SOFT = '#625E50'; LINE = '#888271'; TINT = '#F1EEE6'
FONTS = Path(__file__).resolve().parents[4] / 'runtime/fonts/EB_Garamond/static'


def text(s, size=40, color=INK, weight=NORMAL):
    with register_font(str(FONTS / 'EBGaramond-Regular.ttf')), register_font(str(FONTS / 'EBGaramond-Medium.ttf')):
        return Text(s, font='EB Garamond', font_size=size, color=color, weight=weight).set_z_index(2)


def num(s, size=72, color=INK):
    return text(s, size, color, MEDIUM)


def frac(n, d, size=58, color=INK):
    """A real fraction: grouped numerator over a rule over the denominator."""
    top, bot = num(str(n), size, color), num(str(d), size, color)
    bar = Line(LEFT, RIGHT, color=color, stroke_width=5).set_width(max(top.width, bot.width) + .3)
    return VGroup(top, bar, bot).arrange(DOWN, buff=.14)


def pct(x, places=0):
    return f'{x * 100:.{places}f}%'


class Matrix(VGroup):
    """2×2 confusion matrix. Rows = actual, columns = predicted; positive class first."""

    def __init__(self, center, w, h, row_names, col_names, label_size=36, axis_size=34):
        super().__init__()
        c = np.array(center, dtype=float)
        self.w, self.h, self.c = w, h, c
        self.cells = {}
        for r, rk in enumerate('PN'):
            for k, ck in enumerate('PN'):
                pos = c + np.array([(k - .5) * w, (.5 - r) * h, 0])
                self.cells[rk + ck] = Rectangle(width=w, height=h, stroke_color=LINE, stroke_width=3,
                                                fill_color=BG, fill_opacity=1).move_to(pos)
        self.grid = VGroup(*self.cells.values())
        left, top = c[0] - w, c[1] + h
        self.rows = VGroup(*[text(n, label_size).match_y(self.cells[k]).align_to([left - .3, 0, 0], RIGHT)
                             for n, k in zip(row_names, ['PP', 'NP'])])
        self.cols = VGroup(*[text(n, label_size).move_to([self.cells[k].get_x(), top + .42, 0])
                             for n, k in zip(col_names, ['PP', 'PN'])])
        self.pred_axis = text('Predicted', axis_size, SOFT).move_to([c[0], top + 1.0, 0])
        self.act_axis = text('Actual', axis_size, SOFT).next_to(self.rows, UP, buff=.25).align_to(self.rows, RIGHT)
        self.add(self.grid, self.rows, self.cols, self.pred_axis, self.act_axis)

    def at(self, key):
        return self.cells[key].get_center()

    def row(self, r):
        return VGroup(self.cells[r + 'P'], self.cells[r + 'N'])

    def col(self, k):
        return VGroup(self.cells['P' + k], self.cells['N' + k])


def band(group, color=ACC, pad=-.03):
    """Terracotta tint behind the cells (z between cell fill and ink text).
    A solid accent outline reads as accent *text* to GATE T §8.3; a tint keeps ink-on-tint contrast."""
    return SurroundingRectangle(group, stroke_width=0, fill_color=color, fill_opacity=.28,
                                buff=pad, corner_radius=.04).set_z_index(1)


class Base(Scene):
    def setup(self):
        self.camera.background_color = BG
        self.bid = self.__class__.__name__[:3]
        self.beat = next(b for b in BS['beats'] if b['beat_id'] == self.bid)
        self.target_duration = self.beat['actual_duration_s']
        # Title-safe for GATE V is a 5% inset: |x| <= 6.4, |y| <= 3.6 Manim units.
        handle = text('@sanjiv', 30, SOFT)
        self.add(handle.move_to([0, -3.3, 0]).align_to([6.2, 0, 0], RIGHT))

    def header(self, title, y=3.1):
        self.add(text(title, 56).move_to([0, y, 0]))

    def until(self, fraction):
        goal = self.target_duration * fraction
        if goal > self.renderer.time:
            self.wait(goal - self.renderer.time)

    def cue(self, phrase, fallback):
        words_path = R / 'mp3/words.json'
        if words_path.exists():
            words = json.loads(words_path.read_text()).get('beats', {}).get(self.bid, [])
            target = re.sub(r'[^a-z0-9 ]', '', phrase.lower()).split()
            for k in range(len(words) - len(target) + 1):
                got = [re.sub(r'[^a-z0-9]', '', w['text'].lower()) for w in words[k:k + len(target)]]
                if got == target:
                    sec = words[k]['startFrame'] / 24
                    if sec > self.renderer.time:
                        self.wait(sec - self.renderer.time)
                    return
        self.until(fallback)

    def end(self):
        self.until(1)

    def count(self, value, pos, size=84, color=INK, run_time=.8):
        t = ValueTracker(0)
        m = always_redraw(lambda: num(f'{int(round(t.get_value())):,}', size, color).move_to(pos))
        self.add(m)
        self.play(t.animate.set_value(value), run_time=run_time, rate_func=smooth)
        m.clear_updaters()
        return m


class B02_Scene(Base):
    def construct(self):
        self.header('Truth × Prediction')
        mx = Matrix([.75, -.85, 0], 4.1, 2.1, ['Positive', 'Negative'], ['Positive', 'Negative'], 44, 40)
        self.play(FadeIn(mx.act_axis), FadeIn(mx.rows), Create(mx.grid), run_time=.9)
        self.cue('columns hold', .2)
        self.play(FadeIn(mx.pred_axis), FadeIn(mx.cols), run_time=.8)

        def cell(key, name, tag, color=INK):
            return VGroup(text(name, 46, color, MEDIUM), text(tag, 34, SOFT)).arrange(DOWN, buff=.18).move_to(mx.at(key))

        self.cue('Agreement lands', .38)
        tp, tn = cell('PP', 'True Positive', 'correct catch'), cell('NN', 'True Negative', 'correct clear')
        diag = VGroup(mx.cells['PP'], mx.cells['NN'])
        self.play(diag.animate.set_fill(TINT, 1), FadeIn(tp, shift=UP * .15), FadeIn(tn, shift=UP * .15), run_time=1.0)
        self.cue('Off the diagonal', .62)
        fp = text('False Positive', 46, INK, MEDIUM).move_to(mx.at('NP'))
        fn = text('False Negative', 46, INK, MEDIUM).move_to(mx.at('PN'))
        self.play(FadeIn(fp), FadeIn(fn), run_time=1.0)
        # Highlighter marks behind the two mistake tags: the beat's one accent moment.
        self.cue('false alarm', .78)
        alarm = text('a false alarm', 38, INK).next_to(fp, DOWN, buff=.2).shift(UP * .25)
        self.play(fp.animate.shift(UP * .25), FadeIn(alarm), FadeIn(band(alarm, pad=.12)), run_time=.6)
        self.cue('is a miss', .92)
        miss = text('a miss', 38, INK).next_to(fn, DOWN, buff=.2).shift(UP * .25)
        self.play(fn.animate.shift(UP * .25), FadeIn(miss), FadeIn(band(miss, pad=.12)), run_time=.6)
        self.end()


class B03_Scene(Base):
    def construct(self):
        self.header(f"{D['n']:,} Card Payments · {D['fraud']} Fraud")
        self.add(text('Constructed example', 30, SOFT).move_to([0, 2.52, 0]))
        mx = Matrix([.85, -.9, 0], 4.0, 1.8, ['Fraud', 'Honest'], ['Fraud', 'Honest'], 44, 36)
        self.play(FadeIn(mx), run_time=.9)

        def tag(key, s):
            return text(s, 34, SOFT).move_to(mx.at(key) + DOWN * .5)

        self.cue('Fifteen are real', .22)
        self.count(M['tp'], mx.at('PP') + UP * .3)
        self.play(FadeIn(tag('PP', 'caught')), run_time=.4)
        self.cue('Ten are honest', .38)
        self.count(M['fp'], mx.at('NP') + UP * .3)
        self.play(FadeIn(tag('NP', 'false alarms')), run_time=.4)
        self.cue('Five frauds', .52)
        self.count(M['fn'], mx.at('PN') + UP * .3)
        self.play(FadeIn(tag('PN', 'missed')), FadeIn(band(mx.cells['PN'])), run_time=.5)
        self.cue('The other', .66)
        self.count(M['tn'], mx.at('NN') + UP * .3, run_time=1.1)
        self.play(FadeIn(tag('NN', 'cleared')), run_time=.4)
        self.cue('Every payment', .8)
        total = M['tp'] + M['fn'] + M['fp'] + M['tn']
        assert total == D['n']
        check = text(f"{M['tp']}  +  {M['fn']}  +  {M['fp']}  +  {M['tn']}  =  {total:,}", 46, INK, MEDIUM).move_to([.3, -3.15, 0])
        self.play(FadeIn(check, shift=UP * .15), run_time=.8)
        self.end()


class B04_Scene(Base):
    def construct(self):
        self.header('Rows: Reality · Columns: Claims')
        mx = Matrix([-2.95, -.55, 0], 1.9, 1.6, ['Fraud', 'Honest'], ['Fraud', 'Honest'], 32, 30)
        vals = VGroup(*[num(f'{M[k]:,}', 62).move_to(mx.at(c)) for k, c in
                        [('tp', 'PP'), ('fn', 'PN'), ('fp', 'NP'), ('tn', 'NN')]])
        self.add(mx, vals)
        LABEL_X, FRAC_X, EQ_X = -.7, 3.95, 4.75  # fixed table columns: label | fraction | result

        def rate(name, gloss, n, d, result, y):
            label = VGroup(text(name, 38, INK, MEDIUM), text(gloss, 30, SOFT)).arrange(DOWN, buff=.1, aligned_edge=LEFT)
            label.move_to([0, y, 0]).align_to([LABEL_X, 0, 0], LEFT)
            f = frac(n, d, 50).move_to([FRAC_X, y, 0])
            eq = text(result, 46, INK, MEDIUM).move_to([0, y, 0]).align_to([EQ_X, 0, 0], LEFT)
            return VGroup(label, f, eq)

        rows = [
            ('Recall', 'fraud caught', M['tp'], M['tp'] + M['fn'], f"=  {pct(M['recall'])}", 1.6, mx.row('P'), 'Fraud row'),
            ('Precision', 'flags correct', M['tp'], M['tp'] + M['fp'], f"=  {pct(M['precision'])}", -.3, mx.col('P'), 'Fraud column'),
            ('False-positive rate', 'honest flagged', M['fp'], M['fp'] + M['tn'], f"≈  {pct(M['fpr'])}", -2.2, mx.row('N'), 'Honest row'),
        ]
        hl = None
        for (name, gloss, n, d, res, y, target, _), (phrase, fb) in zip(rows, [('Read across', .05), ('Read down', .4), ('Across the honest', .74)]):
            self.cue(phrase, fb)
            new = band(target)
            self.play(FadeIn(new) if hl is None else Transform(hl, new), run_time=.7)
            hl = hl or new
            r = rate(name, gloss, n, d, res, y)
            self.play(FadeIn(r[0]), run_time=.5)
            self.play(FadeIn(r[1], shift=LEFT * .2), run_time=.6)
            self.play(FadeIn(r[2]), run_time=.5)
        self.end()


class B05_Scene(Base):
    def construct(self):
        self.header('The Accuracy Trap')
        specs = [('Our model', M, -2.6), ('Never flags', L, 3.85)]
        mats = []
        for title, d, x in specs:
            mx = Matrix([x, .25, 0], 2.25, 1.1, ['Fraud', 'Honest'], ['Fraud', 'Honest'], 32, 28)
            mx.remove(mx.pred_axis); mx.remove(mx.act_axis)
            name = text(title, 44, INK, MEDIUM).move_to([x - .45, 2.45, 0])
            vals = {c: num(f'{d[k]:,}', 52).move_to(mx.at(c)) for k, c in [('tp', 'PP'), ('fn', 'PN'), ('fp', 'NP'), ('tn', 'NN')]}
            mats.append((mx, name, vals, d, x))
        self.play(*[FadeIn(VGroup(mx, name, *vals.values())) for mx, name, vals, _, _ in mats], run_time=1.0)

        self.cue('scores ninetyeight percent', .18)
        accs = [text(f"Accuracy  {pct(d['accuracy'], 1)}", 46).move_to([x - .45, -1.45, 0]) for _, _, _, d, x in mats]
        self.play(*[FadeIn(a, shift=UP * .15) for a in accs], run_time=.8)

        self.cue('zero true positives', .42)
        lazy_mx, _, lazy_vals, _, _ = mats[1]
        self.play(Indicate(lazy_vals['PP'], color=INK, scale_factor=1.25), run_time=.7)
        self.cue('all twenty', .52)
        self.play(FadeIn(band(lazy_mx.cells['PN'])), run_time=.6)
        self.cue('recall zero', .6)
        # Accent stays a stroke (text accent fails §8.3 contrast on cream).
        recs = [text(f"Recall  {pct(d['recall'])}", 46, INK, MEDIUM).move_to([x - .45, -2.1, 0])
                for _, _, _, d, x in mats]
        underline = Line(LEFT, RIGHT, color=ACC, stroke_width=8).set_width(recs[1].width + .2).next_to(recs[1], DOWN, buff=.1)
        self.play(*[FadeIn(r, shift=UP * .15) for r in recs], run_time=.8)
        self.play(Create(underline), run_time=.4)

        self.cue('One caution', .8)
        warn = text('Check the labels first: some tools put predictions in the rows.', 34, SOFT).move_to([-.6, -2.95, 0])
        self.play(FadeIn(warn), *[Indicate(mx.rows, color=INK, scale_factor=1.12) for mx, _, _, _, _ in mats], run_time=1.0)
        self.end()
