"""Native teaching figures. Forward propagation calculations derive from evidence/result.json."""
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
        self.title('The Route Through a Network')
        inputs=VGroup(box('Input 1',2.4),box('Input 2',2.4)).arrange(DOWN,buff=.75).move_to([-4.7,.5,0])
        hidden=VGroup(box('Hidden 1',2.4),box('Hidden 2',2.4)).arrange(DOWN,buff=.75).move_to([0,.5,0])
        out=box('Output',2.4).move_to([4.7,.5,0])
        edges=VGroup(*[arrow(a.get_right(),b.get_left()) for a in inputs for b in hidden],*[arrow(b.get_right(),out.get_left()) for b in hidden])
        self.reveal(inputs);self.cue('two hidden units');self.reveal(hidden);self.cue('one output');self.reveal(out,edges)
        self.cue('The weights and biases');self.note('Weights + biases = parameters',-2.3)
        self.cue('we keep them fixed');self.note('Fixed during this forward pass',-3.05)
        self.cue('First we combine');self.play(Indicate(hidden,color=ACC),run_time=.7)
        self.cue('into a prediction');self.play(Indicate(out,color=ACC),run_time=.7);self.finish()

class B03_Scene(Base):
    def construct(self):
        self.title('One Unit, One Calculation')
        self.reveal(formula(r'x=(2,\ 1)',1.8,3.4))
        self.cue('one half and negative one');weights=formula(r'w_1=(0.5,\ -1)',.5,5);self.reveal(weights)
        self.cue('That gives');products=formula(r'(0.5\times2)+(-1\times1)=1-1',-.9,9);self.reveal(products)
        self.cue('the total is zero');zero=formula(r'1-1=0',-2.1,3.5);self.reveal(zero)
        self.cue('Now add the bias');bias=formula(r'z_1=0+1=1',-2.1,5);self.change([zero],bias)
        self.cue('A bias shifts');self.change([weights,products],text('Bias shifts the weighted sum',40).move_to([0,0,0]));self.finish()

class B04_Scene(Base):
    def construct(self):
        self.title('The Other Hidden Unit')
        self.reveal(formula(r'x=(2,\ 1)',1.8,3.4))
        self.cue('Its weights');self.reveal(formula(r'w_2=(-1,\ 1)\qquad b_2=0.5',.5,7.6))
        self.cue('Negative two');self.reveal(formula(r'z_2=(-1\times2)+(1\times1)+0.5=-0.5',-1,11))
        self.cue('We now have');self.reveal(formula(r'z=(1,\ -0.5)',-2.45,4.5));self.finish()

class B05_Scene(Base):
    def construct(self):
        self.title('Apply the Activation')
        eq=formula(r'\operatorname{ReLU}(z)=\max(0,z)',2,6);self.reveal(eq)
        axes=Axes(x_range=[-2,2,1],y_range=[0,2,1],x_length=6,y_length=2.5,axis_config={'color':MUTED,'include_tip':False}).move_to([-2.5,-.3,0])
        curve=VMobject(color=INK,stroke_width=5).set_points_as_corners([axes.c2p(-2,0),axes.c2p(0,0),axes.c2p(2,2)])
        labels=VGroup(text('Input',28).next_to(axes.x_axis,DOWN,buff=.2),text('Output',28).next_to(axes.y_axis,LEFT,buff=.15))
        self.reveal(axes,labels);self.play(Create(curve),run_time=.6)
        self.cue('Watch negative one half');dot=Dot(axes.c2p(-.5,0),color=ACC,radius=.09);a=mathsvg(r'-0.5\ \rightarrow\ 0',3.3).move_to([3.5,.5,0]);self.reveal(dot,a)
        self.cue('while one stays one');self.play(MoveAlongPath(dot,VMobject().set_points_as_corners([axes.c2p(-.5,0),axes.c2p(0,0),axes.c2p(1,1)])),run_time=.5);b=mathsvg(r'1\ \rightarrow\ 1',3.3).move_to([3.5,-.6,0]);self.reveal(b)
        self.cue('now sends');self.reveal(formula(r'h=(1,\ 0)',-2.75,3.5));self.finish()

class B06_Scene(Base):
    def construct(self):
        self.title('From Hidden Values to Prediction')
        self.reveal(formula(r'h=(1,\ 0)',1.85,3.5))
        self.cue('weights two and negative one');self.reveal(formula(r'w_{\mathrm{out}}=(2,\ -1)\qquad b_{\mathrm{out}}=0.5',.55,11.8))
        self.cue('Two times one');self.reveal(formula(r'\hat{y}=2\times1-1\times0+0.5=2.5',-1,11.8))
        self.cue('toy regression model');self.reveal(text('Linear output · constructed regression example',32,MUTED).move_to([0,-2.5,0]))
        self.finish()

class B07_Scene(Base):
    def construct(self):
        self.title('A Layer in Matrix Form')
        top=formula(r'z=Wx+b\qquad h=\operatorname{ReLU}(z)',1.9,9);self.reveal(top)
        W=matrix([[.5,-1],[-1,1]],[-3.8,-.2,0],3)
        x=matrix([[2],[1]],[0,-.2,0],.8)
        bias=matrix([[1],[.5]],[3.6,-.2,0],1.1)
        labs=VGroup(text('W · 2 × 2',32).move_to([-3.8,-1.65,0]),text('x · 2 × 1',32).move_to([0,-1.65,0]),text('b · 2 × 1',32).move_to([3.6,-1.65,0]),text('+',44).move_to([1.8,-.2,0]))
        self.cue('Each row');self.reveal(W);self.play(Indicate(W[0][:2],color=ACC),run_time=.7)
        self.cue('Multiply by');self.reveal(x)
        self.cue('add the bias vector');self.reveal(bias,labs)
        self.cue('apply ReLU');self.reveal(formula(r'(1,\ -0.5)\ \rightarrow\ (1,\ 0)',-2.75,7))
        self.finish()

class B08_Scene(Base):
    def construct(self):
        self.title('Why the Activation Matters')
        subtitle=text('Without the hidden activation',38).move_to([0,1.9,0]);self.reveal(subtitle)
        a=formula(r'W_{\mathrm{out}}(Wx+b)+b_{\mathrm{out}}',.5,8);self.cue('One weighted sum');self.reveal(a)
        b=formula(r'=(W_{\mathrm{out}}W)x+(W_{\mathrm{out}}b+b_{\mathrm{out}})',-1,11);self.cue('combined into');self.reveal(b)
        label=self.note('One affine transformation',-2.4)
        self.cue('The activation changes');self.change([a,b,label,subtitle],text('A nonlinear activation changes the mapping',38).move_to([0,1,0]))
        axes=Axes(x_range=[-2,2,1],y_range=[0,2,1],x_length=7,y_length=2.5,axis_config={'color':MUTED,'include_tip':False}).move_to([0,-1,0]);curve=VMobject(color=ACC,stroke_width=5).set_points_as_corners([axes.c2p(-2,0),axes.c2p(0,0),axes.c2p(2,2)])
        self.cue('ReLU adds a bend');self.reveal(axes);self.play(Create(curve),run_time=.7);self.finish()

class B09_Scene(Base):
    def construct(self):
        self.title('Change One Input')
        self.reveal(text('Same weights and biases',34).move_to([0,2.15,0]))
        left=VGroup(text('Original input',34).move_to([-3.5,1.3,0]),mathsvg(r'x=(2,1)',3.2).move_to([-3.5,.4,0]),mathsvg(r'z=(1,-0.5)',3.5).move_to([-3.5,-.5,0]),mathsvg(r'h=(1,0)',3.2).move_to([-3.5,-1.4,0]),mathsvg(r'\hat{y}=2.5',2.4).move_to([-3.5,-2.3,0]));self.reveal(left)
        self.cue('change the second input');header=text('Changed input',34).move_to([3.5,1.3,0]);x=mathsvg(r'x=(2,3)',3.2).move_to([3.5,.4,0]);self.reveal(header,x)
        self.cue('hidden sums become');z=mathsvg(r'z=(-1,1.5)',3.5).move_to([3.5,-.5,0]);self.reveal(z)
        self.cue('ReLU turns');h=mathsvg(r'h=(0,1.5)',3.2).move_to([3.5,-1.4,0]);self.reveal(h)
        self.cue('output becomes');y=mathsvg(r'\hat{y}=-1',2.4).move_to([3.5,-2.3,0]);self.reveal(y)
        self.cue('only the input changed');self.note('Changed input ≠ parameter update',-3.2);self.finish()

class B10_Scene(Base):
    def construct(self):
        self.title('Where Learning Fits')
        forward=box('Forward pass',3.5).move_to([-4.2,1,0]);pred=box('Prediction',3.5).move_to([.0,1,0]);loss=box('Loss + target',3.5).move_to([4.2,1,0]);self.reveal(forward)
        self.cue('After the prediction');self.reveal(pred,arrow(forward.get_right(),pred.get_left()))
        self.cue('a loss measures');self.reveal(loss,arrow(pred.get_right(),loss.get_left()))
        back=box('Backpropagation',4,.95,36).move_to([3.7,-1.3,0]);update=box('Optimizer update',4,.95,36).move_to([-3.7,-1.3,0])
        self.cue('Backpropagation computes');self.reveal(back,arrow(loss.get_bottom(),back.get_top()))
        self.cue('an optimizer');self.reveal(update,arrow(back.get_left(),update.get_right()))
        self.cue('Our example stopped');self.note('This episode: inputs → prediction',-2.8);self.finish()
