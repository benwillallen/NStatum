from manim import *
from src.Manim_Functions import set_defaults
import random

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

# ── Shared palette ──────────────────────────────────────────────────────────
NODE_COLOR      = "#5BC0EB"
EDGE_COLOR      = "#F17105"
HIGHLIGHT_COLOR = "#FEE20B"
TEXT_COLOR      = "#fff0d5"
DIM_COLOR       = GRAY_D
TREE_GREEN      = "#9BC53D"
TREE_LEAF       = "#627E26"

# ════════════════════════════════════════════════════════════════════════════
# SCENE 1 — Growing Graph  (1m)
# Narration: "As machine learning models have improved over time, they've also
#             become increasingly complex."
# ════════════════════════════════════════════════════════════════════════════
class SHAPANIM_A1(Scene):
    """
    A directed graph starts as a tidy 3-node network and grows wave by wave
    until the screen is a dense, tangled web.
    """
 
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)

        random.seed(24)
 
        # ── helpers ─────────────────────────────────────────────────────────
        def make_node(pos, radius=0.22):
            return Circle(radius=radius, color=NODE_COLOR,
                          fill_color=NODE_COLOR, fill_opacity=0.9,
                          stroke_width=2).move_to(pos)
 
        def make_arrow(start_mob, end_mob):
            return Arrow(
                start_mob.get_center(), end_mob.get_center(),
                buff=0.22, stroke_width=4,
                max_tip_length_to_length_ratio=0.15,
                color=EDGE_COLOR
            )
 
        # ── Wave 0 — three nodes, two edges (clean, readable) ───────────────
        positions_w0 = [LEFT * 3, ORIGIN, RIGHT * 3]
        nodes = [make_node(p) for p in positions_w0]
        label_text = Text("Simple Model", font_size=28, color=TEXT_COLOR
                          ).to_edge(UP, buff=0.5)
 
        self.play(FadeIn(label_text))
        self.play(LaggedStart(*[GrowFromCenter(n) for n in nodes], lag_ratio=0.3))
 
        edges = [make_arrow(nodes[0], nodes[1]),
                 make_arrow(nodes[1], nodes[2])]
        self.play(LaggedStart(*[GrowArrow(e) for e in edges], lag_ratio=0.3))
        self.wait(0.6)
 
        # ── Wave 1 — add 4 nodes in a rough layer, cross-connect ────────────
        new_label = Text("More Complex…", font_size=28, color=TEXT_COLOR
                         ).to_edge(UP, buff=0.5)
        self.play(Transform(label_text, new_label))
 
        positions_w1 = [
            LEFT * 2 + UP * 1.8,  RIGHT * 0.5 + UP * 2,
            LEFT * 0.8 + DOWN * 1.8, RIGHT * 2.2 + DOWN * 1.5,
        ]
        new_nodes_1 = [make_node(p, 0.20) for p in positions_w1]
        self.play(LaggedStart(*[GrowFromCenter(n) for n in new_nodes_1],
                               lag_ratio=0.2, run_time=1.2))
 
        cross_pairs_1 = [(nodes[0], new_nodes_1[0]),
                         (nodes[1], new_nodes_1[1]),
                         (nodes[2], new_nodes_1[3]),
                         (new_nodes_1[0], nodes[1]),
                         (new_nodes_1[2], nodes[2]),
                         (new_nodes_1[1], new_nodes_1[3])]
        cross_edges_1 = [make_arrow(a, b) for a, b in cross_pairs_1]
        self.play(LaggedStart(*[GrowArrow(e) for e in cross_edges_1],
                               lag_ratio=0.12, run_time=1.4))
        nodes.extend(new_nodes_1)
        edges.extend(cross_edges_1)
        self.wait(0.4)
 
        # ── Wave 2 — scatter 8 more nodes, dense random connections ─────────
        new_label2 = Text("Even More Complex…", font_size=28, color=TEXT_COLOR
                          ).to_edge(UP, buff=0.5)
        self.play(Transform(label_text, new_label2))
 
        positions_w2 = [
            LEFT * 4   + UP * 0.6,   LEFT * 3.2 + DOWN * 2.2,
            LEFT * 1.5 + UP * 2.8,   RIGHT * 2.4 + UP * 3.2,
            RIGHT * 3.5 + UP * 1.6,  RIGHT * 4.0 + DOWN * 0.5,
            RIGHT * 1.8 + DOWN * 2.8, LEFT * 0.3 + DOWN * 3.0,
        ]
        new_nodes_2 = [make_node(p, 0.17) for p in positions_w2]
        self.play(LaggedStart(*[GrowFromCenter(n) for n in new_nodes_2],
                               lag_ratio=0.12, run_time=1.6))
 
        # random cross-wiring to make it messy
        all_nodes = nodes + new_nodes_2
        random.shuffle(all_nodes)
        dense_pairs = [(all_nodes[i], all_nodes[j])
                       for i in range(len(all_nodes))
                       for j in range(i + 1, len(all_nodes))
                       if random.random() < 0.18]
        dense_edges = [make_arrow(a, b) for a, b in dense_pairs[:20]]
        self.play(LaggedStart(*[GrowArrow(e) for e in dense_edges],
                               lag_ratio=0.06, run_time=2.2))
 
        # final label
        final_label = Text("Complex Model", font_size=28, color=HIGHLIGHT_COLOR
                           ).to_edge(UP, buff=0.5)
        self.play(Transform(label_text, final_label))
        self.wait(1.0)


# ════════════════════════════════════════════════════════════════════════════
# SCENE 2 — Simple Models & Decision Tree Logic  (2m)
# Narration: "In simple models—like linear regression or decision trees—we can
#             usually explain predictions clearly and rigorously. We can trace
#             how each input affects the output …"
# ════════════════════════════════════════════════════════════════════════════
class SHAPANIM_B2(Scene):
    """
    Part A: Two model icons appear side-by-side (linear regression line,
            decision tree silhouette).
    Part B: Decision tree icon is highlighted; camera zooms in (scale up).
            Individual decision rules slide out as readable text boxes.
    """
 
    # ── Linear Regression icon ───────────────────────────────────────────────
    def _make_lr_icon(self) -> VGroup:
        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 4, 1],
            x_length=2.8, y_length=2.2,
            axis_config={"stroke_color": GRAY_B, "stroke_width": 2,
                         "include_ticks": False},
        )
        # scatter dots
        dot_coords = [(0.6, 0.8), (1.1, 1.3), (1.6, 1.9),
                      (2.2, 2.1), (2.8, 2.7), (3.3, 3.1)]
        dots = VGroup(*[Dot(axes.c2p(x, y), radius=0.07,
                            color=BLUE_C) for x, y in dot_coords])
        # best-fit line
        line = axes.plot(lambda x: 0.82 * x + 0.4,
                         x_range=[0.3, 3.7], color=YELLOW, stroke_width=2.5)
        label = Text("Linear\nRegression", font_size=20, color=TEXT_COLOR,
                     line_spacing=0.8).next_to(axes, DOWN, buff=0.15)
        return VGroup(axes, dots, line, label)
 
    # ── Decision Tree icon ────────────────────────────────────────────────────
    def _make_tree_icon(self) -> VGroup:
        """Returns a small stylized decision tree."""
        # root
        root_box  = RoundedRectangle(width=1.4, height=0.55, corner_radius=0.1,
                                     color=TREE_GREEN, fill_color=TREE_GREEN,
                                     fill_opacity=0.8, stroke_width=2)
        root_text = Text("x1 > 3?", font_size=16, color=TEXT_COLOR).move_to(root_box)
        root = VGroup(root_box, root_text).shift(UP * 1.5)
 
        # left child
        lc_box  = RoundedRectangle(width=1.4, height=0.55, corner_radius=0.1,
                                   color=TREE_GREEN, fill_color=TREE_GREEN,
                                   fill_opacity=0.8, stroke_width=2)
        lc_text = Text("x2 > 5?", font_size=16, color=TEXT_COLOR).move_to(lc_box)
        left_child = VGroup(lc_box, lc_text).shift(LEFT * 1.5)
 
        # right child
        rc_box  = RoundedRectangle(width=1.4, height=0.55, corner_radius=0.1,
                                   color=TREE_GREEN, fill_color=TREE_GREEN,
                                   fill_opacity=0.8, stroke_width=2)
        rc_text = Text("x3 < 2?", font_size=16, color=TEXT_COLOR).move_to(rc_box)
        right_child = VGroup(rc_box, rc_text).shift(RIGHT * 1.5)
 
        # leaves
        def leaf(text, pos):
            b = RoundedRectangle(width=1.1, height=0.45, corner_radius=0.08,
                                 color=TREE_LEAF, fill_color=TREE_LEAF,
                                 fill_opacity=0.9, stroke_width=1.5).move_to(pos)
            t = Text(text, font_size=14, color=TEXT_COLOR).move_to(b)
            return VGroup(b, t)
 
        ll = leaf("Yes",  LEFT * 2.25 + DOWN * 1.5)
        lr = leaf("No",   LEFT * 0.75 + DOWN * 1.5)
        rl = leaf("Yes",  RIGHT * 0.75 + DOWN * 1.5)
        rr = leaf("No",   RIGHT * 2.25 + DOWN * 1.5)
 
        # edges
        def edge(a, b):
            return Line(a.get_bottom(), b.get_top(),
                        stroke_width=1.8, color=GRAY_B)
 
        edges = VGroup(
            edge(root, left_child), edge(root, right_child),
            edge(left_child, ll),   edge(left_child, lr),
            edge(right_child, rl),  edge(right_child, rr),
        )
 
        label = Text("Decision Tree", font_size=20, color=TEXT_COLOR,
                     line_spacing=0.8).next_to(root_box, DOWN, buff=3.2)
 
        return VGroup(edges, root, left_child, right_child, ll, lr, rl, rr, label)
 
    # ── Rule boxes that "slide out" ───────────────────────────────────────────
    def _make_rules(self) -> VGroup:
        rules = [
            "IF  x1 > 3  AND  x2 > 5  |  Predict: Yes",
            "IF  x1 > 3  AND  x2 ≤ 5  |  Predict: No",
            "IF  x1 ≤ 3  AND  x3 < 2  |  Predict: Yes",
            "IF  x1 ≤ 3  AND  x3 ≥ 2  |  Predict: No",
        ]
        colors = [GREEN_C, RED_C, GREEN_C, RED_C]
        boxes = VGroup()
        for i, (rule, col) in enumerate(zip(rules, colors)):
            bg = RoundedRectangle(width=8.5, height=0.55, corner_radius=0.1,
                                  fill_color=col, fill_opacity=0.15,
                                  stroke_color=col, stroke_width=1.5)
            txt = Text(rule, font_size=20, color=TEXT_COLOR).move_to(bg)
            row = VGroup(bg, txt)
            boxes.add(row)
        boxes.arrange(DOWN, buff=0.22).move_to(ORIGIN).shift(0.5*DOWN)
        return boxes
 
    # ── Scene construct ───────────────────────────────────────────────────────
    def construct(self):
 
        b_plane = set_defaults()
        self.add(b_plane)

        # ── PART A: two icons side by side ───────────────────────────────────
        title = Text("Simple Models", font_size=40, color=TEXT_COLOR,
                     weight=BOLD).to_edge(UP, buff=0.45)
        self.play(FadeIn(title, shift=DOWN * 0.3))
 
        lr_icon   = self._make_lr_icon().scale(0.85).shift(LEFT * 3.2 + DOWN * 0.2)
        tree_icon = self._make_tree_icon().scale(0.75).shift(RIGHT * 2.5 + DOWN * 0.2)
 
        self.play(
            LaggedStart(
                FadeIn(lr_icon,   shift=RIGHT * 0.4),
                FadeIn(tree_icon, shift=LEFT  * 0.4),
                lag_ratio=0.4,
            ),
            run_time=1.4,
        )
        self.wait(0.6)
 
        # ── PART B: highlight tree, dim LR, scale up tree ────────────────────
        highlight_ring = SurroundingRectangle(
            tree_icon, color=HIGHLIGHT_COLOR,
            corner_radius=0.12, buff=0.18, stroke_width=2.5,
        )
        self.play(
            lr_icon.animate.set_opacity(0.25),
            Create(highlight_ring),
            run_time=0.9,
        )
 
        # move tree to center and enlarge
        self.play(
            FadeOut(lr_icon),
            FadeOut(highlight_ring),
            tree_icon.animate.scale(1.3).move_to(ORIGIN + UP * 0.3),
            FadeOut(title),
            run_time=1.0,
        )
        self.wait(0.3)
 
        # ── PART C: rules slide in from the tree ─────────────────────────────
        rule_label = Text(
            "Extracted Decision Rules", font_size=28,
            color=HIGHLIGHT_COLOR
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(rule_label, shift=DOWN * 0.2))
 
        # shrink tree to top-left corner
        self.play(
            tree_icon.animate.scale(0.45).to_corner(UL, buff=0.6).shift(DOWN * 0.4),
            run_time=0.9,
        )
 
        rules = self._make_rules()
 
        # animate each rule sliding in from the direction of the tree
        for i, rule_box in enumerate(rules):
            rule_box.set_opacity(0)
            rule_box.shift(LEFT * 3)   # start off-screen left (tree side)
 
        self.play(
            LaggedStart(
                *[
                    AnimationGroup(
                        rule.animate.set_opacity(1).shift(RIGHT * 3),
                    )
                    for rule in rules
                ],
                lag_ratio=0.35,
            ),
            run_time=2.2,
        )
        self.wait(1.2)
 
        # final fade for transition to Scene 4 (SHAP explanation)
        self.play(
            FadeOut(rules),
            FadeOut(tree_icon),
            FadeOut(rule_label),
            run_time=0.8,
        )

class SHAP_Animations(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        marg_crtb_eq = MathTex("f(ACB)-f(AC)", font_size=70, color="#fff0d5")
        fet_before_eq = MathTex("|S|!", font_size=70, color="#fff0d5")
        fet_add_eq = MathTex("(|F|-|S|-1)!", font_size=70, color="#fff0d5")
        prob_sub_eq = MathTex("f_{S\\cup\\{i\\}}(x_{S\\cup\\{i\\}})-f_S(x_S)", font_size=70, color="#fff0d5")
        frac_eq = MathTex("\\frac{|S|!\\cdot(|F|-|S|-1)!}{|F|!}", font_size=70, color="#fff0d5")
        avg_marg_crtb_eq = MathTex("\\phi_i=\\sum_{S\\subseteq F\\setminus\\{i\\}}\\frac{|S|!\\cdot(|F|-|S|-1)!}{|F|!}(f_{S\\cup\\{i\\}}(x_{S\\cup\\{i\\}})-f_S(x_S))",
                                   font_size=50, color="#fff0d5")
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
        