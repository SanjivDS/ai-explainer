"""Native 4K entropy and Gini illustrations, driven by computed evidence and audio cues."""
from pathlib import Path
import json,re
import numpy as np
from manim import *
R=Path(__file__).parent
BS=json.loads((R/'beat_sheet.json').read_text());D=json.loads((R/'evidence/results.json').read_text())
BG='#FAF9F5';INK='#3D3929';ACC='#D97757';SOFT='#625E50';PALE='#C9C5B8'
FONT=R.resolve().parents[3]/'runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf'
def txt(s,size=36,color=INK):
 with register_font(str(FONT)):return Text(s,font='EB Garamond',font_size=size,color=color)
def lab(s,x,y,size=36):return txt(s,size).move_to([x,y,0])
def chip(s,x,y,w=3.5):
 t=lab(s,x,y,34);return VGroup(RoundedRectangle(width=max(w,t.width+.4),height=.8,corner_radius=.1,color=PALE,stroke_width=2).move_to(t),t)
def center(p,color=ACC):return VGroup(Line(np.array(p)+[-.12,-.12,0],np.array(p)+[.12,.12,0],color=color,stroke_width=6),Line(np.array(p)+[-.12,.12,0],np.array(p)+[.12,-.12,0],color=color,stroke_width=6))
class Base(Scene):
 def setup(self):
  self.camera.background_color=BG;self.bid=self.__class__.__name__[:3];self.beat=next(b for b in BS['beats'] if b['beat_id']==self.bid);self.dur=self.beat['actual_duration_s'];self.add(txt('@sanjiv',30,SOFT).move_to([5.25,-3.35,0]))
 def head(self,title,sub=''):
  self.add(lab(title,0,3.03,48))
  if sub:self.add(lab(sub,0,2.35,30))
 def until(self,f):
  sec=self.dur*f
  if sec>self.renderer.time:self.wait(sec-self.renderer.time)
 def cue(self,s,f):
  p=R/'mp3/words.json'
  if p.exists():
   w=json.loads(p.read_text())['beats'].get(self.bid,[]);wanted=re.sub('[^a-z0-9 ]','',s.lower()).split()
   for k in range(len(w)-len(wanted)+1):
    if [re.sub('[^a-z0-9]','',q['text'].lower()) for q in w[k:k+len(wanted)]]==wanted:
     t=w[k]['startFrame']/24
     if t>self.renderer.time:self.wait(t-self.renderer.time)
     return
  self.until(f)
 def end(self):self.until(1)
def equation(name,x,y,w=6):
 m=SVGMobject(str(R/'math'/f'{name}.svg'));m.set_color(INK);m.scale_to_fit_width(w);return m.move_to([x,y,0])
def dots(a,b,x,y,cols=5,space=.55):
 return VGroup(*[Dot([x+(i%cols-(min(a+b,cols)-1)/2)*space,y-(i//cols)*space,0],radius=.14,color=ACC if i<a else INK) for i in range(a+b)])
def mixbar(a,b,x,y,w=4,h=.35):
 n=a+b;left=x-w/2;g=VGroup()
 for count,color in [(a,ACC),(b,INK)]:
  if count:g.add(Rectangle(width=w*count/n,height=h,stroke_width=0,fill_color=color,fill_opacity=1).move_to([left+w*count/n/2,y,0]));left+=w*count/n
 return g
class B02_Scene(Base):
 def construct(self):
  self.head('Labels Define the Mix','Constructed examples • A = terracotta • B = ink')
  cloud=dots(4,1,0,.8);tag=lab('4 A + 1 B',0,-.1,44)
  self.play(FadeIn(cloud),FadeIn(tag),run_time=1)
  self.cue('eighty percent',.23);shares=lab('80% A     20% B',0,-1.1,40);self.play(FadeIn(shares),run_time=.7)
  self.cue('A pure node',.4);self.play(FadeOut(cloud),FadeOut(tag),FadeOut(shares),run_time=.4)
  pure=VGroup(lab('Pure',-3.5,1.25,44),dots(5,0,-3.5,.2),lab('One class',-3.5,-1.15,38))
  balanced=VGroup(lab('Balanced',3.4,1.25,44),dots(5,5,3.4,.5),lab('Equal shares',3.4,-1.15,38))
  self.play(FadeIn(pure),run_time=.7);self.cue('A balanced binary',.52);self.play(FadeIn(balanced),run_time=.7)
  self.cue('Both measures are zero',.65);self.play(FadeIn(lab('Gini = 0     Entropy = 0',-3.5,-2.1,33)),FadeIn(lab('Binary maximum',3.4,-2.1,36)),run_time=.7);self.end()
class B03_Scene(Base):
 def construct(self):
  self.head('Gini: The Chance of Disagreement','Two independent label draws, with replacement')
  cells=VGroup();bad=[]
  for row in range(5):
   for col in range(5):
    mismatch=(row<4)!=(col<4)
    cell=Square(side_length=.46,stroke_color=PALE,stroke_width=2,fill_color=PALE,fill_opacity=.4).move_to([-4.65+col*.55,1.25-row*.55,0]);cells.add(cell)
    if mismatch:bad.append(cell)
  labels=VGroup(*[lab('A' if i<4 else 'B',-4.65+i*.55,1.88,30) for i in range(5)],*[lab('A' if i<4 else 'B',-5.25,1.25-i*.55,30) for i in range(5)])
  self.play(FadeIn(cells),FadeIn(labels),run_time=1)
  self.cue('Eight pairs disagree',.42);self.play(*[c.animate.set_fill(ACC,opacity=1) for c in bad],run_time=.8)
  self.play(FadeIn(lab('8 of 25 pairs disagree',-3.55,-1.8,36)),FadeIn(lab('Gini = 0.32',3.3,1.15,48)),run_time=.7)
  self.cue('The formula subtracts',.65);self.play(FadeIn(equation('gini',3.3,-.4,4.4)),FadeIn(lab('p = class share; C = class count',3.2,-1.85,29)),run_time=.7)
  self.cue('not the error rate',.84);self.play(FadeIn(lab('Majority-vote error here: 0.20',0,-2.7,36)),run_time=.7);self.end()
class B04_Scene(Base):
 def construct(self):
  self.head('Entropy: Average Surprise','Base-two logarithms measure surprise in bits')
  self.play(FadeIn(equation('entropy',-3.25,.55,4.8)),run_time=.8)
  self.add(lab('p = class share',-3.25,-.95,34))
  barA=Rectangle(width=3.2,height=.3,fill_color=INK,fill_opacity=.9,stroke_color=INK,stroke_width=3).move_to([2.8,.65,0])
  barB=Rectangle(width=.8,height=.3,fill_color=INK,fill_opacity=1,stroke_width=0).move_to([1.6,-.6,0])
  self.cue('eighty percent',.25);a=lab('80% A  →  0.322 bits',3.3,1.25,33);self.play(FadeIn(a),GrowFromEdge(barA,LEFT),run_time=.8)
  self.cue('twenty percent',.45);b=lab('20% B  →  2.322 bits',3.3,0,33);self.play(FadeIn(b),GrowFromEdge(barB,LEFT),run_time=.8)
  self.cue('Weight those surprises',.61);self.play(FadeIn(equation('entex',0,-1.8,10.5)),run_time=.9)
  self.cue('probability zero',.83);self.play(FadeIn(lab('Zero-probability classes contribute 0.',0,-2.7,34)),run_time=.7);self.end()
class B05_Scene(Base):
 def construct(self):
  self.head('Same Endpoints, Different Curves','Binary case • Gini doubled here to compare shapes')
  pt=lambda p,v:np.array([-5.3+7.1*p,-2.1+3.8*v,0])
  axes=VGroup(Line(pt(0,0),pt(1,0),color=PALE),Line(pt(0,0),pt(0,1.06),color=PALE))
  labs=VGroup(lab('0',-5.3,-2.55,32),lab('0.5',-1.75,-2.55,32),lab('1',1.8,-2.55,32),lab('Class A share',-1.8,-3.1,30),lab('1',-5.7,1.7,32))
  h=VMobject(color=ACC,stroke_width=5).set_points_as_corners([pt(x['p'],x['entropy']) for x in D['curves']]);g=VMobject(color=INK,stroke_width=5).set_points_as_corners([pt(x['p'],2*x['gini']) for x in D['curves']])
  self.play(Create(axes),FadeIn(labs),Create(g),Create(h),run_time=1.8)
  self.add(txt('Entropy',36,ACC).move_to([4,1.45,0]),lab('2 × Gini',4,.7,36))
  dot=Dot(pt(0,0),radius=.1,color=ACC);self.add(dot)
  self.cue('peak in the middle',.18);self.play(MoveAlongPath(dot,h,rate_func=linear),run_time=2.0)
  self.cue('Gini is one half',.35);self.play(FadeIn(lab('At 50 / 50',4,-.35,38)),FadeIn(lab('Gini: 0.5',4,-1.05,36)),FadeIn(lab('Entropy: 1 bit',4,-1.75,36)),run_time=.8)
  self.cue('more sharply',.63);self.play(Indicate(h,scale_factor=1,color=ACC),run_time=1);self.end()
class B06_Scene(Base):
 def construct(self):
  self.head('Weight Every Child','Constructed split • 8 A + 2 B • 10 records total')
  cloud=dots(8,2,0,1.2);self.play(FadeIn(cloud),run_time=.8)
  self.cue('Send four A labels',.22)
  left=dots(4,0,-3.6,1.0);right=dots(4,2,3.4,1.0,cols=6)
  self.play(*[cloud[i].animate.move_to((left if i<4 else right)[i if i<4 else i-4].get_center()) for i in range(10)],run_time=1.2)
  labels=VGroup(lab('Left: 4 records',-3.6,.2,36),lab('Right: 6 records',3.4,.2,36),lab('Gini: 0',-3.6,-.55,38),lab('Gini: 0.444…',3.4,-.55,38))
  self.cue('left child is pure',.4);self.play(FadeIn(labels),run_time=.8)
  self.cue('Weight each child',.56);self.play(FadeIn(equation('weight',0,-1.65,10.8)),run_time=1)
  self.cue('Subtract that',.82);self.play(FadeIn(equation('reduction',0,-2.75,7.5)),run_time=.7);self.end()
def recordrow(a,b,x,y):
 return VGroup(*[Circle(radius=.105,stroke_color=INK,stroke_width=2,fill_color=ACC if i<a else INK,fill_opacity=1).move_to([x+(i-(a+b-1)/2)*.26,y,0]) for i in range(a+b)])
class B07_Scene(Base):
 def construct(self):
  self.head('The Rankings Can Flip','Same constructed parent: 10 A + 10 B')
  self.add(lab('Split A',-3.3,1.55,42),lab('Split B',3.3,1.55,42))
  ga=VGroup(recordrow(1,7,-3.3,.8),lab('1 A + 7 B',-3.3,.25,32),recordrow(9,3,-3.3,-.35),lab('9 A + 3 B',-3.3,-.9,32))
  gb=VGroup(recordrow(0,5,3.3,.8),lab('0 A + 5 B',3.3,.25,32),recordrow(10,5,3.3,-.35),lab('10 A + 5 B',3.3,-.9,32))
  self.cue('Split A makes',.22);self.play(FadeIn(ga),run_time=.8)
  self.cue('Split B isolates',.43);self.play(FadeIn(gb),run_time=.8)
  self.cue('weighted Gini favors A',.62)
  gini=VGroup(txt('Gini: 0.3125  ✓',36,INK).move_to([-3.3,-1.85,0]),lab('Gini: 0.3333',3.3,-1.85,36));self.play(FadeIn(gini),run_time=.7)
  self.cue('Weighted entropy favors B',.72);ent=VGroup(lab('Entropy: 0.7042',-3.3,-2.7,36),txt('Entropy: 0.6887  ✓',36,INK).move_to([3.3,-2.7,0]));self.play(FadeIn(ent),gini[0].animate.set_color(INK),run_time=.7);self.end()
class B08_Scene(Base):
 def construct(self):
  self.head('Training Purity Is Not Test Performance','Constructed illustration • training labels vs new labels')
  box=RoundedRectangle(width=4,height=2.9,corner_radius=.18,stroke_color=PALE).move_to([-3,-.1,0]);training=dots(6,0,-3,.8,cols=3,space=.6)
  self.play(Create(box),FadeIn(training),FadeIn(lab('Training leaf',-3,1.8,34)),run_time=1)
  score=lab('Training impurity: 0',-3,-2.05,35);self.play(FadeIn(score),run_time=.6)
  arriving=dots(2,2,3.8,.8,cols=2,space=.6)
  self.cue('receive new examples',.2);tag=lab('New labels',3.6,1.8,34);self.play(FadeIn(arriving),FadeIn(tag),run_time=.7)
  self.play(*[arriving[i].animate.move_to([-3.6+(i%2)*.6,-.65-(i//2)*.6,0]) for i in range(4)],run_time=1.5)
  self.cue('Compare criteria',.53);self.play(FadeOut(tag),FadeIn(lab('Same validation plan',3.3,1.3,38)),FadeIn(lab('Limit tree size',3.3,.25,38)),run_time=.8)
  self.cue('held out data',.74);self.play(FadeIn(lab('Measure held-out predictions',3.1,-1,34)),FadeIn(lab('Choose a task-relevant metric.',0,-2.85,37)),run_time=.8);self.end()
