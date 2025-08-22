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

class LFIA1_Intro(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Loss Function Iceberg", font_size=96).to_edge(UP)
        subtitle = Text("Understanding Loss Functions in Machine Learning", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(subtitle, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeOut(title, shift=UP), FadeOut(subtitle, shift=UP)),
        self.wait(1)

# -----------------------------
# -------- LAYER ONE ----------
# -----------------------------

class LFIB2_MSE(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Mean Squared Error (MSE)", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{MSE} = \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIC3_MAE(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Mean Absolute Error (MAE)", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{MAE} = \\frac{1}{n} \\sum_{i=1}^{n} |y_i - \\hat{y}_i|", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFID4_BinaryCrossEntropy(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Binary Cross-Entropy", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{BCE} = -\\frac{1}{n} \\sum_{i=1}^{n} [y_i \\log(\\hat{y}_i) + (1 - y_i) \\log(1 - \\hat{y}_i)]", font_size=36).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIE5_CategoricalCrossEntropy(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Categorical Cross-Entropy", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{CCE} = -\\sum_{i=1}^{n} y_i \\log(\\hat{y}_i)", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIF6_HingeLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Hinge Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Hinge Loss} = \\sum_{i=1}^{n} \\max(0, 1 - y_i \\hat{y}_i)", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)

# -----------------------------
# -------- LAYER TWO ----------
# -----------------------------

class LFIG7_MAPE(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Mean Absolute Percentage Error (MAPE)", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{MAPE} = \\frac{1}{n} \\sum_{i=1}^{n} \\left| \\frac{y_i - \\hat{y}_i}{y_i} \\right|", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH8_SMAPE(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Symmetric Mean Absolute Percentage Error (SMAPE)", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{SMAPE} = \\frac{1}{n} \\sum_{i=1}^{n} \\frac{|y_i - \\hat{y}_i|}{|y_i| + |\\hat{y}_i|}", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH9_HuberLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Huber Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Huber Loss} = \\sum_{i=1}^{n} \\begin{cases} \\frac{1}{2}(y_i - \\hat{y}_i)^2 & \\text{if } |y_i - \\hat{y}_i| \\leq \\delta \\\\ \\delta |y_i - \\hat{y}_i| - \\frac{1}{2}\\delta^2 & \\text{otherwise} \\end{cases}", font_size=36).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH10_SmoothL1Loss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Smooth L1 Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Smooth L1 Loss} = \\sum_{i=1}^{n} \\begin{cases} \\frac{1}{2}(y_i - \\hat{y}_i)^2 & \\text{if } |y_i - \\hat{y}_i| < 1 \\\\ |y_i - \\hat{y}_i| - \\frac{1}{2} & \\text{otherwise} \\end{cases}", font_size=36).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH11_LogCoshLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Log Cosh Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Log Cosh Loss} = \\sum_{i=1}^{n} \\log(\\cosh(y_i - \\hat{y}_i))", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH12_MSLE(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Mean Squared Logarithmic Error (MSLE)", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{MSLE} = \\frac{1}{n} \\sum_{i=1}^{n} (\\log(y_i + 1) - \\log(\\hat{y}_i + 1))^2", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH13_PoissonLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Poisson Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Poisson Loss} = \\sum_{i=1}^{n} (\\hat{y}_i - y_i \\log(\\hat{y}_i))", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH14_KLDivergence(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Kullback–Leibler Divergence", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{KL}(P || Q) = \\sum_{i} P(i) \\log\\left(\\frac{P(i)}{Q(i)}\\right)", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH15_GaussianNLLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Gaussian Negative Log Likelihood Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{NLL} = \\frac{1}{2} \\log(2\\pi\\sigma^2) + \\frac{(y - \\mu)^2}{2\\sigma^2}", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)

# -----------------------------
# ------- LAYER THREE ---------
# -----------------------------

class LFIH16_SquaredHingeLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Squared Hinge Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Squared Hinge Loss} = \\sum_{i=1}^{n} \\max(0, 1 - y_i \\hat{y}_i)^2", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH17_SoftMarginLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Soft Margin Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Soft Margin Loss} = \\sum_{i=1}^{n} \\log(1 + \\exp(-y_i \\hat{y}_i))", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH18_MarginRankingLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Margin Ranking Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Margin Ranking Loss} = \\sum_{i=1}^{n} \\max(0, -y_i (\\hat{y}_i - \\hat{y}_j) + \\text{margin})", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH19_PairwiseHingeLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Pairwise Hinge Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Pairwise Hinge Loss} = \\sum_{i,j} \\max(0, 1 - y_i (\\hat{y}_i - \\hat{y}_j))", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH20_SoftPairwiseHingeLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Soft Pairwise Hinge Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Soft Pairwise Hinge Loss} = \\sum_{i,j} \\log(1 + \\exp(-y_i (\\hat{y}_i - \\hat{y}_j)))", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH21_PairwiseLogisticLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Pairwise Logistic Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Pairwise Logistic Loss} = \\sum_{i,j} \\log(1 + \\exp(-y_i (\\hat{y}_i - \\hat{y}_j)))", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH22_CosineEmbeddingLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Cosine Embedding Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Cosine Embedding Loss} = \\sum_{i} \\max(0, -y_i (\\hat{y}_i \\cdot \\hat{y}_j) + \\text{margin})", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH23_HingeEmbeddingLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Hinge Embedding Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Hinge Embedding Loss} = \\sum_{i} \\max(0, 1 - y_i (\\hat{y}_i - \\hat{y}_j))", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH24_TripletMarginLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Triplet Margin Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Triplet Margin Loss} = \\sum_{i,j,k} \\max(0, d(a_i, p_i) - d(a_i, n_i) + \\text{margin})", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)

# -----------------------------
# -------- LAYER FOUR ---------
# -----------------------------

class LFIH25_FocalCrossEntropyLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Focal Cross-Entropy Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Focal Loss} = -\\alpha (1 - \\hat{y}_i)^{\\gamma} \\log(\\hat{y}_i)", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH26_BalancedCrossEntropyLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Balanced Cross-Entropy Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Balanced BCE} = -\\frac{1}{n} \\sum_{i=1}^{n} \\left( \\beta y_i \\log(\\hat{y}_i) + (1 - y_i) \\log(1 - \\hat{y}_i) \\right)", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH27_DiceLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Dice Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Dice Loss} = 1 - \\frac{2 \\sum_{i=1}^{n} y_i \\hat{y}_i}{\\sum_{i=1}^{n} y_i + \\sum_{i=1}^{n} \\hat{y}_i}", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH28_TverskyLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Tversky Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Tversky Loss} = \\frac{\\alpha \\sum_{i=1}^{n} y_i \\hat{y}_i}{\\alpha \\sum_{i=1}^{n} y_i + (1 - \\alpha) \\sum_{i=1}^{n} (1 - y_i) \\hat{y}_i}", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)

# -----------------------------
# -------- LAYER FIVE ---------
# -----------------------------

class LFIH29_CTC(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Connectionist Temporal Classification (CTC) Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{CTC Loss} = -\\log \\sum_{y \\in \\mathcal{Y}} \\prod_{t=1}^{T} p(y_t | x_t)", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH30_PinballLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Pinball Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Pinball Loss} = \\sum_{i=1}^{n} \\max(\\tau (y_i - \\hat{y}_i), (1 - \\tau)(\\hat{y}_i - y_i))", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH31_TweedieLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Tweedie Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Tweedie Loss} = \\sum_{i=1}^{n} \\left( y_i \\log(\\hat{y}_i) - \\hat{y}_i + \\frac{y_i^2}{2\\phi} \\right)", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)


class LFIH32_WassersteinLoss(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        
        title = Text("Wasserstein Loss", font_size=72).to_edge(UP)
        formula = MathTex(r"\\text{Wasserstein Loss} = \\int_{\\mathcal{X}} \\left| F(x) - G(x) \\right| dx", font_size=48).next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeIn(formula, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(formula, shift=UP)),
        self.wait(1)