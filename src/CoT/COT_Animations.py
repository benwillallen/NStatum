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


class Grid_Blank(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)


class Logical_Deduction(Scene):
    def construct(self):
        b_plane = set_defaults()
        equation_1 = MathTex("P\\implies Q", font_size=70, color="#fff0d5")
        self.add(equation_1)


class Ending_Animation(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        thanks_message = Text("Thanks for Watching!", font='Futura Std', font_size=80, color="#fff0d5") \
            .shift(2.5 * UP)
        long_rectangle1 = Rectangle(height=0.7, width=3.6, stroke_width=9, color="#998675",
                                    fill_color="#fff0d5", fill_opacity=1, z_index=0)
        long_rectangle2 = Rectangle(height=0.7, width=3.6, stroke_width=9, color="#998675",
                                    fill_color="#fff0d5", fill_opacity=1, z_index=1) \
            .rotate(PI / 2)
        short_rectangle1 = Rectangle(height=0.7, width=2.15, stroke_width=9, color="#998675",
                                     fill_color="#fff0d5", fill_opacity=1, z_index=0) \
            .shift(1.45 * UP + 0.725 * LEFT)
        short_rectangle2 = Rectangle(height=0.7, width=2.15, stroke_width=9, color="#998675",
                                     fill_color="#fff0d5", fill_opacity=1, z_index=1) \
            .rotate(PI / 2).shift(1.45 * LEFT + 0.725 * UP)
        vlogo = VGroup(long_rectangle1, short_rectangle1, long_rectangle2, short_rectangle2) \
            .rotate(PI / 4).shift(DOWN + 0.5 * RIGHT)
        self.play(DrawBorderThenFill(thanks_message), DrawBorderThenFill(vlogo), Wait(2))
        self.play(vlogo[0].animate.set_stroke_color("#ff9955"), vlogo[1].animate.set_stroke_color("#55a5ff"),
                  vlogo[2].animate.set_stroke_color("#55ffb5"), vlogo[3].animate.set_stroke_color("#ff5555"), Wait(2))
        self.play(FadeOut(thanks_message),
                  AnimationGroup(vlogo[2].animate.shift(7 * UP + 7 * LEFT),
                                 vlogo[3].animate.shift(7 * DOWN + 7 * RIGHT),
                                 vlogo[0].animate.shift(7 * UP + 7 * RIGHT),
                                 vlogo[1].animate.shift(7 * DOWN + 7 * LEFT), Wait(2),
                                 lag_ratio=0.1))