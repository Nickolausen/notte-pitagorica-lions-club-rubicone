from manim import *
import cv2

class Splashscreen(Scene):
    def construct(self):
        cap = cv2.VideoCapture("../assets/pythagoras-moving.mp4")
        flag = True
        frame_imgs: List[ImageMobject] = []
        
        logos = ImageMobject("../assets/loghi.png")
        logos.to_corner(UL)
        logos.shift(UP * 1.4)
        self.add(logos)

        title = Tex(r"$\mathbb{N}$\textsc{otte} $\mathbb{P}$\textsc{itagorica}")
        subtitle = Tex(r"Errare humanum est, perseverare...\\ \textbf{pytagoricum}!")

        title.scale(1.7).to_edge(RIGHT).shift(UP * 1.5 + LEFT * .1)
        subtitle.next_to(title, DOWN, .2).scale(.8)
        self.add(title, subtitle)
        
        def make_circle(radius, hexColor):
             return Circle(radius).set_color(ManimColor.from_hex(hexColor)).set_z_index(-1)
        
        c1 = make_circle(3, "#2d2f6e").set_opacity(.4)
        c2 = make_circle(4, "#06072f").set_opacity(.6)
        c3 = make_circle(2.5, "#1a1c75").set_opacity(.3)
        c1.to_corner(UR).shift(UR * 3)
        c2.next_to(c1, DOWN).shift(UP * 2 + RIGHT * 2.5)
        c3.next_to(c1, LEFT).shift(RIGHT * 1.4)
        self.add(c1, c2, c3)

        tetractys = ImageMobject("../assets/tetraktys_nowriting.png").scale(.1)
        tetractys.to_corner(DR)
        self.add(tetractys)

        while flag:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame)
                frame_img.scale(1.3).shift(DOWN * 1.3 + LEFT * 1.7)
                frame_img.set_z_index(-1)
                frame_imgs.append(frame_img)
        cap.release()

        for _ in range(0, 1):
            frame_imgs.extend(reversed(frame_imgs))
             
        for frame_img in frame_imgs:
                self.add(frame_img)
                self.wait(0.06)
                self.remove(frame_img)
