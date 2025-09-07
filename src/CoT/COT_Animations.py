from manim import *
from src.Manim_Functions import set_defaults

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

class COT_Animations(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        equation_1 = MathTex("\\binom{5}{2}\\times7\\times\\binom{4}{2}", font_size=70, color="#fff0d5")
        equation_2 = MathTex("\\frac{5!}{2!(5-2)!}\\times7\\times\\frac{4!}{2!(4-2)!}", font_size=70, color="#fff0d5")
        equation_3 = MathTex("10\\times7\\times6", font_size=70, color="#fff0d5")
        equation_final = MathTex("420", font_size=70, color="#fff0d5")
        combination_formula = MathTex("\\binom{n}{r} = \\frac{n!}{r!(n-r)!}", font_size=40, color="#fff0d5").next_to(equation_1, DOWN).shift(DOWN)
        note_text = Text("Note:", font_size=36, color="#fff0d5").next_to(combination_formula, LEFT, buff = 0.5)
        self.wait(1)
        self.play(AnimationGroup(Write(equation_1), Write(note_text), Write(combination_formula), lag_ratio=0.5))
        self.wait(3)
        self.play(TransformMatchingShapes(equation_1, equation_2))
        self.wait(3)
        self.play(TransformMatchingShapes(equation_2, equation_3))
        self.wait(3)
        self.play(TransformMatchingShapes(equation_3, equation_final),
                  Write(SurroundingRectangle(equation_final, fill_color="#fff0d5", buff=0.2), run_time=3))
        self.wait(2)