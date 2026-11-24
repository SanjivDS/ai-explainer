"""Original native-4K XGBoost teaching diagrams. Data: evidence/result.json."""
import json,re
from pathlib import Path
from manim import *
R=Path(__file__).parent
BS=json.loads((R/'beat_sheet.json').read_text())
DATA=json.loads((R/'evidence/result.json').read_text())
BG='#FAF9F5';INK='#3D3929';ACC='#D97757';SOFT='#625E50';LINE='#888271'
FONT=Path(__file__).resolve().parents[4]/'runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf'

def text(s,size=36,color=INK):
 with register_font(str(FONT)):
  return Text(s,font='EB Garamond',font_size=size,color=color)

def label(s,pos,size=36):return text(s,size).move_to(pos)
def box(s,pos,w=3,h=1.1):
 rect=RoundedRectangle(width=w,height=h,corner_radius=.12,stroke_color=LINE,stroke_width=2,fill_color=BG,fill_opacity=1).move_to(pos)
 t=text(s,34)
 if t.width>w-.3:t.scale_to_fit_width(w-.3)
 return VGroup(rect,t.move_to(pos))
def arrow(a,b,color=INK):return Arrow(a,b,buff=.14,color=color,stroke_width=4,max_tip_length_to_length_ratio=.13)
def branch(pos,scale=1):
 p=np.array(pos); offsets=[np.array([0,.65,0]),np.array([-.7,-.45,0]),np.array([.7,-.45,0])]
 pts=[p+v*scale for v in offsets]
 return VGroup(Line(pts[0],pts[1],color=INK,stroke_width=4),Line(pts[0],pts[2],color=INK,stroke_width=4),*[Dot(q,radius=.1*scale,color=INK) for q in pts])

class Base(Scene):
 def setup(self):
  self.camera.background_color=BG
  self.bid=self.__class__.__name__[:3]
  self.beat=next(b for b in BS['beats'] if b['beat_id']==self.bid)
  self.target_duration=self.beat['actual_duration_s']
  self.add(text('@sanjiv',29,SOFT).move_to([4.85,-3.35,0]))
 def header(self,title,source):
  self.add(text(title,44).move_to([0,3.0,0]))
  self.add(text(source,29,SOFT).move_to([-1.35,-3.35,0]))
 def until(self,fraction):
  goal=self.target_duration*fraction
  if goal>self.renderer.time:self.wait(goal-self.renderer.time)
 def cue(self,phrase,fallback):
  words_path=R/'mp3/words.json'
  if words_path.exists():
   words=json.loads(words_path.read_text()).get('beats',{}).get(self.bid,[])
   target=re.sub(r'[^a-z0-9 ]','',phrase.lower()).split()
   for k in range(len(words)-len(target)+1):
    got=[re.sub(r'[^a-z0-9]','',w['text'].lower()) for w in words[k:k+len(target)]]
    if got==target:
     sec=words[k]['startFrame']/24
     if sec>self.renderer.time:self.wait(sec-self.renderer.time)
     return
  self.until(fallback)
 def end(self):self.until(1)

class B02_Scene(Base):
 def construct(self):
  self.header('Small Trees, Useful Rules','Source: XGBoost model tutorial · simplified')
  root=box('Age < 30?',[-3.5,1.8,0],3.3)
  child=box('Income < 50?',[-4.9,-.1,0],2.65)
  leaf=box('Leaf',[-1.9,-.1,0],2.0)
  self.play(FadeIn(root),run_time=.7)
  self.play(GrowArrow(arrow(root.get_bottom(),child.get_top())),GrowArrow(arrow(root.get_bottom(),leaf.get_top())),FadeIn(child),FadeIn(leaf),run_time=1)
  l=Dot([-5.7,-1.55,0],radius=.12,color=ACC);r=Dot([-4.1,-1.55,0],radius=.12,color=INK)
  self.play(Create(Line(child.get_bottom(),l,color=INK)),Create(Line(child.get_bottom(),r,color=INK)),FadeIn(l),FadeIn(r),run_time=.8)
  self.add(label('Illustrative feature thresholds',[-3.6,-2.4,0],28))
  self.cue('Boosting adds',.30)
  trees=VGroup(*[branch([x,.4,0],.72) for x in [1,3,5]])
  self.play(FadeIn(trees[0]),run_time=.5)
  for j in [1,2]:self.play(FadeIn(trees[j]),FadeIn(label('+',[j*2, .35,0],42)),run_time=.5)
  self.play(FadeIn(label('Add Corrections',[3,1.8,0],38)),run_time=.5)
  self.cue('X G Boost combines',.57)
  chips=VGroup(*[box(s,[x,-1.65,0],1.75,.95) for s,x in [('Loss',.9),('Limits',3),('Search',5.1)]])
  self.play(LaggedStart(*[FadeIn(c) for c in chips],lag_ratio=.2),run_time=1.2)
  self.play(FadeIn(label('Flexible rules + disciplined training',[2.8,-2.6,0],29)),run_time=.5);self.end()

class B03_Scene(Base):
 def construct(self):
  self.header('Correct What Remains','Constructed example · evidence/example.py')
  xs=[-2.4,0,2.4,4.8];ys=[1.65,.7,-.25,-1.2]
  for s,y in zip(['Target','Start','Residual','Updated'],ys):self.add(label(s,[-5,y,0],33))
  vals=DATA['targets']; groups=[]
  for values,y in [(vals,ys[0]),([6]*4,ys[1])]:
   g=VGroup(*[label(str(v),[x,y,0],43) for v,x in zip(values,xs)]);groups.append(g);self.play(FadeIn(g),run_time=.7)
  self.cue('The residuals',.22)
  res=VGroup(*[label(f'{v:+g}',[x,ys[2],0],43) for v,x in zip(DATA['residuals'],xs)])
  self.play(LaggedStart(*[FadeIn(m) for m in res],lag_ratio=.18),run_time=1.1)
  self.cue('A split',.38)
  line=DashedLine([1.2,2.2,0],[1.2,-1.65,0],color=ACC,stroke_width=4)
  self.play(Create(line),run_time=.6)
  av=VGroup(label('Leaf −3',[-1.2,-2,0],35),label('Leaf +3',[3.6,-2,0],35));self.play(FadeIn(av),run_time=.7)
  self.cue('Apply half',.62)
  out=VGroup(*[label(f'{v:g}',[x,ys[3],0],43) for v,x in zip(DATA['prediction'],xs)])
  self.play(FadeIn(out),run_time=.9)
  self.cue('Mean squared error',.84)
  self.play(FadeIn(label('Half-step update    •    Training MSE: 10 → 3.25',[0,-2.7,0],36)),run_time=.7);self.end()

class B04_Scene(Base):
 def construct(self):
  self.header('Slope And Curvature','Source: XGBoost model tutorial · conceptual curves')
  axes=[]
  for x,title in [(-3.35,'Gentler Curvature'),(3.35,'Steeper Curvature')]:
   ax=Axes(x_range=[-1,3,1],y_range=[0,5,1],x_length=5.1,y_length=3.0,axis_config={'color':LINE,'include_ticks':False,'include_tip':False}).move_to([x,-.15,0]);axes.append(ax)
   self.add(label(title,[x,2.1,0],35),label('Correction',[x,-2.45,0],28))
   self.play(Create(ax),run_time=.5)
  curves=[axes[0].plot(lambda x:.5*x*x-2*x+3,x_range=[-.7,3],color=INK,stroke_width=5),axes[1].plot(lambda x:2*x*x-2*x+3,x_range=[-.6,1.6],color=INK,stroke_width=5)]
  self.play(*[Create(c) for c in curves],run_time=1.2)
  self.cue('gradient',.29)
  tangents=VGroup(*[ax.plot(lambda x:3-2*x,x_range=[-.4,.8],color=ACC,stroke_width=5) for ax in axes]);self.play(Create(tangents),run_time=.8)
  self.play(FadeIn(label('Same Slope At Zero',[0,-2.05,0],27)),run_time=.5)
  self.cue('different step sizes',.65)
  for ax,x,y in [(axes[0],2,1),(axes[1],.5,2.5)]:
   self.play(FadeIn(Dot(ax.c2p(x,y),radius=.11,color=ACC)),Create(DashedLine(ax.c2p(x,0),ax.c2p(x,y),color=SOFT)),run_time=.6)
  self.play(FadeIn(label('Local Guide, Not Global Optimum',[0,-2.9,0],28)),run_time=.6);self.end()

class B05_Scene(Base):
 def construct(self):
  self.header('Control The Correction','Source: XGBoost parameters · same constructed example')
  self.add(label('Leaf Score Magnitude',[-3.25,2.0,0],34),label('Separate Controls',[3.4,1.9,0],37))
  baseline=Line([-5.8,-.75,0],[-.9,-.75,0],color=INK);self.add(baseline)
  bars=VGroup(*[Rectangle(width=1.25,height=1.8,stroke_width=0,fill_color=INK,fill_opacity=1).move_to([x,.15,0]) for x in [-4.55,-2.2]])
  nums=VGroup(label('−3',[-4.55,1.35,0],35),label('+3',[-2.2,1.35,0],35))
  self.play(FadeIn(bars),FadeIn(nums),run_time=.8)
  self.cue('shrinks',.15)
  small=VGroup(*[Rectangle(width=1.25,height=.9,stroke_width=0,fill_color=ACC,fill_opacity=1).move_to([x,-.3,0]) for x in [-4.55,-2.2]])
  newnums=VGroup(label('−1.5',[-4.55,.45,0],35),label('+1.5',[-2.2,.45,0],35))
  self.play(Transform(bars,small),Transform(nums,newnums),run_time=1)
  self.add(label('L2 penalty = 2',[-3.4,-1.2,0],34))
  self.cue('learning rate',.39)
  rate=box('Learning Rate × 0.5',[3.2,.65,0],4.8,1.1);self.play(FadeIn(rate),run_time=.6)
  self.play(FadeIn(label('−1.5 → −0.75     +1.5 → +0.75',[3.2,-.25,0],34)),run_time=.6)
  self.cue('A split penalty',.55)
  controls=VGroup(box('Split Penalty',[-3.8,-2.25,0],3.4),box('Depth Limit',[0,-2.25,0],3.4),box('Sampling',[3.8,-2.25,0],3.4))
  self.play(LaggedStart(*[FadeIn(c) for c in controls],lag_ratio=.6),run_time=1.8);self.end()

class B06_Scene(Base):
 def construct(self):
  self.header('Make Search Affordable','Sources: Chen & Guestrin; XGBoost tree methods')
  dots=VGroup(*[Dot([-5.4+i*.56,1.9,0],radius=.105,color=INK) for i in range(20)])
  self.play(FadeIn(dots),run_time=.8)
  self.cue('bins',.19)
  bins=VGroup(*[Rectangle(width=1.65,height=1.4,stroke_color=LINE,stroke_width=3).move_to([x,.3,0]) for x in [-4.8,-2.4,0,2.4,4.8]])
  self.play(Create(bins),run_time=.6)
  self.play(*[d.animate.move_to([[-4.8,-2.4,0,2.4,4.8][i//4]+(.2 if i%2 else -.2),.1+(.4 if i%4>1 else 0),0]) for i,d in enumerate(dots)],run_time=1.1)
  scan=Line([-3.6,1.15,0],[-3.6,-.55,0],color=ACC,stroke_width=7);self.play(Create(scan),run_time=.5);self.play(scan.animate.shift(RIGHT*2.4),run_time=.7);self.play(scan.animate.shift(RIGHT*2.4),run_time=.7)
  self.cue('Missing values',.43)
  missing=box('Missing',[-4.8,-1.25,0],2.0,.8);dest=box('Learned Branch',[-1.05,-1.25,0],3.0,.8)
  self.play(FadeIn(missing),FadeIn(dest),GrowArrow(arrow(missing.get_right(),dest.get_left())),run_time=.9)
  self.cue('The boosting rounds',.77)
  rounds=VGroup(*[box(s,[x,-2.45,0],3.3,.8) for s,x in [('Round 1',-4),('Round 2',0),('Round 3',4)]])
  self.play(FadeIn(rounds[0]),run_time=.4)
  for i in [1,2]:self.play(GrowArrow(arrow(rounds[i-1].get_right(),rounds[i].get_left())),FadeIn(rounds[i]),run_time=.6)
  self.end()

class B07_Scene(Base):
 def construct(self):
  self.header('Strong Is Not Universal','Constructed failure modes · not benchmark data')
  ax=Axes(x_range=[0,10,2],y_range=[0,5,1],x_length=5.2,y_length=3.5,axis_config={'color':LINE,'include_ticks':False,'include_tip':False}).move_to([-3.2,-.05,0])
  self.add(label('Error Over Rounds',[-3.2,2.1,0],37),label('Rounds',[-3.2,-2.2,0],29));self.play(Create(ax),run_time=.6)
  training=ax.plot(lambda x:3.6*np.exp(-x/3)+.3,x_range=[0,10],color=INK,stroke_width=5)
  validation=ax.plot(lambda x:.08*(x-4.7)**2+1.25,x_range=[0,10],color=ACC,stroke_width=5)
  self.play(Create(training),Create(validation),run_time=2)
  self.add(label('Training',[-4.65,-2.72,0],30),label('Validation',[-1.75,-2.72,0],30))
  self.add(Line([-5.95,-2.72,0],[-5.5,-2.72,0],color=INK,stroke_width=5),Line([-3.25,-2.72,0],[-2.8,-2.72,0],color=ACC,stroke_width=5))
  self.cue('Use validation',.40)
  self.play(Create(DashedLine(ax.c2p(4.7,0),ax.c2p(4.7,3.8),color=SOFT)),FadeIn(label('Stop Here',[-3.05,1.3,0],31)),run_time=.8)
  self.cue('Trees also',.61)
  right=Axes(x_range=[0,10,2],y_range=[0,5,1],x_length=5.1,y_length=3.5,axis_config={'color':LINE,'include_ticks':False,'include_tip':False}).move_to([3.4,-.05,0])
  self.play(Create(right),FadeIn(label('Beyond Training Range',[3.4,2.1,0],37)),run_time=.6)
  step=VMobject(color=INK,stroke_width=5).set_points_as_corners([right.c2p(x,y) for x,y in [(0,.5),(2,.5),(2,1.5),(4,1.5),(4,2.5),(6,2.5),(10,2.5)]])
  trend=DashedLine(right.c2p(6,3),right.c2p(10,5),color=ACC,stroke_width=4)
  self.play(Create(step),Create(trend),run_time=1)
  self.add(label('Tree prediction stays flat',[3.4,-2.2,0],29),label('Test On Untouched Data',[3.4,-2.72,0],32));self.end()
