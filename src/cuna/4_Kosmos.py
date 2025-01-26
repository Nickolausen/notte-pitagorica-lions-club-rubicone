from manim import *

class Kosmos(Scene):
    def construct(self): 
        bg = ImageMobject("../../assets/stelle-finale.jpg")
        bg.scale(3).set_z_index(-1).set_opacity(.4)
        self.add(bg)

        kosmos = Tex(r"\textsc{Kosmos}")
        kosmos.scale(5)
        self.play(Write(kosmos), run_time=2)