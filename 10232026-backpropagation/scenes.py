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

class B02_Scene(Base):
 def construct(self):
  self.title('Bring Back the Network')
  x=box('Inputs',3).move_to([-4.5,1.2,0]);h=box('Hidden · ReLU',3).move_to([0,1.2,0]);y=box('Linear output',3).move_to([4.5,1.2,0])
  self.reveal(x,h,y,arrow(x.get_right(),h.get_left()),arrow(h.get_right(),y.get_left()))
  self.cue('The inputs are');self.reveal(mathsvg(r'x=(2,1)',3.4).move_to([-4.5,-.2,0]))
  self.cue('The hidden sums');z=mathsvg(r'z=(1,-0.5)',4).move_to([0,-.2,0]);self.reveal(z)
  self.cue('After ReLU');self.reveal(mathsvg(r'h=(1,0)',3.4).move_to([0,-1.5,0]))
  self.cue('the prediction is');self.reveal(mathsvg(r'\hat y=2.5',3.3).move_to([4.5,-.2,0]));self.note('Same constructed network · parameters held fixed');self.finish()

class B03_Scene(Base):
 def construct(self):
  self.title('Give the Prediction a Target')
  self.reveal(mathsvg(r'\hat y=2.5',4).move_to([-3.5,1.4,0]),mathsvg(r'y=1',2.5).move_to([3.5,1.4,0]))
  self.cue('half the squared error');loss=formula(r'L=\frac{1}{2}(\hat y-y)^2',-.2,7.5);self.reveal(loss)
  self.cue('Subtract one');result=formula(r'L=\frac{1}{2}(2.5-1)^2=1.125',-1.8,10);self.reveal(result)
  self.cue('numerical objective');self.note('One example · half-squared-error loss',-3.05);self.finish()

class B04_Scene(Base):
 def construct(self):
  self.title('Start at the Loss')
  axes=Axes(x_range=[0,3,1],y_range=[0,2,1],x_length=5.6,y_length=3.3,axis_config={'color':MUTED,'include_tip':False}).move_to([-3.3,-.2,0])
  curve=axes.plot(lambda v:.5*(v-1)**2,x_range=[0,3],color=INK);dot=Dot(axes.c2p(2.5,1.125),color=ACC)
  labels=VGroup(text('Prediction',32).next_to(axes,DOWN,buff=.2),text('Loss',32).next_to(axes,UP,buff=.15))
  self.reveal(axes,labels);self.play(Create(curve),run_time=.6);self.reveal(dot)
  self.cue('one point five');eq=mathsvg(r'\frac{\partial L}{\partial\hat y}=1.5',4.5).move_to([3.5,.5,0]);self.reveal(eq)
  tangent=Line(axes.c2p(2.05,.45),axes.c2p(2.85,1.65),color=ACC,stroke_width=4)
  self.cue('local sensitivity');self.play(Create(tangent),run_time=.5);self.note('Gradient = local rate of change',-2.9);self.finish()

class B05_Scene(Base):
 def construct(self):
  self.title('The Chain Rule')
  w=box('Parameter w',3).move_to([-4.5,1.25,0]);u=box('Value u',3).move_to([0,1.25,0]);l=box('Loss L',3).move_to([4.5,1.25,0])
  self.reveal(w,u,l,arrow(w.get_right(),u.get_left(),tip_ratio=.25),arrow(u.get_right(),l.get_left(),tip_ratio=.25))
  self.cue('Multiply the gradient');eq=formula(r'\frac{\partial L}{\partial w}=\frac{\partial L}{\partial u}\frac{\partial u}{\partial w}',-1,8.5);self.reveal(eq)
  self.cue('Repeat backward');back=VGroup(arrow([4.5,.55,0],[.6,.55,0],ACC),arrow([-.6,.55,0],[-4.5,.55,0],ACC));self.reveal(back)
  self.cue('several paths');self.note('Multiply along a path · add across paths',-3);self.finish()

class B06_Scene(Base):
 def construct(self):
  self.title('Gradients at the Output')
  self.reveal(formula(r'\hat y=v_1h_1+v_2h_2+c',1.95,8))
  self.cue('One point five times one');self.reveal(formula(r'\frac{\partial L}{\partial v_1}=1.5\times1=1.5',.25,8))
  self.cue('One point five times zero');self.reveal(formula(r'\frac{\partial L}{\partial v_2}=1.5\times0=0',-1.2,8))
  self.cue('output bias');self.reveal(formula(r'\frac{\partial L}{\partial c}=1.5',-2.7,3.4));self.finish()

class B07_Scene(Base):
 def construct(self):
  self.title('Pass Through ReLU')
  self.reveal(text('Use the original output weights',34).move_to([0,2,0]))
  self.cue('arriving gradients');arrive=formula(r'\frac{\partial L}{\partial h}=(3,-1.5)',.8,7);self.reveal(arrive)
  self.cue('slope one');left=box('Positive z · slope 1',5,.9,34).move_to([-3.3,-.55,0]);self.reveal(left)
  self.cue('zero on its negative');right=box('Negative z · slope 0',5,.9,34).move_to([3.3,-.55,0]);self.reveal(right)
  self.cue('gradients become');self.reveal(formula(r'\frac{\partial L}{\partial z}=(3,0)',-1.95,5.8));self.note('Here z = (1, −0.5) · neither value is zero',-3.15);self.finish()

class B08_Scene(Base):
 def construct(self):
  self.title('Reach the Earlier Weights')
  self.reveal(formula(r'x=(2,1)\qquad\frac{\partial L}{\partial z_1}=3',1.65,8))
  self.cue('six and three');self.reveal(formula(r'\frac{\partial L}{\partial w_{11}}=3\times2=6',-.1,7.8),formula(r'\frac{\partial L}{\partial w_{12}}=3\times1=3',-1.75,7.8))
  self.cue('bias gradient');note=self.note('First hidden bias: gradient 3',-3.05)
  self.cue('The second unit');self.change([note],text('Second unit: zero gradients for this input',32,MUTED).move_to([0,-3.05,0]));self.finish()

class B09_Scene(Base):
 def construct(self):
  self.title('The Optimizer Takes a Step')
  self.reveal(formula(r'\theta_{\mathrm{new}}=\theta-\eta\nabla L',1.5,8.5))
  self.cue('zero point zero five');self.reveal(formula(r'\eta=0.05',.1,4))
  self.cue('first hidden weight');self.reveal(formula(r'w_{11}:\quad0.5-0.05\times6=0.2',-1.5,11))
  self.cue('Compute all gradients');self.note('Compute all gradients first · then update together',-3);self.finish()

class B10_Scene(Base):
 def construct(self):
  self.title('Run Forward Again')
  self.reveal(formula(r'h=(0.1,0)',1.65,4.7))
  self.cue('updated output');self.reveal(formula(r'\hat y=1.925\times0.1+0.425=0.6175',.1,11.8))
  self.cue('loss falls');self.reveal(formula(r'L:\quad1.125\ \longrightarrow\ 0.0732',-1.6,9.5))
  self.cue('This particular step');self.note('One example · one step · rounded loss',-3);self.finish()

class B11_Scene(Base):
 def construct(self):
  self.title('Check the Gradient')
  self.reveal(formula(r'\frac{L(w+\varepsilon)-L(w-\varepsilon)}{2\varepsilon}',1.25,9))
  self.cue('agrees with');self.reveal(text('Analytic: 6     Numerical: ≈ 6',44).move_to([0,-.3,0]))
  self.cue('all nine parameters');self.reveal(formula(r'\varepsilon=10^{-6}',-1.65,4.5));self.note('All 9 parameter checks pass · example.py',-3)
  self.finish()

class B12_Scene(Base):
 def construct(self):
  self.title('From One Step to Learning')
  nodes=VGroup(*[box(s,2.5,.95,34) for s in ['Forward','Loss','Backward','Update']]).arrange(RIGHT,buff=.55).move_to([0,1.2,0])
  self.reveal(nodes);edges=VGroup(*[Arrow(nodes[i].get_right(),nodes[i+1].get_left(),buff=.04,color=MUTED,stroke_width=3,max_tip_length_to_length_ratio=.5) for i in range(3)]);self.reveal(edges)
  repeat=CurvedArrow(nodes[-1].get_bottom()+DOWN*.1,nodes[0].get_bottom()+DOWN*.1,angle=-TAU/5,color=PALE)
  self.reveal(repeat)
  self.cue('overly large step');n=self.note('Learning rate controls step size',-1.6)
  self.cue('We also evaluate');self.change([n],box('Evaluate on held-out data',8,.95,38).move_to([0,-1.7,0]))
  self.cue('Useful learning');self.note('Training progress needs an independent check',-3);self.finish()
