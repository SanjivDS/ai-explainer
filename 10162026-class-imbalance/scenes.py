"""Native 4K teaching diagrams. Geometry keeps header, body and footer bands separate."""
from pathlib import Path
import json,re
import numpy as np
from manim import *
R=Path(__file__).parent
BS=json.loads((R/'beat_sheet.json').read_text());D=json.loads((R/'evidence/results.json').read_text())
BG='#FAF9F5';INK='#3D3929';ACC='#D97757';SOFT='#625E50';PALE='#C9C5B8'
FONT=R.resolve().parents[3]/'runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf'
H1=42;H2=30;BODY=28;VALUE=44

def txt(s,size=BODY,color=INK):
 with register_font(str(FONT)):return Text(s,font='EB Garamond',font_size=size,color=color)
def lab(s,x,y,size=BODY,color=INK):
 t=txt(s,size,color).move_to([x,y,0]);assert t.get_left()[0]>-6.4 and t.get_right()[0]<6.4, s
 return t

def fraction(num,den,x,y,size=36,width=1.65):
 # Structured numerator / bar / denominator layout, never an inline slash string.
 a=lab(str(num),x,y+.36,size);b=lab(str(den),x,y-.36,size)
 w=max(width,a.width+.22,b.width+.22)
 return VGroup(a,Line([x-w/2,y,0],[x+w/2,y,0],color=INK,stroke_width=3),b)
def box(s,x,y,w=3.4,h=.9,size=BODY):
 t=lab(s,x,y,size);assert t.width<w-.3,s
 return VGroup(RoundedRectangle(width=w,height=h,corner_radius=.1,color=PALE,stroke_width=2,fill_color=BG,fill_opacity=1).move_to(t),t)
def arr(a,b):return Arrow(a,b,buff=.12,color=INK,stroke_width=4,max_tip_length_to_length_ratio=.13)
class Base(Scene):
 def setup(self):
  self.camera.background_color=BG;self.bid=self.__class__.__name__[:3];self.beat=next(b for b in BS['beats'] if b['beat_id']==self.bid);self.dur=self.beat['actual_duration_s']
  self.add(lab('@sanjiv',5.3,-3.35,30,SOFT))
 def head(self,title,sub):self.add(lab(title,0,3.12,H1),lab(sub,0,2.45,H2))
 def until(self,f):
  if self.dur*f>self.renderer.time:self.wait(self.dur*f-self.renderer.time)
 def cue(self,s,f):
  w=json.loads((R/'mp3/words.json').read_text())['beats'].get(self.bid,[]);wanted=re.sub('[^a-z0-9 ]','',s.lower()).split()
  for k in range(len(w)-len(wanted)+1):
   if [re.sub('[^a-z0-9]','',q['text'].lower()) for q in w[k:k+len(wanted)]]==wanted:
    t=w[k]['startFrame']/24
    if t>self.renderer.time:self.wait(t-self.renderer.time)
    return
  self.until(f)
 def end(self):
  self.until(1)
  texts=[];seen=set()
  for root in self.mobjects:
   for m in root.get_family():
    if isinstance(m,Text) and id(m) not in seen:
     seen.add(id(m));texts.append(m)
  faults=[]
  for a in texts:
   if a.get_left()[0]<-6.4 or a.get_right()[0]>6.4 or a.get_top()[1]>3.6 or a.get_bottom()[1]<-3.6:faults.append('outside safe area: '+a.text)
  for i,a in enumerate(texts):
   for b in texts[i+1:]:
    ox=min(a.get_right()[0],b.get_right()[0])-max(a.get_left()[0],b.get_left()[0]);oy=min(a.get_top()[1],b.get_top()[1])-max(a.get_bottom()[1],b.get_bottom()[1])
    if ox>.025 and oy>.025:faults.append('text overlap: '+a.text+' / '+b.text)
  q=R/'_qc/layout';q.mkdir(parents=True,exist_ok=True)
  (q/f'{self.bid}.json').write_text(json.dumps({'type_scale':{'heading':H1,'subheading':H2,'body':BODY,'key_value':VALUE},'text_elements':len(texts),'faults':faults},indent=2))
  assert not faults, faults
class B01_Scene(Base):
 def construct(self):
  self.head('Look Beyond Accuracy','High accuracy can hide failure on rare cases.')
  for label,y,f in [('Which cases are missed?',1.0,.08),('How many false alarms?',-.15,.35),('What do those mistakes cost?',-1.3,.65)]:
   self.until(f);self.play(FadeIn(lab(label,0,y,34)),run_time=.6)
  self.end()
class B02_Scene(Base):
 def construct(self):
  self.head('The Majority-Class Trap','Constructed example • positive means fault')
  dots=VGroup(*[Dot([-5.4+(i%10)*.39,1.25-(i//10)*.34,0],radius=.10,color=INK) for i in range(100)])
  self.play(LaggedStart(*[FadeIn(d) for d in dots],lag_ratio=.008),run_time=1.3)
  self.add(lab('1 dot = 10 cases',-3.65,-2.35,30))
  self.cue('ten faults',.2);self.play(dots[-1].animate.set_color(ACC),FadeIn(lab('990 normal + 10 faults',2.7,1.1,30)),run_time=.7)
  rule=box('Always predict normal',2.7,.1,5.0,1,32)
  self.cue('always predicts normal',.4);self.play(FadeIn(rule),run_time=.7)
  self.cue('ninety-nine percent accuracy',.57);score=VGroup(lab('99%',2.7,-1.0,52),lab('accuracy',2.7,-1.65,30));self.play(FadeIn(score),run_time=.7)
  self.cue('zero of the ten faults',.72);self.play(FadeIn(lab('Faults found: 0 of 10',2.7,-2.6,32)),run_time=.8);self.end()
class B03_Scene(Base):
 def construct(self):
  self.head('Open the Confusion Matrix','Constructed scores • alert when score ≥ 0.5')
  self.add(lab('Predicted alert',-.55,1.65,30),lab('Predicted normal',3.5,1.65,30),lab('Actual fault',-4.7,.6,30),lab('Actual normal',-4.7,-1.15,30))
  m=D['thresholds']['0.5']
  def cell(n,note,x,y):
   border=RoundedRectangle(width=3.65,height=1.42,corner_radius=.08,color=PALE,stroke_width=2).move_to([x,y,0])
   return VGroup(border,lab(str(n),x,y+.22,44),lab(note,x,y-.36,28))
  cells=[cell(m['tp'],'TP · detected',-.55,.65),cell(m['fn'],'FN · missed',3.5,.65),cell(m['fp'],'FP · false alarm',-.55,-1.12),cell(m['tn'],'TN · correct normal',3.5,-1.12)]
  for phrase,f,c in zip(['eight real faults','misses two','twenty false alarms','seventy normal cases'],[.25,.35,.43,.55],cells):
   self.cue(phrase,f);self.play(FadeIn(c),run_time=.6)
  self.cue('Accuracy falls',.67);self.play(FadeIn(lab('978 correct out of 1,000 = 97.8%',0,-2.7,32)),run_time=.7);self.end()
class B04_Scene(Base):
 def construct(self):
  self.head('Recall and Precision','Constructed example • threshold 0.5')
  self.add(lab('Recall',-3.35,1.55,36),lab('Precision',3.35,1.55,36))
  left=VGroup(*[Dot([-4.6+i*.28,.7,0],radius=.09,color=INK,fill_opacity=1 if i<8 else 0,stroke_width=2) for i in range(10)])
  right=VGroup(*[Dot([2.45+(i%7)*.3,.9-(i//7)*.27,0],radius=.085,color=INK,fill_opacity=1 if i<8 else 0,stroke_width=2) for i in range(28)])
  self.play(FadeIn(left),run_time=.7)
  self.cue('Eight out of ten',.2);a=VGroup(fraction(8,10,-4.0,-.75),lab('= 80%',-1.9,-.75,36),lab('All actual faults',-3.35,-1.85,30));self.play(FadeIn(a),run_time=.8)
  self.cue('twenty-eight alerts',.41);self.play(FadeIn(right),run_time=.7)
  self.cue('Eight out of twenty-eight',.5);b=VGroup(fraction(8,28,2.5,-.75),lab('≈ 28.6%',4.8,-.75,36),lab('All alerts',3.35,-1.85,30));self.play(FadeIn(b),run_time=.8)
  self.cue('denominators differ',.73);self.play(FadeIn(lab('Filled dots = real faults caught',0,-2.75,28)),run_time=.7);self.end()
class B05_Scene(Base):
 def construct(self):
  self.head('Give Each Class a Voice','Balanced accuracy averages class recalls')
  # Two independent panels with a shared 0–100% visual scale.
  self.add(lab('Always normal',-3.3,1.6,34),lab('Scored rule',3.3,1.6,34))
  def bars(x,vals):
   g=VGroup()
   for y,label,v in zip([.65,-.55],['Fault','Normal'],vals):
    g.add(lab(label,x-1.9,y,30))
    g.add(Rectangle(width=2.55,height=.42,color=PALE,stroke_width=2).move_to([x+.3,y,0]))
    if v>0:g.add(Rectangle(width=2.55*v,height=.42,fill_color=INK,fill_opacity=1,stroke_width=0).move_to([x+.3-2.55*(1-v)/2,y,0]))
    g.add(lab(f'{100*v:.0f}%',x+.3,y-.46,30))
   return g
  headline=VGroup(lab('Accuracy: 99%',-3.3,-.3,36),lab('Accuracy: 97.8%',3.3,-.3,36))
  self.play(FadeIn(headline),run_time=.7);self.cue('Balanced accuracy instead',.17);self.play(FadeOut(headline),run_time=.5)
  self.cue('zero percent on faults',.28);self.play(FadeIn(bars(-3.3,[0,1])),run_time=.8)
  self.cue('fifty percent',.47);self.play(FadeIn(lab('Average: 50%',-3.3,-1.85,36)),run_time=.7)
  self.cue('eighty percent and about',.56);self.play(FadeIn(bars(3.3,[.8,D['thresholds']['0.5']['specificity']])),run_time=.8)
  self.cue('eighty-nine percent',.72);self.play(FadeIn(lab('Average: ≈ 89%',3.3,-1.85,36)),run_time=.7)
  self.cue('does not price',.88);self.play(FadeIn(lab('Equal class weighting does not price mistakes.',0,-2.8,28)),run_time=.6);self.end()
class B06_Scene(Base):
 def construct(self):
  self.head('Move the Threshold','Same scores. Different alert cutoffs.')
  line=Line([-5.6,1.4,0],[5.6,1.4,0],color=PALE,stroke_width=4);marker=Triangle(color=INK,fill_opacity=1).scale(.12).rotate(PI).move_to([3.36,1.65,0])
  self.add(line,lab('0',-5.6,.94,30),lab('1',5.6,.94,30));self.play(FadeIn(marker),run_time=.6)
  xs=[-5,-2.6,0,2.6,5];self.add(*[lab(s,x,.25,28) for s,x in zip(['Threshold','Caught','False alarms','Recall','Precision'],xs)])
  for t,y,phrase,f in [(.8,-.5,'zero point eight',.14),(.5,-1.35,'Lower it to',.34),(.2,-2.2,'Lower it again',.49)]:
   m=D['thresholds'][str(t)];values=[f'{t:.1f}',str(m['tp']),str(m['fp']),f"{100*m['recall']:.0f}%",f"{100*m['precision']:.1f}%"]
   row=VGroup(*[lab(s,x,y,32) for s,x in zip(values,xs)])
   self.cue(phrase,f);self.play(marker.animate.move_to([-5.6+11.2*t,1.65,0]),FadeIn(row),run_time=.8)
  self.end()
class B07_Scene(Base):
 def construct(self):
  self.head('Protect the Evaluation','Resample training only.')
  train=box('Training fold',-3.4,1.15,4.2,.95,34);val=box('Validation fold',3.4,1.15,4.2,.95,34)
  self.play(FadeIn(train),FadeIn(val),run_time=.8)
  weights=box('Class weights',-3.4,-.1,4.2,.8,28);sample=box('Resampling',-3.4,-1.15,4.2,.8,28)
  self.cue('Class weights',.21);self.play(FadeIn(weights),run_time=.65)
  self.cue('Resampling changes',.31);self.play(FadeIn(sample),run_time=.65)
  self.cue('only inside the training',.43);bound=RoundedRectangle(width=4.55,height=3.5,corner_radius=.1,color=INK,stroke_width=3).move_to([-3.4,0,0]);self.play(Create(bound),run_time=.7)
  self.cue('representative of deployment',.65);v=VGroup(lab('Original class mix',3.4,-.1,32),lab('Tune the threshold here',3.4,-.8,30));self.play(FadeIn(v),run_time=.7)
  self.cue('Balancing the test set',.73);test=box('Final test: untouched',3.4,-1.8,4.2,.8,28);self.play(FadeIn(test),run_time=.7)
  self.end()
class B08_Scene(Base):
 def construct(self):
  self.head('Counts Matter','Constructed comparison • one changed outcome')
  self.add(lab('10 actual faults',-3.3,1.65,32),lab('100 actual faults',3.3,1.65,32))
  def sample(x,n,hit):
   cols=10;dx=.34 if n==100 else .34
   return VGroup(*[Dot([x+(i%cols-4.5)*dx,1.0-(i//cols)*.26,0],radius=.075,color=INK,fill_opacity=1 if i<hit else 0,stroke_width=2) for i in range(n)])
  a=sample(-3.3,10,8);b=sample(3.3,100,80)
  self.cue('Eight detected faults',.12);self.play(FadeIn(a),run_time=.7)
  self.cue('eighty out of one hundred',.25);self.play(FadeIn(b),run_time=.7)
  la=lab('8 of 10 = 80%',-3.3,-1.8,36);lb=lab('80 of 100 = 80%',3.3,-1.8,36);self.play(FadeIn(la),FadeIn(lb),run_time=.7)
  self.cue('change one hit to a miss',.4);self.play(a[7].animate.set_fill(opacity=0),b[79].animate.set_fill(opacity=0),run_time=.8)
  self.play(FadeOut(la),FadeOut(lb),run_time=.25);self.play(FadeIn(lab('7 of 10 = 70%',-3.3,-1.8,36)),FadeIn(lab('79 of 100 = 79%',3.3,-1.8,36)),run_time=.45)
  self.cue('ten percentage points',.5);self.play(FadeIn(lab('−10 percentage points',-3.3,-2.65,28)),FadeIn(lab('−1 percentage point',3.3,-2.65,28)),run_time=.7);self.end()
