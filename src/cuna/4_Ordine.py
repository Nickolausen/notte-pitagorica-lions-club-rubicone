from manim import *

class Ordine(Scene):
    def construct(self):
        bg = ImageMobject("../../assets/stelle-finale.jpg")
        bg.scale(3).set_z_index(-1).set_opacity(.4)
        self.add(bg)
        kosmos = Tex(r"\textsc{Kosmos}")
        kosmos.scale(5)
        self.add(kosmos)
        ordine = Tex(r"\textsc{Ordine}")
        ordine.scale(5)
        self.play(Transform(kosmos, ordine), run_time=2)