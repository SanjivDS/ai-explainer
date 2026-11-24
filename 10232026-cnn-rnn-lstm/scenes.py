"""Native teaching figures. Backpropagation calculations derive from evidence/result.json."""
import json,hashlib
from pathlib import Path
from manim import *
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SHEET=json.loads((HERE/'beat_sheet.json').read_text())
WORDS=json.loads((HERE/'mp3/words.json').read_text()) if (HERE/'mp3/words.json').exists() else {'beats':{}}
DATA=json.loads((HERE/'evidence/result.json').read_text())
BG='#FAF9F5';INK='#3D3929';ACC='#A34B31';PALE='#DAD5C9';MUTED='#625E52';WHITE='#FFFDF9'
def text(s,size=38,color=INK):
    with register_font(ROOT/'runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf'):
        return Text(s,font='EB Garamond',font_size=size,color=color)
def box(s,w=2.6,h=.95,size=38):
    t=text(s,size)
    if t.width>w-.3:t.scale_to_fit_width(w-.3)
    return VGroup(RoundedRectangle(width=w,height=h,corner_radius=.1,stroke_color=PALE,stroke_width=2,fill_color=WHITE,fill_opacity=1),t)
def arrow(a,b,color=PALE,tip_ratio=.1):return Arrow(a,b,buff=.16,color=color,stroke_width=3,max_tip_length_to_length_ratio=tip_ratio)
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
        t=text(s,32,MUTED).move_to([0,y,0]);self.reveal(t);return t


def formula(expr,y=0,width=8):
    return mathsvg(expr,width).move_to([0,y,0])

def matrix(rows,position,width=3):
    entries=VGroup(*[text(str(v).replace('-', '−'),40) for row in rows for v in row]).arrange_in_grid(rows=len(rows),cols=len(rows[0]),buff=(.65,.48))
    h=entries.height+.4;w=entries.width+.5
    left=VGroup(Line([-w/2,-h/2,0],[-w/2,h/2,0]),Line([-w/2,h/2,0],[-w/2+.15,h/2,0]),Line([-w/2,-h/2,0],[-w/2+.15,-h/2,0])).set_color(INK)
    right=left.copy().flip(UP,about_point=ORIGIN)
    return VGroup(entries,left,right).scale(1.05).move_to(position)

def grid(n=5,side=.52):
 return VGroup(*[Square(side_length=side,stroke_color=PALE,stroke_width=2,fill_color=WHITE,fill_opacity=1) for _ in range(n*n)]).arrange_in_grid(rows=n,buff=.02)
def signal():
 return VMobject(color=INK,stroke_width=4).set_points_as_corners([[i*.35-2, .6*v,0] for i,v in enumerate([0,.2,.1,1,-.7,.1,0,.2,.1,1,-.7,0])])
class B02_Scene(Base):
 def construct(self):
  self.title('Three Ways to Handle Information')
  g=grid().move_to([-4.3,.35,0]);self.reveal(g);self.play(g[12].animate.set_fill(ACC,1),run_time=.5);self.reveal(text('Image defect',36).move_to([-4.3,-1.65,0]))
  self.cue('following a sensor stream');s=signal().scale(.8).move_to([0,.35,0]);self.play(Create(s),run_time=.7);self.reveal(text('Ordered stream',36).move_to([0,-1.65,0]))
  self.cue('remembering an earlier event');a=arrow([2.7,.35,0],[5.8,.35,0]);self.reveal(a,Dot([2.7,.35,0],color=ACC),text('Delayed context',36).move_to([4.3,-1.65,0]));self.note('Input structure suggests candidates · testing decides');self.finish()
class B03_Scene(Base):
 def construct(self):
  self.title('CNN: Reuse a Local Detector');g=grid().move_to([-3.7,.2,0]);f=grid(3,.65).move_to([3.5,.2,0]);self.reveal(g,f,text('Input',36).move_to([-3.7,2,0]),text('Feature map',36).move_to([3.5,2,0]))
  win=SurroundingRectangle(VGroup(g[0],g[12]),buff=.03,color=ACC);self.play(Create(win),run_time=.5)
  self.cue('at different locations')
  for k in range(3):
   self.play(win.animate.move_to(VGroup(g[k],g[k+12]).get_center()),f[k].animate.set_fill(ACC,.65),run_time=.6)
  self.cue('Sharing weights');self.note('One learned filter · reused at every location',-2.5)
  self.cue('Deeper layers');self.reveal(arrow([-1.7,.2,0],[1.7,.2,0]),text('Local → larger patterns',36).move_to([0,-3.15,0]));self.finish()
class B04_Scene(Base):
 def construct(self):
  self.title('A Tiny Convolution');cells=VGroup(*[box(str(i),1.35,.9) for i in range(1,6)]).arrange(RIGHT,buff=.12).move_to([0,1.4,0]);self.reveal(cells)
  self.cue('weights one');self.reveal(formula(r'w=(1,0,-1)',.05,5));win=SurroundingRectangle(VGroup(*cells[:3]),buff=.1,color=ACC);self.reveal(win)
  self.cue('Each three-value window');outs=VGroup(*[box('−2',1.5,.9) for _ in range(3)]).arrange(RIGHT,buff=.3).move_to([0,-1.6,0])
  for i in range(3):
   self.play(win.animate.move_to(VGroup(*cells[i:i+3]).get_center()),FadeIn(outs[i]),run_time=.65)
  self.note('Constructed cross-correlation · stride 1 · no padding');self.finish()
class B05_Scene(Base):
 def construct(self):
  self.title('When a CNN Fits');g=grid(4).move_to([-3.7,.8,0]);s=signal().move_to([3.3,.8,0]);self.reveal(g);self.cue('short motifs');self.play(Create(s),run_time=.7)
  self.cue('Stacking layers');cells=VGroup(*[Square(.55,color=PALE) for _ in range(15)]).arrange(RIGHT,buff=.03).move_to([0,-1.25,0]);self.reveal(cells);win=SurroundingRectangle(VGroup(*cells[6:9]),color=ACC,buff=.08);self.reveal(win)
  self.cue('expands the region');self.play(Transform(win,SurroundingRectangle(VGroup(*cells[3:12]),color=ACC,buff=.08)),run_time=1);self.note('Receptive field = input region an output can use');self.finish()
class B06_Scene(Base):
 def construct(self):
  self.title('RNN: Carry a State Forward');nodes=VGroup(*[box('Same update',3,1,36).move_to([x,.5,0]) for x in [-4.5,0,4.5]])
  for i,n in enumerate(nodes):
   if i:self.reveal(arrow(nodes[i-1].get_right(),n.get_left(),ACC))
   self.reveal(n,text(f'Input {i+1}',36).move_to([n.get_x(),-1.5,0]),arrow([n.get_x(),-1,0],n.get_bottom()))
  self.cue('learned summary');self.reveal(text('Hidden state carries earlier information',38).move_to([0,1.9,0]));self.cue('same update rule');self.note('Shared weights across time · order matters');self.finish()
class B07_Scene(Base):
 def construct(self):
  self.title('A Tiny Recurrent Update');self.reveal(formula(r'h_t=\tanh(x_t+0.5h_{t-1})',1.6,9));self.reveal(formula(r'h_0=0',.25,2.7))
  self.cue('inputs one');nodes=VGroup(*[box(s,3.4,1.1,38).move_to([x,-1.5,0]) for s,x in zip(['1 → 0.762','0 → 0.363','0 → 0.180'],[-4.4,0,4.4])])
  for i,n in enumerate(nodes):
   self.reveal(n)
   if i:self.reveal(arrow(nodes[i-1].get_right(),n.get_left(),ACC))
  self.note('Constructed scalar example · input → rounded state');self.finish()
class B08_Scene(Base):
 def construct(self):
  self.title('Where a Basic RNN Struggles');nodes=VGroup(*[Square(.65,color=PALE) for _ in range(10)]).arrange(RIGHT,buff=.55).move_to([0,1.15,0]);self.reveal(nodes)
  for i in range(9,0,-1):self.play(Create(arrow(nodes[i].get_left(),nodes[i-1].get_right(),ACC,.4)),run_time=.16)
  self.cue('multiplying by one half');self.reveal(formula(r'(0.5)^{10}\approx0.00098',-.5,8))
  self.cue('small baseline');self.note('Short dependencies: a useful baseline',-2.1);self.note('Illustrative product · not a measured network gradient',-3.05);self.finish()
class B09_Scene(Base):
 def construct(self):
  self.title('LSTM: Control the Memory');self.reveal(text('Cell state',36).move_to([-4.7,1.9,0]));line=Line([-5.8,.8,0],[5.8,.8,0],color=PALE,stroke_width=5);self.play(Create(line),run_time=.6)
  self.cue('forget gate');f=box('Forget',2.5,.9).move_to([-3,.8,0]);self.reveal(f,text('retain',34).move_to([-3,-.35,0]))
  self.cue('input gate');g=box('Input',2.5,.9).move_to([.6,-1,0]);self.reveal(g,arrow(g.get_top(),[.6,.8,0],ACC),text('new content',34).move_to([.6,-2,0]))
  self.cue('output gate');out=box('Output',2.5,.9).move_to([4,-1,0]);self.reveal(out,arrow([4,.8,0],out.get_top()),text('Hidden state',34).move_to([4,-2,0]));self.note('Learned gates regulate information flow',-3.1);self.finish()
class B10_Scene(Base):
 def construct(self):
  self.title('One Gated Memory Update');self.reveal(formula(r'c_{\mathrm{new}}=f c_{\mathrm{old}}+i g',1.5,8));self.reveal(text('retain old memory + admit new content',34).move_to([0,.35,0]))
  self.cue('Retain eighty percent');self.reveal(formula(r'0.8\times0.5+0.2\times0.3',-.9,9))
  self.cue('zero point four six');self.reveal(formula(r'c_{\mathrm{new}}=0.46',-2.1,4.8));self.note('Supplied illustrative gates · not trained values',-3.15);self.finish()
class B11_Scene(Base):
 def construct(self):
  self.title('When an LSTM Fits');line=arrow([-5.5,.5,0],[5.5,.5,0]);self.reveal(line,text('Earlier cue',38).move_to([-4.5,1.5,0]),text('Later decision',38).move_to([4.3,1.5,0]));dot=Dot([-4.5,.5,0],color=ACC,radius=.13);self.reveal(dot)
  self.cue('persist across many steps');self.play(dot.animate.move_to([4.3,.5,0]),run_time=2);self.reveal(box('Gated state carries context',8,1,38).move_to([0,-1.2,0]))
  self.cue('add parameters');self.note('Extra capacity and compute · same hidden width',-2.65);self.finish()
class B12_Scene(Base):
 def construct(self):
  self.title('Compare the Constraints');self.reveal(text('CNN · parallel windows',38).move_to([0,2,0]));windows=VGroup(*[box('Window',2.5,.8,34) for _ in range(4)]).arrange(RIGHT,buff=.35).move_to([0,.9,0]);self.reveal(windows)
  self.cue('Recurrent steps');nodes=VGroup(*[box('State',2.5,.8,34) for _ in range(4)]).arrange(RIGHT,buff=.35).move_to([0,-1,0]);self.reveal(text('RNN / LSTM · time dependency',38).move_to([0,-.1,0]))
  for i,n in enumerate(nodes):
   self.reveal(n)
   if i:self.reveal(Arrow(nodes[i-1].get_right(),n.get_left(),buff=.025,color=ACC,stroke_width=3,max_tip_length_to_length_ratio=.4))
  self.cue('live prediction');self.note('Live prediction: use only information available now',-2.4);self.cue('Measure latency');self.note('Measure on deployment hardware',-3.15);self.finish()
class B13_Scene(Base):
 def construct(self):
  self.title('Choose Through an Experiment');rows=[]
  for cue,label,y in [('For image defects','Image defect → test CNN',1.6),('For a short stream','Short stream → basic RNN baseline',.15),('For delayed context','Delayed context → LSTM + temporal CNN',-1.3)]:
   self.cue(cue);r=box(label,11.5,1,38).move_to([0,y,0]);self.reveal(r);rows.append(r)
  self.cue('Compare against');self.play(*[FadeOut(r) for r in rows],run_time=.4)
  train=box('Train candidates',4,1.2,38).move_to([-3,1,0]);evaluate=box('Held-out evaluation',4.5,1.2,36).move_to([3,1,0]);self.reveal(train,evaluate,arrow(train.get_right(),evaluate.get_left(),ACC,.3))
  self.reveal(box('Compare task metric + deployment cost',11,1,36).move_to([0,-1.1,0]));self.note('Same metric · suitable split · deployment budget',-2.9);self.finish()
