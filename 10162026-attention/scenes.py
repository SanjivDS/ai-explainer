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

class B02_Scene(Base):
    def construct(self):
        self.title('One Summary Is a Bottleneck')
        states=VGroup(*[box(f'Source {i+1}',2.2,.8,34) for i in range(4)]).arrange(RIGHT,buff=.65).move_to([0,1.5,0])
        summary=box('One summary',3.3,.85,38).move_to([0,-.2,0]);decoder=box('Decoder',3.3,.85,38).move_to([0,-2,0])
        links=VGroup(*[arrow(s.get_bottom(),summary.get_top()) for s in states]);down=arrow(summary.get_bottom(),decoder.get_top())
        self.reveal(states);self.cue('compresses');self.reveal(summary,links);self.cue('decoder generates');self.reveal(decoder,down)
        self.cue('lets the decoder consult');self.change([summary,links,down],text('Source states remain accessible',40).move_to([0,-.25,0]))
        self.finish()

class B03_Scene(Base):
    def construct(self):
        self.title('Context Can Change Each Step')
        sources=VGroup(*[box(f'Source {i+1}',2.5,.85,36) for i in range(3)]).arrange(RIGHT,buff=1.1).move_to([0,1.4,0]);self.reveal(sources)
        self.note('Illustrative weights · not a measured alignment',-3.05)
        def state(label,weights):
            q=box(label,3.2,.9,36).move_to([0,-1.6,0]);g=VGroup(q)
            for src,w in zip(sources,weights):
                edge=arrow(src.get_bottom(),q.get_top(),ACC if w==max(weights) else MUTED);edge.set_stroke(width=2+5*w)
                lab=text(f'{w:.1f}',34).move_to([src.get_x()+.55,.35,0]);g.add(edge,lab)
            return g
        a=state('Decoder step 1',[.6,.3,.1]);self.cue('a new set of weights');self.reveal(a)
        self.cue('another step');b=state('Decoder step 2',[.1,.2,.7]);self.change([a],b);self.finish()

class B04_Scene(Base):
    def construct(self):
        self.title('Query, Key, Value')
        q=box('Query',2.8,1,42).move_to([-4.1,1,0]);k=box('Keys',2.8,1,42).move_to([0,1,0]);scores=box('Scores',2.8,1,42).move_to([4.1,1,0])
        self.cue('A query');self.reveal(q,k,arrow(q.get_right(),k.get_left()),scores,arrow(k.get_right(),scores.get_left()))
        vals=box('Values',2.8,1,42).move_to([-4.1,-1.1,0]);mix=box('Weighted mix',4.2,1,40).move_to([1,-1.1,0]);self.cue('Values supply');self.reveal(vals,mix,arrow(vals.get_right(),mix.get_left()),arrow(scores.get_bottom(),mix.get_top()))
        self.cue('In self-attention');self.change([q,k,scores,vals,mix,*[m for m in list(self.mobjects) if isinstance(m,Arrow)]],text('Same sequence → learned projections → Q, K, V',40).move_to([0,.7,0]))
        self.note('Three numeric roles',-1.1);self.finish()

class B05_Scene(Base):
    def construct(self):
        self.title('Compute the Scores')
        self.reveal(text('q = (1, 0)       key dimension = 2',40).move_to([0,1.9,0]))
        keys=VGroup(*[box(s,3,.85,36) for s in ['k₁ = (2, 0)','k₂ = (0, 2)','k₃ = (0, 0)']]).arrange(RIGHT,buff=.7).move_to([0,.6,0]);self.reveal(keys)
        self.cue('Its dot products');dots=mathsvg(r'qK^{\mathsf{T}}=[2,\ 0,\ 0]',5.3).move_to([0,-.8,0]);self.reveal(dots)
        self.cue('Divide by');scaled=mathsvg(r'\frac{qK^{\mathsf{T}}}{\sqrt{d_k}}=[\sqrt{2},\ 0,\ 0]\approx[1.414,\ 0,\ 0]',9.3).move_to([0,-2.1,0]);self.reveal(scaled)
        self.finish()

class B06_Scene(Base):
    def construct(self):
        self.title('Scores Become Weights')
        eq=mathsvg(r'\alpha_i=\frac{\exp(s_i)}{\sum_j\exp(s_j)}',4.8).move_to([0,1.5,0]);self.reveal(eq)
        weights=DATA['examples'][0]['weights'];bars=VGroup()
        for i,w in enumerate(weights):
            x=-3.6+i*3.6;h=w*3
            bar=Rectangle(width=1.7,height=h,fill_color=ACC if i==0 else MUTED,fill_opacity=1,stroke_width=0).move_to([x,-1.65+h/2,0]);bars.add(bar,text(f'{w:.3f}',36).next_to(bar,UP,buff=.18),text(f'Source {i+1}',32).move_to([x,-2.05,0]))
        self.cue('Our first source');self.reveal(bars)
        self.cue('The unrounded weights');self.note('Unrounded sum = 1 · displayed values rounded',-2.9)
        self.finish()

class B07_Scene(Base):
    def construct(self):
        self.title('Mix the Values')
        vals=text('v₁ = (1, 0)     v₂ = (0, 1)     v₃ = (1, 1)',40).move_to([0,1.65,0]);self.reveal(vals)
        eq=mathsvg(r'z=\alpha_1v_1+\alpha_2v_2+\alpha_3v_3',8).move_to([0,.2,0]);self.reveal(eq)
        self.cue('gives approximately');out=mathsvg(r'q=(1,0)\quad\Rightarrow\quad z\approx(0.836,\ 0.327)',10).move_to([0,-1.4,0]);self.reveal(out)
        self.cue('Change only the query');new=mathsvg(r'q=(0,1)\quad\Rightarrow\quad z\approx(0.327,\ 0.836)',10).move_to([0,-1.4,0]);self.change([out],new)
        self.cue('Same keys and values');self.note('Constructed vectors · changed query, changed mixture',-2.8);self.finish()

class B08_Scene(Base):
    def construct(self):
        self.title('Self-Attention and Cross-Attention')
        def panel(x,cross):
            head=text('Cross-attention' if cross else 'Self-attention',42).move_to([x,1.9,0]);g=VGroup(head)
            if cross:
                a=box('Decoder → Q',4.7,.9,36).move_to([x,.7,0]);b=box('Encoder → K, V',4.7,.9,36).move_to([x,-.5,0]);g.add(a,b)
            else:
                a=box('One sequence',4.7,.9,36).move_to([x,.7,0]);b=box('Q, K, V',4.7,.9,36).move_to([x,-.5,0]);g.add(a,b,arrow(a.get_bottom(),b.get_top()))
            g.add(text('Score → weight → mix',34).move_to([x,-1.9,0]));return g
        self.cue('Self-attention relates');self.reveal(panel(-3.4,False));self.cue('Cross-attention takes');self.reveal(panel(3.4,True));self.finish()

class B09_Scene(Base):
    def construct(self):
        self.title('Why the Transformer Mattered')
        year=text('Transformer · 2017',36).move_to([0,2.1,0]);self.reveal(year)
        nodes=VGroup(*[box(str(i+1),1.1,.8,36) for i in range(5)]).arrange(RIGHT,buff=1.1).move_to([0,.7,0]);links=VGroup(*[arrow(nodes[i].get_right(),nodes[i+1].get_left()) for i in range(4)]);lbl=text('Recurrent sequence of states',36).move_to([0,-.35,0]);self.reveal(nodes,links,lbl)
        self.cue('Allowed positions');direct=CurvedArrow(nodes[0].get_bottom(),nodes[4].get_bottom(),angle=TAU/5,color=ACC,stroke_width=4);newlbl=text('Direct interaction between allowed positions',36).move_to([0,-2.3,0]);self.change([links,lbl],direct,newlbl)
        self.cue('training could compute');train=VGroup(text('Training',42),text('Many positions in parallel',36)).arrange(DOWN,buff=.5).move_to([-3.3,0,0]);gen=VGroup(text('Generation',42),text('Next token after previous tokens',34)).arrange(DOWN,buff=.5).move_to([3.3,0,0]);self.change([nodes,direct,newlbl],train)
        self.cue('Autoregressive generation');self.reveal(gen);self.finish()

class B10_Scene(Base):
    def construct(self):
        self.title('Structure Still Matters')
        order=VGroup(*[box(s,2.8,1,38) for s in ['1 · cat','2 · sees','3 · dog']]).arrange(RIGHT,buff=.8).move_to([0,.6,0]);label=text('Position information represents order',38).move_to([0,-1,0]);self.reveal(order,label)
        self.cue('A causal mask');grid=VGroup()
        for i in range(4):
            for j in range(4):grid.add(Square(.6,stroke_color=PALE,stroke_width=2,fill_color=MUTED if j<=i else WHITE,fill_opacity=1).move_to([-1.1+j*.7,1.25-i*.7,0]))
        masklabel=text('Causal mask · future positions blocked',38).move_to([0,-1.7,0]);self.change([order,label],grid,masklabel)
        self.cue('Multiple heads');heads=VGroup(box('Head 1',3.3).move_to([-3,1,0]),box('Head 2',3.3).move_to([3,1,0]));out=box('Concatenate → project',6,.95,38).move_to([0,-.9,0]);edges=VGroup(*[arrow(h.get_bottom(),out.get_top()) for h in heads]);self.change([grid,masklabel],heads,out,edges)
        self.cue('Feed-forward layers');self.note('Also: feed-forward layers and residual connections',-2.7);self.finish()

class B11_Scene(Base):
    def construct(self):
        self.title('Power Has Limits')
        def grid(n,x,size):
            g=VGroup(*[Square(size,stroke_color=PALE,stroke_width=2,fill_color=MUTED,fill_opacity=.7) for _ in range(n*n)]).arrange_in_grid(rows=n,cols=n,buff=.07).move_to([x,.4,0]);return g
        a=grid(4,-3.1,.5);b=grid(8,3.1,.23);labels=VGroup(text('4 positions · 16 pairs',36).move_to([-3.1,-1.6,0]),text('8 positions · 64 pairs',36).move_to([3.1,-1.6,0]));self.reveal(a,b,labels)
        self.cue('And a bright cell');heat=VGroup()
        for i in range(4):
            for j in range(4):heat.add(Square(.65,stroke_color=PALE,stroke_width=2,fill_color=ACC if (i,j)==(2,1) else MUTED,fill_opacity=1 if (i,j)==(2,1) else .45).move_to([-4.2+j*.75,1.3-i*.75,0]))
        caution=VGroup(text('A map suggests a question.',38),text('Test the model to explain it.',38)).arrange(DOWN,buff=.55).move_to([2.1,.2,0]);self.change([a,b,labels],heat,caution)
        self.note('Illustrative map · no trained-model measurements',-2.8);self.finish()
