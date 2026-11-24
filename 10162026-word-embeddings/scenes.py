"""Native teaching figures. Counts and cosine numbers derive from evidence/result.json."""
import json,hashlib
from pathlib import Path
from manim import *
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SHEET=json.loads((HERE/'beat_sheet.json').read_text())
WORDS=json.loads((HERE/'mp3/words.json').read_text()) if (HERE/'mp3/words.json').exists() else {'beats':{}}
DATA=json.loads((HERE/'evidence/result.json').read_text())
BG='#FAF9F5';INK='#3D3929';ACC='#D97757';PALE='#DAD5C9';MUTED='#625E52';WHITE='#FFFDF9'
def text(s,size=38,color=INK):
    with register_font(ROOT/'runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf'):
        return Text(s,font='EB Garamond',font_size=size,color=color)
def box(s,w=2.6,h=.95,size=38):
    t=text(s,size)
    if t.width>w-.3:t.scale_to_fit_width(w-.3)
    return VGroup(RoundedRectangle(width=w,height=h,corner_radius=.1,stroke_color=PALE,stroke_width=2,fill_color=WHITE,fill_opacity=1),t)
def arrow(a,b,color=PALE):return Arrow(a,b,buff=.16,color=color,stroke_width=3,max_tip_length_to_length_ratio=.1)
def mathsvg(expr,width=6):
    path=HERE/'math'/f'{hashlib.sha256(expr.encode()).hexdigest()[:14]}.svg'
    if not path.exists():raise FileNotFoundError(f'Missing typeset equation asset: {path}')
    return SVGMobject(str(path)).set_width(width)
class Base(Scene):
    def setup(self):
        self.camera.background_color=BG;self.bid=self.__class__.__name__[:3]
        self.beat=next(b for b in SHEET['beats'] if b['beat_id']==self.bid);self.end=self.beat['actual_duration_s']
    def title(self,s):
        t=text(s,52).move_to([0,3.1,0])
        if t.width>12.2:t.scale_to_fit_width(12.2)
        self.add(t)
    def reveal(self,*m):self.play(LaggedStart(*[FadeIn(x,shift=UP*.06) for x in m],lag_ratio=.12),run_time=.45)
    def change(self,old,*new):
        self.play(*[FadeOut(x) for x in old],run_time=.2)
        self.reveal(*new)
    def cue(self,phrase):
        import re
        norm=lambda x:re.sub('[^a-z0-9]','',x.lower())
        target=[norm(x) for x in phrase.split()];words=WORDS['beats'][self.bid]
        for i in range(len(words)-len(target)+1):
            if [norm(x['text']) for x in words[i:i+len(target)]]==target:
                self.until(words[i]['startFrame']/24);return
        raise ValueError(f'Missing cue {self.bid}: {phrase}')
    def until(self,t):
        if t>self.renderer.time+.025:self.wait(t-self.renderer.time)
    def finish(self):self.until(self.end)
    def note(self,s,y=-2.9):
        t=text(s,28,MUTED).move_to([0,y,0]);self.reveal(t);return t

class B02_Scene(Base):
    def construct(self):
        self.title('From Address to Vector')
        cat=box('cat',2).move_to([-4.6,.5,0]);idx=box('ID 7',2).move_to([-1.4,.5,0]);link=arrow(cat.get_right(),idx.get_left())
        self.reveal(cat,idx,link);self.note('Illustrative ID and coordinates')
        self.cue('A learned embedding table')
        vals=[['0.1','0.5','−0.2'],['0.2','−0.4','0.8'],['−0.3','0.1','0.6']]
        rows=VGroup(*[VGroup(*[box(v,1.05,.66,30) for v in row]).arrange(RIGHT,buff=.08) for row in vals]).arrange(DOWN,buff=.2).move_to([3.5,.5,0])
        h=text('Embedding table',34).move_to([3.5,2,0]);self.reveal(rows,h)
        self.play(rows[1][0][0].animate.set_stroke('#A34B31',width=4),rows[1][1][0].animate.set_stroke('#A34B31',width=4),rows[1][2][0].animate.set_stroke('#A34B31',width=4),run_time=.4)
        self.reveal(arrow(idx.get_right(),rows[1].get_left()))
        self.cue('Those coordinates work together');self.reveal(text('One row · a learned representation',36).move_to([0,-1.5,0]));self.finish()

class B03_Scene(Base):
    def construct(self):
        self.title('Context Supplies the Signal')
        sentences=['cat eats food','dog eats food','cat likes play','dog likes play']
        lines=VGroup(*[text(s,38) for s in sentences]).arrange(DOWN,buff=.35).move_to([-3.5,.3,0]);self.reveal(lines)
        self.note('Toy corpus · one-word context window')
        self.cue('With a window')
        header=VGroup(text('eats',32),text('likes',32)).arrange(RIGHT,buff=.75).move_to([3,.95,0])
        cells=VGroup(*[VGroup(box('1',1.1,.75,36),box('1',1.1,.75,36)).arrange(RIGHT,buff=.25) for _ in range(2)]).arrange(DOWN,buff=.25).move_to([3,-.2,0])
        labels=VGroup(text('cat',34).next_to(cells[0],LEFT,buff=.4),text('dog',34).next_to(cells[1],LEFT,buff=.4))
        self.reveal(header,cells,labels)
        self.cue('That is a training signal');self.reveal(text('Shared context ≠ identical meaning',38).move_to([0,-1.9,0]));self.finish()

class B04_Scene(Base):
    def construct(self):
        self.title('Word2Vec: Two Prediction Tasks')
        sub=text('CBOW · context predicts the target',38).move_to([0,2,0]);self.reveal(sub)
        inputs=VGroup(box('the',2.2).move_to([-3.7,.7,0]),box('eats',2.2).move_to([-3.7,-.7,0]));target=box('cat',2.2).move_to([3.5,0,0]);edges=VGroup(*[arrow(m.get_right(),target.get_left()) for m in inputs]);self.reveal(inputs,target,edges)
        self.note('Example window: the [cat] eats')
        self.cue('Skip-gram reverses')
        sub2=text('Skip-gram · target predicts context',38).move_to([0,2,0]);left=box('cat',2.2).move_to([-3.7,0,0]);right=VGroup(box('the',2.2).move_to([3.5,.7,0]),box('eats',2.2).move_to([3.5,-.7,0]));links=VGroup(*[arrow(left.get_right(),m.get_left()) for m in right])
        self.change([sub,inputs,target,edges],sub2,left,right,links)
        self.cue('Slide a window');self.reveal(text('Window → examples → vector updates',36).move_to([0,-1.9,0]));self.finish()

class B05_Scene(Base):
    def construct(self):
        self.title('Learn From Observed Pairs')
        a=box('cat',2).move_to([-3.4,.9,0]);b=box('eats',2).move_to([3.4,.9,0]);e=arrow(a.get_right(),b.get_left(),'#A34B31')
        lbl=text('Observed pair',34).move_to([0,1.85,0]);self.reveal(a,b,e,lbl)
        self.note('Schematic negative-sampling step')
        self.cue('Negative sampling')
        c=box('cat',2).move_to([-3.4,-.9,0]);d=box('road',2).move_to([3.4,-.9,0]);e2=arrow(c.get_right(),d.get_left());l2=text('Sampled contrast',34).move_to([0,-1.85,0]);self.reveal(c,d,e2,l2)
        self.cue('Training adjusts');self.play(Indicate(a,color=INK,scale_factor=1.06),Indicate(b,color=INK,scale_factor=1.06),run_time=.7)
        self.cue('A sampled negative');self.change([l2],text('Not “impossible together”',34).move_to([0,-1.85,0]));self.finish()

class B06_Scene(Base):
    def construct(self):
        self.title('GloVe: Count, Then Fit')
        contexts=['eats','likes','uses','needs'];words=['cat','dog','car','truck']
        cells=VGroup();labels=VGroup()
        for j,c in enumerate(contexts):labels.add(text(c,34).move_to([-2.2+j*1.7,1.8,0]))
        for i,w in enumerate(words):
            y=1.05-i*.65;labels.add(text(w,34).move_to([-4.1,y,0]))
            for j,c in enumerate(contexts):
                val=DATA['rows'][w].get(c,0);m=box(str(val),1.5,.57,34).move_to([-2.2+j*1.7,y,0]);cells.add(m)
        labels.shift(UP*.25);cells.shift(UP*.25)
        self.reveal(labels,cells);self.note('Toy corpus · selected rows and columns',-3.15)
        self.cue('It learns word and context vectors')
        eq=mathsvg(r'w_i^{\mathsf{T}}\widetilde{w}_j+b_i+\widetilde{b}_j\approx\log X_{ij}',7.7).move_to([0,-1.65,0]);self.reveal(eq)
        self.cue('A weighting function');self.reveal(text('Weighted fit · nonzero counts',32).move_to([0,-2.5,0]));self.finish()

class B07_Scene(Base):
    def construct(self):
        self.title('Different Routes, Related Evidence')
        left=VGroup(box('Prediction examples',5,1,36),box('Word2Vec',5,1,40),box('Learned vectors',5,1,36)).arrange(DOWN,buff=.55).move_to([-3.3,0,0])
        right=VGroup(box('Co-occurrence counts',5,1,36),box('GloVe',5,1,40),box('Learned vectors',5,1,36)).arrange(DOWN,buff=.55).move_to([3.3,0,0])
        self.reveal(left);self.cue('GloVe fits');self.reveal(right)
        self.reveal(*[arrow(g[i].get_bottom(),g[i+1].get_top()) for g in [left,right] for i in [0,1]])
        self.cue('Both depend');self.note('Same questions: corpus · context · evaluation',-2.85);self.finish()

class B08_Scene(Base):
    def construct(self):
        self.title('Cosine Compares Directions')
        eq=mathsvg(r'\cos(\theta)=\frac{u\cdot v}{\|u\|\,\|v\|}',6.3).move_to([0,.45,0]);self.reveal(eq)
        self.note('Constructed 2D vectors · not trained embeddings')
        self.cue('Here are constructed');self.play(FadeOut(eq),run_time=.2)
        axes=Axes(x_range=[0,3,1],y_range=[0,5,1],x_length=3.5,y_length=3.6,tips=False,axis_config={'color':PALE,'stroke_width':2}).move_to([-3,.15,0])
        origin=axes.c2p(0,0);a=Arrow(origin,axes.c2p(1,2),buff=0,color=INK,stroke_width=7);b=Arrow(origin,axes.c2p(2,4),buff=0,color=ACC,stroke_width=3)
        al=text('A = (1, 2)',32).next_to(axes.c2p(1,2),LEFT,buff=.25);bl=text('B = (2, 4)',32).next_to(axes.c2p(2,4),RIGHT,buff=.2)
        self.reveal(axes,a,al);self.cue('B is two');self.reveal(b,bl)
        self.cue('They point');score=mathsvg(r'\cos(A,B)=1',4).move_to([3.4,.5,0]);self.reveal(score,text('Same direction',34).move_to([3.4,-.6,0]));self.finish()

class B09_Scene(Base):
    def construct(self):
        self.title('Compute, Do Not Guess')
        pair=text('A = (1, 2)     C = (2, 1)',40).move_to([0,1.9,0]);self.reveal(pair)
        dot=mathsvg(r'A\cdot C=1\times2+2\times1=4',7.3).move_to([0,.65,0]);self.cue('Their dot product');self.reveal(dot)
        norms=mathsvg(r'\|A\|=\|C\|=\sqrt{5}',5.2).move_to([0,-.55,0]);self.cue('each length');self.reveal(norms)
        score=mathsvg(r'\cos(A,C)=\frac{4}{\sqrt{5}\sqrt{5}}=\frac{4}{5}=0.8',8.5).move_to([0,-2,0]);self.cue('Cosine is');self.reveal(score)
        self.cue('A perpendicular vector');self.change([pair,dot,norms,score],text('A = (1, 2)     D = (−2, 1)',40).move_to([0,1.5,0]),mathsvg(r'A\cdot D=0\quad\Rightarrow\quad\cos(A,D)=0',8.5).move_to([0,0,0]))
        self.cue('cosine is undefined');self.reveal(text('Zero vector → undefined cosine',38).move_to([0,-1.8,0]));self.finish()

class B10_Scene(Base):
    def construct(self):
        self.title('Close Does Not Mean Synonymous')
        words=VGroup(box('hot',2.4),box('cold',2.4)).arrange(RIGHT,buff=1).move_to([0,.8,0]);ctx=text('Both can describe weather',38).move_to([0,-.5,0]);disc=text('Qualitative example · no measured score',28,MUTED).move_to([0,-2.8,0]);self.reveal(words,ctx,disc)
        self.cue('Classic Word2Vec');a=box('river bank',3.5).move_to([-3.8,1,0]);b=box('bank loan',3.5).move_to([-3.8,-.7,0]);v=box('bank vector',3.8).move_to([3.3,.15,0]);links=VGroup(arrow(a.get_right(),v.get_left()),arrow(b.get_right(),v.get_left()))
        self.change([words,ctx,disc],a,b,v,links)
        self.cue('A later contextual model');self.reveal(text('Contextual models can distinguish occurrences',36).move_to([0,-2.3,0]));self.finish()
