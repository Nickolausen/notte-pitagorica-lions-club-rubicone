from manim import *
import cv2

class Pythagoras(Scene):
    def construct(self):
        cap = cv2.VideoCapture("../../assets/pythagoras-moving.mp4")
        flag = True
        frame_imgs: List[ImageMobject] = []

        while flag:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame)
                frame_img.scale(1.6).shift(DOWN * .8)
                frame_img.set_z_index(-1)
                frame_imgs.append(frame_img)
        cap.release()

        for _ in range(0, 1):
            frame_imgs.extend(reversed(frame_imgs))
             
        for frame_img in frame_imgs:
                self.add(frame_img)
                self.wait(0.06)
                self.remove(frame_img)
