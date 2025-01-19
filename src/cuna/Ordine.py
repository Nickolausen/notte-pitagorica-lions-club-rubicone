from manim import *

class Ordine(Scene):
    def construct(self):
        kosmos = Tex(r"\textsc{Kosmos}")
        kosmos.scale(5)
        self.add(kosmos)
        ordine = Tex(r"\textsc{Ordine}")
        ordine.scale(5)
        self.play(Transform(kosmos, ordine), run_time=2)