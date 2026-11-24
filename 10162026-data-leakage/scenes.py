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
def arr(a,b):return Arrow(a,b,buff=.035,color=INK,stroke_width=3,max_tip_length_to_length_ratio=.35)
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
  self.head('An Unfair Preview','A useful test must match the real task.')
  for phrase,label,y,f in [('available','Available at prediction time?',1.05,.2),('held-out','Learned from training only?',-.15,.4),('connected','Independent enough for the task?',-1.35,.6)]:
   self.cue(phrase,f);self.play(FadeIn(lab(label,0,y,34)),run_time=.6)
  self.end()
class B02_Scene(Base):
 def construct(self):
  self.head('Respect Prediction Time','Illustration • escalation predicted when a ticket arrives')
  self.add(Line([-5.5,.1,0],[5.5,.1,0],color=PALE,stroke_width=3))
  for x,label in [(-3.5,'Ticket arrives'),(3.5,'Ticket closes')]:self.add(Dot([x,.1,0],radius=.08,color=INK),lab(label,x,-.5,30))
  boundary=DashedLine([-1.1,-1.4,0],[-1.1,1.75,0],color=INK,stroke_width=2)
  self.play(Create(boundary),run_time=.7)
  start=box('Opening message',-3.6,1.15,3.8,.8,30);later=box('Resolution code',3.5,1.15,3.8,.8,30)
  self.cue('opening message',.18);self.play(FadeIn(start),run_time=.6)
  self.cue('resolution code',.3);self.play(FadeIn(later),run_time=.6)
  model=box('Predict escalation',-3.6,-1.65,3.8,.8,30)
  self.play(FadeIn(model),Create(arr([-3.6,-.82,0],[-3.6,-1.18,0])),run_time=.6)
  self.cue('later field',.45)
  leak=Arrow([3.5,-.85,0],[-1.5,-1.65,0],color=INK,buff=.12,stroke_width=4)
  self.play(Create(leak),run_time=.7);self.add(lab('Not available yet',2.7,-1.7,30,INK))
  self.cue('random train-test split',.6);self.play(FadeIn(lab('A row split cannot fix a future-only feature.',0,-2.75,28)),run_time=.6);self.end()
class B03_Scene(Base):
 def construct(self):
  self.head('Separate the Right Units','Illustration • the goal is prediction for new customers')
  self.add(lab('Training',-3.2,1.55,34),lab('Evaluation',3.2,1.55,34),DashedLine([0,-2.2,0],[0,1.9,0],color=PALE))
  left=VGroup(box('Customer A · ticket 1',-3.2,.6,4.5,.85,28),box('Customer B · ticket 1',-3.2,-.65,4.5,.85,28))
  right=VGroup(box('Customer A · ticket 2',3.2,.6,4.5,.85,28),box('Customer C · ticket 1',3.2,-.65,4.5,.85,28))
  self.play(FadeIn(left),FadeIn(right),run_time=.7)
  self.cue('same customer',.25);self.play(Create(Line([-1,.6,0],[1,.6,0],color=INK,stroke_width=4)),run_time=.6)
  notice=lab('Customer A crosses the boundary',0,-2.25,30,INK);self.play(FadeIn(notice),run_time=.5)
  self.cue('Keep each customer together',.53)
  self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.4)
  self.add(lab('@sanjiv',5.3,-3.35,30,SOFT));self.head('Split by Customer','New customers stay unseen during training.')
  self.add(lab('Training',-3.2,1.55,34),lab('Evaluation',3.2,1.55,34),DashedLine([0,-1.7,0],[0,1.9,0],color=PALE))
  self.play(FadeIn(box('All tickets: A and B',-3.2,.3,4.5,1.25,30)),FadeIn(box('All tickets: C',3.2,.3,4.5,1.25,30)),run_time=.7)
  self.cue('respect time',.78);self.play(FadeIn(lab('Future task? Also preserve time order.',0,-1.6,28)),run_time=.7);self.end()
class B04_Scene(Base):
 def construct(self):
  self.head('Build a Noise-Only Task','Seed 42 • synthetic data • no planted signal')
  dots=VGroup(*[Dot([-5.1+(i%6)*.38,1.1-(i//6)*.38,0],radius=.1,color=INK) for i in range(30)])
  self.play(FadeIn(dots),run_time=.7);self.add(lab('300 rows',-4.15,-1.35,34),lab('1 dot = 10 rows',-4.15,-1.95,28))
  self.cue('ten thousand',.12);self.play(FadeIn(lab('10,000 random features',2.2,1.1,34)),run_time=.6)
  self.cue('independent random',.2);self.play(FadeIn(lab('Independent labels: 0 or 1',2.2,.2,30)),run_time=.6)
  self.cue('Reserve',.4);self.play(*[d.animate.set_color(ACC) for d in dots[18:]],run_time=.6)
  self.play(FadeIn(lab('Train: 180    Evaluate: 120',2.2,-.8,30)),run_time=.6)
  self.cue('twenty-five features',.72);self.play(FadeIn(lab('Select only 25 features',2.2,-1.85,34)),run_time=.6);self.end()
class B05_Scene(Base):
 def construct(self):
  self.head('The Leak Happens Before Fitting','Feature selection sees the held-out answers.')
  train=box('180 training rows + labels',-3.3,1.2,5,.9,28);test=box('120 evaluation rows + labels',3.3,1.2,5,.9,28)
  select=box('Choose 25 correlated features',0,-.15,6.5,.9,30)
  self.play(FadeIn(train),FadeIn(test),run_time=.7)
  self.cue('across all',.22);self.play(FadeIn(select),Create(arr([-3.3,.65,0],[-1.5,.38,0])),Create(Arrow([3.3,.65,0],[1.5,.38,0],buff=.06,color=INK,stroke_width=4)),run_time=.7)
  model=box('Fit classifier on training rows only',0,-1.75,7,.9,30)
  self.cue('train a simple',.31);self.play(FadeIn(model),Create(arr([0,-.65,0],[0,-1.25,0])),run_time=.7)
  self.cue('already helped',.55);self.play(FadeIn(lab('Training-only fitting is too late to undo the leak.',0,-2.75,28)),run_time=.6);self.end()
class B06_Scene(Base):
 def construct(self):
  self.head('A Better Score, a Broken Test','Recorded synthetic run • same split and classifier')
  x0=-1.5;w=6
  self.add(lab('Evaluation accuracy',1.5,1.6,32))
  self.add(Line([x0,-1.95,0],[x0+w,-1.95,0],color=PALE))
  for v in [0,.5,1]:self.add(lab(f'{100*v:.0f}%',x0+w*v,-2.3,28))
  self.add(DashedLine([1.5,-1.8,0],[1.5,1.15,0],color=PALE,stroke_width=2))
  for key,label,y,phrase,f,color in [('leaky','Select before split',.75,'ninety-five correct',.1,INK),('clean','Select on training',-.65,'sixty-two correct',.45,INK)]:
   result=D[key];v=result['accuracy'];self.cue(phrase,f)
   g=VGroup(lab(label,-4.0,y+.15,30),lab(f"{result['correct']} of {result['total']}",-4.0,y-.38,28),Rectangle(width=w*v,height=.46,stroke_width=0,fill_color=color,fill_opacity=1).move_to([x0+w*v/2,y,0]),lab(f'{100*v:.1f}%',5.3,y,34))
   self.play(FadeIn(g),run_time=.8)
  self.cue('not universal',.75);self.play(FadeIn(lab('One run • chance expectation ≈ 50%',0,-2.85,28)),run_time=.6);self.end()
class B07_Scene(Base):
 def construct(self):
  self.head('Fit Inside the Boundary','Repeat the whole pipeline within each training fold.')
  self.add(lab('Training fold',-3.3,1.65,34),lab('Held-out fold',3.3,1.65,34),DashedLine([0,-2.2,0],[0,1.95,0],color=PALE,stroke_width=2))
  a=box('Learn preprocessing',-3.3,.65,4.5,.9,30);b=box('Fit model',-3.3,-.85,4.5,.9,30)
  self.cue('Learn imputation',.14);self.play(FadeIn(a),run_time=.6)
  self.play(FadeIn(b),Create(arr([-3.3,.1,0],[-3.3,-.3,0])),run_time=.6)
  c=box('Apply fixed transform',3.3,.65,4.5,.9,30);d=box('Predict and score',3.3,-.85,4.5,.9,30)
  self.cue('Apply those fixed',.32);self.play(FadeIn(c),Create(arr([-1,.65,0],[1,.65,0])),run_time=.6)
  self.play(FadeIn(d),Create(arr([3.3,.1,0],[3.3,-.3,0])),run_time=.6)
  self.cue('without fitting again',.42);self.play(FadeIn(lab('No refitting on held-out data',3.3,-1.85,28)),run_time=.6)
  self.cue('cannot recognize',.76);self.play(FadeIn(lab('A pipeline cannot fix a future-only feature.',0,-2.75,28)),run_time=.6);self.end()
class B08_Scene(Base):
 def construct(self):
  self.head('A Score Is Not a Diagnosis','Distinguish overfitting from evaluation contamination.')
  self.add(lab('Overfitting',-3.3,1.5,36),lab('Leakage',3.3,1.5,36))
  self.cue('memorizes training noise',.18);self.play(FadeIn(box('Memorizes training noise',-3.3,.45,5,.95,30)),run_time=.6)
  self.play(FadeIn(lab('Clean test can expose it',-3.3,-.55,28)),run_time=.6)
  self.cue('compromises',.38);self.play(FadeIn(box('Evaluation information leaks',3.3,.45,5,.95,28)),run_time=.6)
  self.play(FadeIn(lab('The test is compromised',3.3,-.55,28)),run_time=.6)
  self.cue('Shuffling labels',.49);self.play(FadeIn(lab('Shuffle labels → rerun the entire workflow',0,-1.65,30)),run_time=.6)
  self.cue('does not certify',.7);self.play(FadeIn(lab('A diagnostic check, not a certificate.',0,-2.65,28)),run_time=.6);self.end()
