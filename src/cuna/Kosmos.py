from manim import *

class Kosmos(Scene):
    def construct(self):
        kosmos = Tex(r"\textsc{Kosmos}")
        kosmos.scale(5)
        self.play(Write(kosmos), run_time=2)