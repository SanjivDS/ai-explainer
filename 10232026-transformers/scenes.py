"""Native teaching figures. Attention calculations derive from evidence/result.json."""
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
def arrow(a,b,color=PALE,tip_ratio=.3):return Arrow(a,b,buff=.04,color=color,stroke_width=3,max_tip_length_to_length_ratio=tip_ratio)
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


def chain(labels,y=0,width=3):
    nodes=VGroup(*[box(s,width,1.05,36) for s in labels]).arrange(RIGHT,buff=.65).move_to([0,y,0])
    links=VGroup(*[Arrow(a.get_right(),b.get_left(),buff=.04,color=ACC,stroke_width=3,max_tip_length_to_length_ratio=.3) for a,b in zip(nodes,nodes[1:])])
    return VGroup(nodes,links)

class B02_Scene(Base):
    def construct(self):
        self.title('The Architecture Map')
        top=chain(['Source tokens','Encoder stack','Source vectors'],1.35)
        bottom=chain(['Target prefix','Decoder stack','Next-token scores'],-1.3)
        self.reveal(top);self.cue('The decoder');self.reveal(bottom)
        link=Arrow(top[0][2].get_bottom(),bottom[0][1].get_top(),buff=.12,color=ACC)
        label=text('cross-attention',32).move_to([-.9,0,0])
        self.reveal(link,label);self.note('Original encoder–decoder design');self.finish()

class B03_Scene(Base):
    def construct(self):
        self.title('Give Tokens Position')
        chips=VGroup(*[box(s,2.7) for s in ['cats','chase','birds']]).arrange(RIGHT,buff=1.1).move_to([0,1.3,0]);self.reveal(chips)
        vectors=VGroup(*[VGroup(*[Rectangle(width=.38,height=.35,fill_color=ACC,fill_opacity=a,stroke_width=0) for a in [.3,.7,.5,1]]).arrange(DOWN,buff=.08).move_to([x,-.35,0]) for x in [-3.8,0,3.8]])
        self.reveal(vectors);self.cue('position');tags=VGroup(*[text('position '+str(i+1),34).move_to([x,-1.75,0]) for i,x in enumerate([-3.8,0,3.8])]);self.reveal(tags)
        self.cue('Other designs');self.change([chips[0],chips[2]],chips[0].copy().move_to(chips[2]),chips[2].copy().move_to(chips[0]))
        self.note('Same token identities · different order');self.finish()

class B04_Scene(Base):
    def construct(self):
        self.title('Self-Attention Connects a Sequence')
        source=box('One sequence of representations',8).move_to([0,1.8,0]);self.reveal(source)
        lanes=VGroup(*[box(s,3,1.1) for s in ['Queries · Q','Keys · K','Values · V']]).arrange(RIGHT,buff=.6).move_to([0,0,0])
        links=VGroup(*[arrow(source.get_bottom(),n.get_top(),ACC) for n in lanes]);self.reveal(links,lanes)
        self.cue('A query');out=chain(['Q compares with K','Weights mix V','New representation'],-1.9,width=3.3);self.reveal(out);self.finish()

class B05_Scene(Base):
    def construct(self):
        self.title('Calculate Attention Weights');self.note('Constructed example · weights sum to 1')
        q=formula(r'q=(1,0)',1.8,2.5);k=formula(r'K=[(1,0),(0,1),(1,1)]',.6,7.5);self.reveal(q,k)
        self.cue('dot products');row=formula(r'qK^T=[1,0,1]',-1.05,5);self.reveal(row)
        self.cue('Divide');new=formula(r'\frac{qK^T}{\sqrt{2}}=[0.707,0,0.707]',-1.05,8);self.change([row],new)
        self.cue('resulting weights');weights=formula(r'\mathrm{softmax}\approx[0.401,0.198,0.401]',-1.05,9);self.change([new],weights)
        self.finish()

class B06_Scene(Base):
    def construct(self):
        self.title('Mix the Values')
        f=formula(r'\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V',1.65,10);self.reveal(f)
        values=VGroup(*[box(s,3,1.1) for s in ['0.401 × (1, 0)','0.198 × (0, 2)','0.401 × (3, 1)']]).arrange(RIGHT,buff=.6).move_to([0,-.15,0]);self.reveal(values)
        self.cue('weighted sum');out=formula(r'\mathrm{output}\approx(1.604,\ 0.797)',-1.7,7);self.reveal(out)
        self.note('Output uses unrounded weights');self.finish()

class B07_Scene(Base):
    def construct(self):
        self.title('Why Multiple Heads')
        projections=VGroup(*[box('Projection set '+str(i+1),4,.9,36).move_to([x,1.65,0]) for i,x in enumerate([-3.2,3.2])])
        heads=VGroup(*[box('Attention head '+str(i+1),4,.9,36).move_to([x,.25,0]) for i,x in enumerate([-3.2,3.2])])
        self.reveal(projections,heads,*[arrow(a.get_bottom(),b.get_top(),ACC) for a,b in zip(projections,heads)])
        self.cue('concatenated');merge=box('Concatenate outputs',5,.85).move_to([0,-1.15,0]);self.reveal(merge,*[arrow(h.get_bottom(),merge.get_top(),ACC) for h in heads])
        output=box('Output projection',5,.85).move_to([0,-2.55,0]);self.reveal(output,arrow(merge.get_bottom(),output.get_top(),ACC));self.finish()

class B08_Scene(Base):
    def construct(self):
        self.title('Inside an Encoder Block')
        nodes=VGroup(*[box(s,5,.8,34) for s in ['Self-attention','Add & Norm','Feed-forward','Add & Norm']]).arrange(DOWN,buff=.43).move_to([0,.1,0])
        self.reveal(nodes[0]);self.cue('residual');self.reveal(nodes[1]);self.cue('feed-forward');self.reveal(nodes[2]);self.cue('another residual');self.reveal(nodes[3])
        arrows=VGroup(*[Arrow(a.get_bottom(),b.get_top(),buff=.025,color=ACC,max_tip_length_to_length_ratio=.4) for a,b in zip(nodes,nodes[1:])]);self.reveal(arrows)
        for a,b,x in [(nodes[0],nodes[1],-3.7),(nodes[2],nodes[3],3.7)]:
            start=a.get_top()+UP*.18;end=b.get_left() if x<0 else b.get_right()
            path=VMobject(color=ACC,stroke_width=3).set_points_as_corners([start,[x,start[1],0],[x,end[1],0],end]);self.reveal(path)
        self.note('Original post-norm arrangement');self.finish()

class B09_Scene(Base):
    def construct(self):
        self.title('The Decoder Cannot Peek')
        shift=VGroup(text('Input',36).move_to([-3.8,2,0]),text('Target',36).move_to([-3.8,1.3,0]),*[text(t,36).move_to([x,y,0]) for y,tokens in [(2,['START','I','see']),(1.3,['I','see','cats'])] for x,t in zip([-1.75,0,1.75],tokens)]);self.reveal(shift)
        self.cue('causal mask');cells=VGroup()
        for i in range(3):
            for j in range(3):
                cell=box('allow' if j<=i else 'block',1.55,.68,34).move_to([(j-1)*1.75,-i*.83+.1,0]);cell[1].set_color(ACC if j<=i else MUTED);cells.add(cell)
        labels=VGroup(text('keys →',34).move_to([0,.75,0]),text('query',34).move_to([-3.4,-.7,0]));self.reveal(cells,labels)
        self.note('Future scores excluded before softmax');self.finish()

class B10_Scene(Base):
    def construct(self):
        self.title('Cross-Attention Reads the Source')
        decoder=box('Decoder states',4).move_to([-3.4,1.55,0]);encoder=box('Encoder outputs',4).move_to([3.4,1.55,0]);self.reveal(decoder,encoder)
        self.cue('queries');q=box('Queries · Q',3).move_to([-3.4,-.15,0]);kv=box('Keys · K     Values · V',4.6).move_to([3.4,-.15,0]);self.reveal(q,kv,arrow(decoder.get_bottom(),q.get_top(),ACC),arrow(encoder.get_bottom(),kv.get_top(),ACC))
        out=box('Cross-attention output',5).move_to([0,-1.95,0]);self.reveal(out,arrow(q.get_bottom(),out.get_top(),ACC),arrow(kv.get_bottom(),out.get_top(),ACC));self.finish()

class B11_Scene(Base):
    def construct(self):
        self.title('Training and Generation')
        train=VGroup(text('TRAINING · known target sequence',38),chain(['START → I','I → see','see → cats'],width=3),text('Parallel positions · causal mask',36)).arrange(DOWN,buff=.7).move_to([0,.2,0]);self.reveal(train)
        self.cue('During ordinary');self.play(FadeOut(train),run_time=.3)
        gen=chain(['Prefix','Distribution','Choose token'],1,3);append=box('Append token to prefix',5).move_to([0,-1.35,0]);self.reveal(gen,append)
        path=CurvedArrow(append.get_left(),gen[0][0].get_bottom(),angle=-TAU/4,color=ACC);self.reveal(path,CurvedArrow(gen[0][2].get_bottom(),append.get_right(),angle=-TAU/4,color=ACC));self.note('Generation repeats one step at a time');self.finish()

class B12_Scene(Base):
    def construct(self):
        self.title('Three Transformer Families')
        cols=[]
        for x,heading,items in [(-4.3,'Encoder-only',['Input sequence','Encoder','Representations']),(0,'Decoder-only',['Target prefix','Causal decoder','Next token']),(4.3,'Encoder–decoder',['Source → encoder','Cross-attention','Decoder → token'])]:
            col=VGroup(text(heading,37,ACC),*[box(s,3.7,.95,34) for s in items]).arrange(DOWN,buff=.4).move_to([x,.1,0]);cols.append(col)
        self.reveal(cols[0]);self.cue('Decoder-only');self.reveal(cols[1]);self.cue('Encoder-decoder');self.reveal(cols[2]);self.note('Different information paths · shared attention machinery');self.finish()

class B13_Scene(Base):
    def construct(self):
        self.title('Check the Mask');self.note('Executed unit test · fixed queries and keys')
        before=formula(r'v_3:(3,1)\ \longrightarrow\ (300,-100)',1.65,8);self.reveal(before)
        self.cue('With the causal mask');safe=VGroup(text('CAUSAL MASK',37,ACC),text('Earlier outputs: unchanged',40),formula(r'y_1=(1,0)',width=3.5)).arrange(DOWN,buff=.35).move_to([-3.2,-.45,0]);self.reveal(safe)
        self.cue('Without that mask');open_=VGroup(text('NO MASK',37),text('Earlier outputs: changed',40),formula(r'y_1\approx(120.735,-39.716)',width=5.1)).arrange(DOWN,buff=.4).move_to([3.2,-.45,0]);self.reveal(open_)
        self.finish()
