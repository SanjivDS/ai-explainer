"""Tokenization diagrams using the older Claude template typography and branding."""
import json
from pathlib import Path
from manim import *
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SHEET=json.loads((HERE/'beat_sheet.json').read_text())
WORDS=json.loads((HERE/'mp3/words.json').read_text()) if (HERE/'mp3/words.json').exists() else {'beats':{}}
BG='#FAF9F5'; INK='#3D3929'; ACC='#D97757'; PALE='#DAD5C9'; MUTED='#625E52'; WHITE='#FFFDF9'
FONT='EB Garamond'

def text(s,size=30,color=INK):
    with register_font(ROOT/'runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf'):
        return Text(s,font=FONT,font_size=max(size * 1.25,36),color=color,disable_ligatures=False)

def label(s,y=3.0,size=44.8): return text(s,size).move_to([0,y,0])
def tiles(items,y=0,width=1.4):
    result=VGroup()
    for s in items:
        box=RoundedRectangle(width=width,height=1.03,corner_radius=.10,stroke_color=PALE,stroke_width=2,fill_color=WHITE,fill_opacity=1)
        t=text(str(s),32)
        if t.width>width-.2: t.scale_to_fit_width(width-.2)
        result.add(VGroup(box,t))
    return result.arrange(RIGHT,buff=.23).move_to([0,y,0])
def line(s,y=-1.7,size=25): return text(s,size).move_to([0,y,0])
def arrow(a,b): return Arrow(a,b,buff=.18,color=PALE,stroke_width=3,max_tip_length_to_length_ratio=.08)

class Base(Scene):
    def setup(self):
        self.camera.background_color=BG
        self.bid=self.__class__.__name__[:3]
        self.beat=next(b for b in SHEET['beats'] if b['beat_id']==self.bid)
        self.end=self.beat['actual_duration_s']
    def cue(self,phrase,fallback=0):
        ws=WORDS['beats'].get(self.bid,[])
        import re
        norm=lambda s:re.sub('[^a-z0-9]','',s.lower())
        target=[norm(w) for w in phrase.split()]
        for i in range(len(ws)-len(target)+1):
            if [norm(w['text']) for w in ws[i:i+len(target)]]==target:
                self.until(ws[i]['startFrame']/24);return
        raise ValueError(f"Missing audio cue {self.bid}: {phrase}")
    def until(self,t):
        if t>self.renderer.time+.04:self.wait(t-self.renderer.time)
    def finish(self):self.until(self.end)
    def reveal(self,*objects):
        self.play(LaggedStart(*[FadeIn(m,shift=UP*.08) for m in objects],lag_ratio=.12),run_time=.5)
    def swap(self,old,new):
        self.play(FadeOut(old,shift=UP*.08),run_time=.175)
        self.play(FadeIn(new,shift=UP*.08),run_time=.175)
    def highlight(self,mob):
        self.indicator=Line(mob.get_corner(DL)+DOWN*.16,mob.get_corner(DR)+DOWN*.16,color=ACC,stroke_width=4)
        self.play(FadeIn(self.indicator),run_time=.35)

class B01_Scene(Base):
    def construct(self):
        self.reveal(label('From Language to Model Input'))
        cells=tiles(['Text','Pieces','IDs'],width=2.5)
        self.reveal(cells)
        arrows=VGroup(*[arrow(cells[i].get_right(),cells[i+1].get_left()) for i in range(2)])
        # Extra space between pipeline stages, so arrows never touch labels.
        for i,c in enumerate(cells):c.move_to([(i-1)*3.7,0,0])
        arrows=VGroup(*[arrow(cells[i].get_right(),cells[i+1].get_left()) for i in range(2)])
        self.reveal(arrows)
        self.cue('divides text');self.highlight(cells[1])
        self.cue('assigns each');self.play(self.indicator.animate.move_to(cells[2].get_bottom()+DOWN*.16),run_time=.35)
        self.cue('It does not');self.reveal(line('Representation comes before understanding.',-1.7))
        self.finish()

class B02_Scene(Base):
    def construct(self):
        self.reveal(label('Choose the Pieces'))
        row=tiles(['cats'],width=2.4);note=line('Whole word',-1.45)
        self.reveal(row,note,line('Illustrative splits',-2.5,23))
        self.cue('split every character');n=tiles(['c','a','t','s']);self.swap(row,n);row=n;self.swap(note,line('Characters',-1.45));note=self.mobjects[-1]
        self.cue('reuse a piece');n=tiles(['cat','s'],width=1.8);self.swap(row,n);row=n;self.remove(note);note=line('Subwords',-1.45);self.reveal(note)
        self.cue('Whole words need');self.remove(row,note)
        comparison=VGroup(text('Whole words · Larger vocabulary',26),text('Characters · Longer sequences',26)).arrange(DOWN,buff=.8).move_to([0,0,0]);self.reveal(comparison)
        self.cue('Subwords offer');self.remove(comparison);self.reveal(tiles(['cat','s'],width=1.8),line('A reusable middle ground',-1.45))
        self.finish()

class B03_Scene(Base):
    def construct(self):
        self.reveal(label('Learn a Merge'),line('Toy training corpus',-2.5,23))
        corpus=VGroup(text('low  ×  5',34),text('lower  ×  2',34)).arrange(DOWN,buff=.7)
        self.reveal(corpus)
        self.cue('We start with characters');self.remove(corpus)
        row1=tiles(['l','o','w'],.6);row2=tiles(['l','o','w','e','r'],-.6)
        self.reveal(row1,row2)
        self.cue('L followed by o');self.remove(row1,row2)
        counts=VGroup(text('l + o     7',34),text('o + w     7',34)).arrange(DOWN,buff=.7)
        self.reveal(counts)
        self.cue('That is a tie');self.reveal(line('Tie → alphabetical order',-1.6,26))
        self.cue('l and o merge');self.play(Circumscribe(counts[0],color=ACC,fade_out=False),run_time=.6)
        self.finish()

class B04_Scene(Base):
    def construct(self):
        self.reveal(label('Merge, Then Count Again'),line('Toy tokenizer · two learned rules',-2.5,23))
        row=tiles(['lo','w'],.15,width=2)
        self.reveal(row,line('lo + w   appears 7 times',-1.5,28))
        self.cue('so it becomes low');self.play(row[0].animate.shift(RIGHT*.115),row[1].animate.shift(LEFT*.115),run_time=.45)
        self.remove(row);merged=tiles(['low'],.15,width=3.3);merged[0][0].set_stroke(PALE,width=2);self.reveal(merged,Line(LEFT*1.65+DOWN*.45,RIGHT*1.65+DOWN*.45,color=ACC,stroke_width=4))
        self.cue('We stop after two');self.remove(*[m for m in list(self.mobjects) if m is not merged and m.get_center()[1] < -1 and m.get_center()[1]>-2]);self.reveal(line('l + o → lo       lo + w → low',-1.5,28))
        self.finish()

class B05_Scene(Base):
    def construct(self):
        self.reveal(label('Apply the Saved Rules'),line('Toy tokenizer',-2.65,23))
        self.reveal(text('Text',24).move_to([-4.5,1.3,0]),text('Pieces',24).move_to([0,1.3,0]),text('IDs',24).move_to([4.5,1.3,0]))
        original=text('lower',36).move_to([-4.5,0,0]);pieces=tiles(['l','o','w','e','r'],width=.6).scale(.9);self.reveal(original,pieces)
        self.cue('then the two learned');self.remove(pieces);pieces=tiles(['low','e','r'],width=1).scale(.9);self.reveal(pieces)
        self.cue('Each piece has an ID');nums=text('6   0   3',32).move_to([4.5,0,0]);self.reveal(nums,arrow(original.get_right(),pieces.get_left()),arrow(pieces.get_right(),nums.get_left()))
        self.cue('Another tokenizer');self.reveal(line('These IDs belong to this vocabulary.',-1.6,25))
        self.finish()

class B06_Scene(Base):
    def construct(self):
        self.reveal(label('IDs Are Lookup Addresses'))
        row=tiles(['low','e','r'],.9);ids=tiles(['6','0','3'],-.5)
        self.reveal(row,ids)
        self.cue('The model uses');self.remove(row,ids)
        left=text('Token IDs',30).move_to([-4.4,0,0]);right=text('Learned vectors',30).move_to([4.0,0,0])
        table=VGroup(*[Rectangle(width=1.6,height=.38,stroke_color=PALE,stroke_width=2,fill_color=WHITE,fill_opacity=1) for _ in range(4)]).arrange(DOWN,buff=.12)
        self.reveal(left,right,table,arrow(left.get_right(),table.get_left()),arrow(table.get_right(),right.get_left()))
        self.play(table[2].animate.set_stroke(INK,width=3),run_time=.4)
        self.cue('The tokenizer supplies');self.reveal(line('Tokenizer → sequence     Model → context',-1.7,26))
        self.finish()

class B07_Scene(Base):
    def construct(self):
        self.reveal(label('Stress-Test the Vocabulary'))
        row=tiles(['L','o','w','e','r']);row[0][0].set_stroke(ACC,width=4);self.reveal(row)
        note=line('Toy vocabulary: capital L is missing.',-1.5,26);self.reveal(note)
        self.cue('Byte-level designs');self.remove(row,note)
        glyph=text('é',54).move_to([-3,0,0]);bytes_=tiles(['C3','A9'],width=1.6).move_to([2,0,0]);self.reveal(glyph,bytes_,arrow(glyph.get_right(),bytes_.get_left()),line('UTF-8 bytes · hexadecimal',-1.5,26))
        self.cue('but representing it');self.reveal(line('Coverage does not imply understanding.',-2.3,24))
        self.finish()

class B08_Scene(Base):
    def construct(self):
        self.reveal(label('Inspect the Actual Encoding'))
        row=tiles(['lower','Lower'],width=3);self.reveal(row)
        self.cue('then add a leading space');self.remove(row);row=tiles(['lower','[space]lower'],width=3.8);self.reveal(row,line('[space] marks one leading space',-1.5,25))
        self.cue('Inspect the actual');self.until(7.3);self.remove(row);self.remove(*[m for m in list(self.mobjects) if -2<m.get_center()[1]<-1]);self.reveal(VGroup(text('Tokenizer name',28),text('Exact input',28),text('Pieces and IDs',28)).arrange(DOWN,buff=.45).move_to([0,.3,0]))
        self.cue('Normalization');self.remove(*[m for m in list(self.mobjects) if -2<m.get_center()[1]<-1]);self.reveal(line('Decode → compare with the original',-1.8,25))
        self.finish()

class B09_Scene(Base):
    def construct(self):
        self.reveal(label('The Takeaway'))
        box=RoundedRectangle(width=10.2,height=3.6,corner_radius=.16,stroke_color=PALE,stroke_width=2,fill_color=WHITE,fill_opacity=1)
        points=VGroup(text('Pieces depend on the tokenizer.',28),text('IDs identify vocabulary entries.',28),text('Inspect the actual encoding.',28)).arrange(DOWN,buff=.65)
        self.reveal(box,points);self.finish()

class B10_Scene(Base):
    def construct(self):
        self.reveal(label('Your Turn',2.5,38))
        box=RoundedRectangle(width=11.1,height=3.1,corner_radius=.15,stroke_color=PALE,stroke_width=2,fill_color=WHITE,fill_opacity=1)
        prompt=VGroup(*[text(s,27) for s in ['Using a named tokenizer, compare lower, Lower,','and a space followed by lower. Show pieces, IDs,','and decoded text. Run the code; do not guess.']]).arrange(DOWN,buff=.32)
        self.reveal(box,prompt)
        self.cue('Check that the answer');self.remove(prompt)
        self.reveal(VGroup(text('Names its tokenizer',28),text('Includes reproducible code',28),text('Checks the decoded text',28)).arrange(DOWN,buff=.55))
        self.finish()

class B11_Scene(Base):
    def construct(self):
        self.clear();self.reveal(label('Tokenization',.8,45),label('How Machines Break Down Language',-.1,32),line('@sanjiv',-1.4,28));self.finish()
