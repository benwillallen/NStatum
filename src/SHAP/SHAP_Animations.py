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

class SHAP_Animations(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        marg_crtb_eq = MathTex("f(ACB)-f(AC)", font_size=70, color="#fff0d5")
        fet_before_eq = MathTex("|S|!", font_size=70, color="#fff0d5")
        fet_add_eq = MathTex("(|F|-|S|-1)!", font_size=70, color="#fff0d5")
        prob_sub_eq = MathTex("f_{S\\cup\\{i\\}}(x_{S\\cup\\{i\\}})-f_S(x_S)", font_size=70, color="#fff0d5")
        frac_eq = MathTex("\\frac{|S|!\\cdot(|F|-|S|-1)!}{|F|!}", font_size=70, color="#fff0d5")
        avg_marg_crtb_eq = MathTex("\\phi_i=\\sum_{S\\subseteq F\\setminus\\{i\\}}\\frac{|S|!\\cdot(|F|-|S|-1)!}{|F|!}(f_{S\\cup\\{i\\}}(x_{S\\cup\\{i\\}})-f_S(x_S))", font_size=50, color="#fff0d5")
        self.wait(1)
        self.play(Write(marg_crtb_eq))
        self.wait(2)
        self.play(TransformMatchingShapes(marg_crtb_eq, fet_before_eq))
        self.wait(2)
        self.play(TransformMatchingShapes(fet_before_eq, fet_add_eq))
        self.wait(2)
        self.play(TransformMatchingShapes(fet_add_eq, prob_sub_eq))
        self.wait(2)
        self.play(TransformMatchingShapes(prob_sub_eq, frac_eq))
        self.wait(2)
        self.play(TransformMatchingShapes(frac_eq, avg_marg_crtb_eq))
        self.wait(2)
        