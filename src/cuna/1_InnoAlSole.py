from manim import *

class InnoAlSole(Scene):
    def construct(self):
        img = ImageMobject("../../assets/hymn-to-the-rising-sun.jpg")
        img_title = Tex(r"\textsc{Pitagorici celebrano il sorgere del Sole}")
        img_artist_and_date = Tex(r"\textit{Fëdor Bronnikov, 1869}")
        self.play(FadeIn(img), run_time=1)
        self.wait(2)
        self.play(img.animate.shift(UP * .6))
        self.wait()
        self.play(img.animate.scale(.9))
        img_title.next_to(img, DOWN, .35)
        img_title.scale(1.2)
        self.play(Write(img_title))
        img_artist_and_date.next_to(img_title, DOWN, .3)
        img_artist_and_date.scale(.8)
        self.play(Write(img_artist_and_date))
        
        