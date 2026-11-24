"""Native 4K cross-validation illustrations, driven by computed evidence and audio cues."""
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
def box(text,x,y,w=3.2,h=.8,size=34,accent=False):
 t=lab(text,x,y,size);return VGroup(RoundedRectangle(width=w,height=h,corner_radius=.08,stroke_color=INK if accent else PALE,stroke_width=4 if accent else 2,fill_color=BG,fill_opacity=1).move_to([x,y,0]),t)
def arrow(a,b):return Arrow(a,b,buff=.12,color=INK,stroke_width=4,max_tip_length_to_length_ratio=.12)
class B02_Scene(Base):
 def construct(self):
  self.head('One Procedure, Two Partitions','Recorded synthetic regression • lower RMSE is better')
  allids=D['development'];panels=[]
  for j,x in enumerate([-3.4,3.4]):
   row=D['holdouts'][j];vs=set(row['validation']);dots=VGroup(*[Dot([x+(i%10-4.5)*.3,1.35-(i//10)*.28,0],radius=.08,color=ACC if k in vs else INK) for i,k in enumerate(allids)])
   p=VGroup(lab(f"Split seed {row['seed']}",x,1.78,31),dots,lab('80 train / 20 validate',x,-1.6,34));panels.append(p)
  self.play(FadeIn(panels[0]),run_time=1);self.cue('two different random partitions',.2);self.play(FadeIn(panels[1]),run_time=1)
  self.cue('first root mean squared error',.4);self.play(FadeIn(lab(f"RMSE: {D['holdouts'][0]['rmse']:.3f}",-3.4,-2.55,46)),run_time=.8)
  self.cue('The second',.57);self.play(FadeIn(lab(f"RMSE: {D['holdouts'][1]['rmse']:.3f}",3.4,-2.55,46)),run_time=.8);self.end()
class B03_Scene(Base):
 def construct(self):
  self.head('Rotate the Held-Out Fold','100 development records • five folds of 20')
  xs=[-3.8,-2.45,-1.1,.25,1.6];ys=[1.05,.35,-.35,-1.05,-1.75]
  self.add(*[lab(f'F{i+1}',x,1.8,30) for i,x in enumerate(xs)])
  test=VGroup(box('Final test',4.4,.7,2.5,1,34),lab('40 records',4.4,-.3,34),lab('CLOSED',4.4,-1.1,34));self.add(test)
  for i,y in enumerate(ys):
   row=VGroup(lab(f'Fit {i+1}',-5.45,y,31),*[box('V' if k==i else 'T',x,y,1,.48,27,accent=k==i) for k,x in enumerate(xs)])
   self.until(.08+i*.11);self.play(FadeIn(row),run_time=.65)
  self.cue('Every record is validated once',.68);self.play(FadeIn(lab('T = training     V = validation',-1.3,-2.7,35)),run_time=.7);self.end()
class B04_Scene(Base):
 def construct(self):
  self.head('See the Variation','Recorded cubic-model RMSE • identical five-fold partition')
  vals=D['cv']['3']['scores'];xs=[-4.8,-2.4,0,2.4,4.8];bottom=-1.1;scale=2.8/.65
  axis=Line([-5.6,bottom,0],[5.6,bottom,0],color=PALE);self.add(axis);chart=VGroup(axis)
  for i,(x,v) in enumerate(zip(xs,vals)):
   bar=Rectangle(width=1.2,height=v*scale,stroke_width=0,fill_color=INK,fill_opacity=.85).move_to([x,bottom+v*scale/2,0]);num=lab(f'{v:.3f}',x,1.85,33);tag=lab(f'Fold {i+1}',x,-1.65,33);chart.add(bar,num,tag)
   self.play(GrowFromEdge(bar,DOWN),FadeIn(num),FadeIn(tag),run_time=.45)
  mean=D['cv']['3']['mean'];line=DashedLine([-5.6,bottom+mean*scale,0],[5.6,bottom+mean*scale,0],color=ACC,stroke_width=5);meanlabel=lab(f'Mean RMSE: {mean:.3f}',0,-2.45,43)
  self.cue('Their mean',.32);self.play(Create(line),FadeIn(meanlabel),run_time=.8);chart.add(line,meanlabel)
  self.cue('not five independent experiments',.65);self.play(FadeOut(chart),run_time=.5)
  rows=[]
  for i,y in enumerate([.85,-.35]):
   row=VGroup(*[box('Validate' if k==i else 'Train',x,y,1.85,.8,27,accent=k==i) for k,x in enumerate([-4.2,-2.1,0,2.1,4.2])]);rows.append(row)
  self.play(FadeIn(VGroup(*rows)),run_time=.7)
  overlap=VGroup(*[rows[i][k] for i in range(2) for k in [2,3,4]])
  self.play(Circumscribe(overlap,color=ACC),FadeIn(lab('Training sets overlap.',0,-1.7,40)),run_time=.9)
  self.play(FadeIn(lab('Fold spread is not a confidence interval.',0,-2.7,36)),run_time=.7);self.end()
class B05_Scene(Base):
 def construct(self):
  self.head('Select, Refit, Then Test','Recorded synthetic experiment • the test set does not select the model')
  lin=box('Linear CV: 0.774',-3.4,1.25,4.4,1.05,39);cub=box('Cubic CV: 0.534',3.4,1.25,4.4,1.05,39)
  self.play(FadeIn(lin),run_time=.7);self.cue('the cubic model averages',.25);self.play(FadeIn(cub),run_time=.7)
  self.cue('selects the cubic model',.43);self.play(Circumscribe(cub,color=ACC),run_time=.8)
  self.cue('refit it on all hundred',.6);refit=box('Refit cubic: all 100',0,-.35,4.6,1,39);self.play(FadeIn(refit),GrowArrow(arrow([3.4,.7,0],[1,-.1,0])),run_time=.8)
  self.cue('open the separate test set',.72);test=box('Final test: 40 records',0,-1.7,5.4,.85,37);self.play(FadeIn(test),run_time=.6)
  self.cue('Its error is',.8);self.play(FadeIn(lab(f"Test RMSE: {D['final']['rmse']:.3f}",0,-2.8,42)),run_time=.7);self.end()
class B06_Scene(Base):
 def construct(self):
  self.head('Keep Preprocessing Inside the Fold','Learn parameters from training data only')
  train=box('Training fold',-3.5,1.1,3.5,1,38);val=box('Validation fold',3.5,1.1,3.5,1,38,accent=True);scaler=box('Scaler',0,-.3,2.8,.9,38)
  self.play(FadeIn(train),FadeIn(val),FadeIn(scaler),run_time=.8)
  wrong=arrow([3.5,.6,0],[.8,.1,0]);good=arrow([-3.5,.6,0],[-.8,.1,0]);self.cue('all the development data',.2);self.play(GrowArrow(wrong),GrowArrow(good),run_time=.9)
  warning=lab('Wrong: validation helps fit the scaler',0,-1.8,36);self.play(FadeIn(warning),run_time=.6)
  self.cue('Fit the scaler using only',.48);self.play(FadeOut(wrong),FadeOut(warning),Transform(scaler,box('Fit on training',0,-.3,3.6,.9,36)),run_time=.9)
  fixed=arrow([.8,-.75,0],[3.5,-1.55,0]);apply=box('Apply unchanged',3.5,-2.1,3.9,.85,35)
  self.cue('then apply that fitted transform',.63);self.play(GrowArrow(fixed),GrowArrow(arrow([3.5,.55,0],[3.5,-1.65,0])),FadeIn(apply),run_time=.8)
  self.cue('Feature selection and imputation',.78);self.play(FadeIn(lab('Also: imputation + feature selection',-1.6,-2.9,34)),run_time=.7);self.end()
class B07_Scene(Base):
 def construct(self):
  self.head('Match the Split to Deployment','Preserve the boundaries that matter')
  titles=['Stratify','Group','Time'];xs=[-4.35,0,4.35]
  self.add(*[lab(s,x,1.65,40) for s,x in zip(titles,xs)])
  strat=VGroup(*[Dot([-5.3+j*.6,.75-i*.55,0],radius=.12,color=INK,fill_opacity=0 if j==0 else 1,stroke_width=3) for i in range(3) for j in range(4)])
  self.cue('stratification',.15);self.play(FadeIn(strat),FadeIn(lab('Preserve class shares',-4.35,-1.45,29)),run_time=.8)
  group=VGroup(*[box(f'Patient {i+1}',0,.8-i*.8,2.5,.55,28,accent=i==2) for i in range(3)])
  self.cue('one patient',.33);self.play(FadeIn(group),FadeIn(lab('Keep each entity together',0,-1.95,29)),run_time=.8)
  timeline=VGroup(*[Square(side_length=.5,stroke_color=INK,fill_color=INK,fill_opacity=.2).move_to([3.35+j*.65,.45,0]) for j in range(4)])
  boundary=Line([4.325,-.3,0],[4.325,1.1,0],color=INK,stroke_width=5)
  self.cue('For forecasting',.56);self.play(FadeIn(timeline),Create(boundary),FadeIn(lab('Past → Future',4.35,-1.45,32)),run_time=.8)
  self.cue('earlier data',.62);self.play(boundary.animate.shift(RIGHT*.65),run_time=.8)
  self.cue('wrong question',.78);self.play(FadeIn(lab('Split for the prediction you will actually make.',0,-2.8,36)),run_time=.7);self.end()
class B08_Scene(Base):
 def construct(self):
  self.head('Useful, Not Magic','Validation reduces uncertainty; it does not remove it')
  fits=VGroup(*[box('Fit',-4.6+j*1.15,1.3-i*.9,.85,.55,27) for i in range(2) for j in range(5)])
  self.play(LaggedStart(*[FadeIn(f) for f in fits],lag_ratio=.06),run_time=1.4)
  self.cue('ten model fits',.13);self.play(FadeIn(lab('2 settings × 5 folds = 10 fits',1.6,-.35,37)),run_time=.8)
  self.cue('Searching many settings',.42);outer=VGroup(RoundedRectangle(width=3.8,height=1.8,corner_radius=.1,stroke_color=PALE).move_to([3.9,1.05,0]),lab('Outer evaluation',3.9,1.58,28),box('Tune inside',3.9,.65,2.7,.65,30));self.play(FadeIn(outer),run_time=.7)
  self.cue('separate untouched test',.59);self.play(FadeIn(lab('Untouched test or nested CV',0,-1.65,40)),run_time=.7)
  self.cue('real world changes',.88);self.play(FadeIn(lab('Distribution shift can still break the estimate.',0,-2.8,36)),run_time=.7);self.end()
