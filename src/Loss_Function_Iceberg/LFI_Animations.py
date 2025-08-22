from manim import *
from Manim_Functions import set_defaults

config.background_color = "#001014"

# DARKER: #1993C8 #A28F02 #627E26 #7C2927 #8C4103
# BLUE: #5BC0EB YELLOW: #FEE20B GREEN: #9BC53D RED: #C3423F ORANGE: #F17105
# LIGHTER: #B6E3F6 #FEED72 #C6DE91 #D88483 #FCA65F

# New Color Scheme
# DARK BLUE: #1B264F
# BLUE: #007991
# LIGHT BLUE: #0E9594
# RED: #D62828
# BLACK #21201E

class LFI1_Intro(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Loss Function Iceberg", font_size=96).to_edge(UP)
        subtitle = Text("Understanding Loss Functions in Machine Learning", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(subtitle, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(author, shift=UP), run_time=2)
        self.wait(2)

        self.play(FadeOut(title, shift=UP), FadeOut(subtitle, shift=UP), FadeOut(author, shift=UP), run_time=2)
        self.wait(1)