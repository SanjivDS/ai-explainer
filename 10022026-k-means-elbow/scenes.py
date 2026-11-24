"""Native 4K K-means illustrations, driven by computed evidence and audio cues."""
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
class B02_Scene(Base):
 def construct(self):
  self.head('Assign. Average. Repeat.')
  steps=VGroup(*[chip(s,x,1.9,3.3) for s,x in [('1. Choose K',-4.2),('2. Assign',0),('3. Average',4.2)]])
  self.play(FadeIn(steps[0]),run_time=.7)
  pts=np.array([[-4,-1],[-3.5,-.4],[-2.7,-1.2],[-3,-1.8],[2,-.7],[2.5,-1.7],[3.6,-1.1],[3.1,-.1]])
  dots=VGroup(*[Dot([*p,0],radius=.1,color=INK) for p in pts]);c1=center([-4.9,.3,0]);c2=center([4.9,.3,0],INK)
  self.cue('Start those centers',.2);self.play(FadeIn(dots),FadeIn(c1),FadeIn(c2),run_time=1)
  links=VGroup(*[Line(d.get_center(),c1.get_center() if i<4 else c2.get_center(),color=PALE,stroke_width=3) for i,d in enumerate(dots)])
  self.cue('Assign every point',.34);self.play(FadeIn(steps[1]),Create(links),run_time=1.2)
  self.cue('then move',.47);self.play(FadeIn(steps[2]),FadeOut(links),c1.animate.move_to([*pts[:4].mean(0),0]),c2.animate.move_to([*pts[4:].mean(0),0]),run_time=1.6)
  self.cue('Repeat',.65);self.play(Circumscribe(steps[1],color=ACC),run_time=.7);self.play(Circumscribe(steps[2],color=ACC),run_time=.7)
  self.cue('K is your input',.8);self.play(FadeIn(lab('You choose the number of centers.',0,-2.65,38)),run_time=.7);self.end()
class B03_Scene(Base):
 def construct(self):
  self.head('Move the Means','Constructed example: four points, K = 2')
  pos=lambda v,y:np.array([-5.4+1.2*v,y,0])
  axis=Line(pos(0,-.25),pos(9.6,-.25),color=PALE,stroke_width=3)
  dots=VGroup(*[Dot(pos(v,-.25),radius=.12,color=INK) for v in [1,2,8,9]])
  nums=VGroup(*[lab(str(v),pos(v,0)[0],-.85,40) for v in [1,2,8,9]])
  a=center(pos(1,1));b=center(pos(2,1),INK)
  self.play(Create(axis),FadeIn(dots),FadeIn(nums),run_time=1)
  self.cue('initially',.15);self.play(FadeIn(a),FadeIn(b),run_time=.8)
  links=VGroup(*[Line(d.get_center(),a.get_center() if i==0 else b.get_center(),color=PALE,stroke_width=3) for i,d in enumerate(dots)])
  self.play(Create(links),run_time=1)
  self.cue('its average moves',.44);self.play(FadeOut(links),b.animate.move_to(pos(19/3,1)),run_time=1.5);tag=lab('Second center: 6.33',2.3,1.6,34);self.play(FadeIn(tag),run_time=.5)
  self.cue('Reassign',.64);self.play(Circumscribe(dots[1],color=ACC),FadeOut(tag),run_time=.8)
  self.cue('centers settle',.74);self.play(a.animate.move_to(pos(1.5,1)),b.animate.move_to(pos(8.5,1)),run_time=1.4)
  self.play(FadeIn(lab('Mean: 1.5',pos(1.5,0)[0],1.65,36)),FadeIn(lab('Mean: 8.5',pos(8.5,0)[0],1.65,36)),FadeIn(lab('Memberships stop changing.',0,-2.35,38)),run_time=.7);self.end()
class B04_Scene(Base):
 def construct(self):
  self.head('Large Misses Cost More','Inertia: sum of squared distances to assigned centers')
  small=Square(side_length=.7,color=INK,fill_color=INK,fill_opacity=.85).move_to([-3.5,-.2,0]);big=Square(side_length=2.1,color=ACC,fill_color=ACC,fill_opacity=.85).move_to([3.2,-.2,0])
  first=VGroup(lab('Distance 1',-3.5,1.55,40),small,lab('Contribution: 1',-3.5,-1.9,38));second=VGroup(lab('Distance 3',3.2,1.55,40),big,lab('Contribution: 9',3.2,-1.9,38))
  self.cue('A distance of one',.17);self.play(FadeIn(first),run_time=1)
  self.cue('A distance of three',.28);self.play(FadeIn(second),run_time=1);self.until(.54)
  self.play(FadeOut(first),FadeOut(second),run_time=.6)
  values=VGroup(*[chip('0.25',x,.2,2) for x in [-4.5,-1.5,1.5,4.5]])
  self.cue('every point finishes',.62);self.play(FadeIn(lab('Each final distance: 0.5',0,1.5,40)),LaggedStart(*[FadeIn(v) for v in values],lag_ratio=.12),run_time=1.2)
  self.cue('sum to one',.8);self.play(FadeIn(lab('Total inertia: 1',0,-1.5,54)),run_time=.7);self.end()
def curve_graph(vals,x0=-5.4,y0=-2.2,w=7.1,h=3.7):
 ymax=max(vals);pt=lambda k,v:np.array([x0+(k-1)*w/5,y0+v*h/ymax,0])
 axes=VGroup(Line([x0,y0,0],[x0+w,y0,0],color=PALE,stroke_width=3),Line([x0,y0,0],[x0,y0+h,0],color=PALE,stroke_width=3))
 labs=VGroup(*[lab(str(k),pt(k,0)[0],y0-.38,32) for k in range(1,7)],lab('K',x0+w+.35,y0,34),lab('Inertia',x0+.4,y0+h+.38,34))
 path=VMobject(color=INK,stroke_width=5).set_points_as_corners([pt(k,v) for k,v in enumerate(vals,1)])
 dots=VGroup(*[Dot(pt(k,v),radius=.08,color=INK) for k,v in enumerate(vals,1)])
 return axes,labs,path,dots,pt
class B05_Scene(Base):
 def construct(self):
  self.head('Find the Diminishing Gain','Computed example: 18 synthetic points')
  vals=[x['inertia'] for x in D['elbow']];axes,labs,path,dots,pt=curve_graph(vals)
  self.play(Create(axes),FadeIn(labs),run_time=1);self.play(Create(path),FadeIn(dots),run_time=2)
  cloud=VGroup(*[Dot([4.15+p[0]*.48,.5+(p[1]-1.5)*.48,0],radius=.065,color=INK) for p in D['points']])
  self.play(FadeIn(cloud),run_time=.7)
  self.cue('With one center',.2);self.play(FadeOut(cloud),run_time=.4)
  notes=VGroup(*[lab(s,4.2,y,36) for s,y in [('K = 1: 148.08',1.35),('K = 2: 58.08',.45),('K = 3: 4.08',-.45)]])
  for phrase,f,n in zip(['With one center','With two','With three'],[.2,.31,.38],notes):self.cue(phrase,f);self.play(FadeIn(n),run_time=.6)
  self.cue('After that',.5);self.play(AnimationGroup(*[Indicate(d,color=ACC,scale_factor=1.25) for d in dots[3:]]),run_time=1.4)
  self.cue('That bend near three',.64);self.play(Circumscribe(dots[2],color=ACC,buff=.16),FadeIn(lab('Candidate: K = 3',4.1,-1.65,38)),run_time=1);self.end()
class B06_Scene(Base):
 def construct(self):
  self.head('Scale Changes Similarity','Same four observations; different feature weighting')
  self.add(lab('Original scale',-3.5,1.6,40),lab('Rescaled feature',3.5,1.6,40))
  positions=[np.array([[-4.8,-1.5],[-4.8,.6],[-2.2,-1.5],[-2.2,.6]]),np.array([[2.2,-1.5],[2.2,.6],[4.8,-1.5],[4.8,.6]])]
  grids=[]
  for j,arr in enumerate(positions):
   dots=VGroup(*[Dot([*v,0],radius=.14,color=INK) for v in arr]);grids.append(dots)
  self.play(FadeIn(grids[0]),run_time=1)
  a=VGroup(*[Line(grids[0][i].get_center(),grids[0][i+2].get_center(),color=ACC,stroke_width=5) for i in [0,1]])
  leftnotes=VGroup(lab('Feature A: 0–1',-3.5,-2.25,32),lab('Feature B: 0–10',-3.5,-2.75,32))
  self.cue('larger scale',.32);self.play(Create(a),FadeIn(leftnotes),run_time=1)
  self.cue('Rescale that feature',.42);self.play(TransformFromCopy(grids[0],grids[1]),run_time=1)
  b=VGroup(*[Line(grids[1][i].get_center(),grids[1][i+1].get_center(),color=ACC,stroke_width=5) for i in [0,2]])
  self.play(Create(b),FadeIn(lab('Feature A: 0–1',3.5,-2.25,32)),FadeIn(lab('Feature B: 0–0.5',3.5,-2.75,32)),run_time=1)
  self.cue('Standardization can help',.61);self.play(FadeIn(lab('Panel axes rescaled for display.',0,.98,30)),run_time=.7);self.end()
class B07_Scene(Base):
 def construct(self):
  self.head('Two Centers, Wrong Shape','Computed fit on two synthetic curved bands')
  pts=np.array(D['moons']);labels=np.array(D['moon_labels']);groups=[]
  for xshift in [-3.4,3.4]:
   g=VGroup(*[Dot([(p[0]-.5)*1.6+xshift,(p[1]-.25)*1.6-.3,0],radius=.072,color=INK) for p in pts]);groups.append(g)
  self.play(FadeIn(groups[0]),FadeIn(lab('Curved bands',-3.4,1.8,40)),run_time=1.2)
  self.cue('K means with two centers',.22);self.play(TransformFromCopy(groups[0],groups[1]),FadeIn(lab('Nearest centers',3.4,1.8,38)),run_time=1.2)
  self.play(*[dot.animate.set_color(ACC) for i,dot in enumerate(groups[0]) if i<30],*[dot.animate.set_color(ACC) for i,dot in enumerate(groups[1]) if labels[i]==0],run_time=1)
  self.cue('It prefers compact groups',.5);self.play(FadeIn(lab('Nearest-center geometry does not follow the bands.',0,-2.55,34)),run_time=.7);self.end()
class B08_Scene(Base):
 def construct(self):
  self.head('Sometimes There Is No Elbow','Computed counterexample: evenly spaced points on a line')
  vals=[v['inertia'] for v in D['uniform_elbow']];axes,labs,path,dots,pt=curve_graph(vals,w=6.8)
  self.play(Create(axes),FadeIn(labs),run_time=1);self.play(Create(path),FadeIn(dots),run_time=2)
  cloud=VGroup(*[Dot([2.4+i*.13,1.6,0],radius=.045,color=INK) for i in range(24)])
  self.cue('evenly spaced',.13);self.play(FadeIn(cloud),run_time=.8)
  self.cue('Their inertia still falls',.25);self.play(Indicate(path,color=ACC),run_time=1)
  notes=VGroup(*[lab(s,4.2,y,34) for s,y in [('Silhouette',.5),('Stability',-.4),('Usefulness',-1.3)]])
  self.cue('Compare nearby choices',.62);self.play(LaggedStart(*[FadeIn(n) for n in notes],lag_ratio=.25),run_time=1.5)
  self.cue('ambiguous',.9);self.play(FadeIn(lab('A smaller score is not proof of categories.',0,-2.92,32)),run_time=.7);self.end()
