"""
2026-02-18
Ivan Zheryakov
Arcade TP5 theorie
"""

import arcade
from arcade import open_window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tutoriel Arcade"


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()  # + Start ↕
# ELLIPSE
arcade.draw.draw_ellipse_filled(400,
                                400,
                                500,
                                369,
                                arcade.color.DEEP_LEMON,
                                tilt_angle=50, num_segments=5)
# RECTANGLE
arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH,
                                       0,
                                       SCREEN_HEIGHT / 2,
                                       arcade.csscolor.DARK_GREEN)

# CIRCLE
arcade.draw.draw_circle_outline(200,
                                200,
                                60,
                                arcade.color.BUBBLE_GUM,
                                num_segments=8, tilt_angle=35)
arcade.draw.draw_circle_outline(400,
                                200,
                                60,
                                arcade.color.BUBBLE_GUM
                                , num_segments=8)

# RECTANGLE FOREST
r = arcade.rect.XYWH(200, SCREEN_HEIGHT / 2, 30, 60)
rr = arcade.rect.XYWH(250, 225, 30, 60)
rrr = arcade.rect.XYWH(300, 250, 30, 60)
rrrr = arcade.rect.XYWH(350, 235, 30, 60)
rrrrr = arcade.rect.XYWH(400, 280, 30, 60)

r_equator = arcade.rect.XYWH(SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2,
                             SCREEN_WIDTH, 2)
r_rotation = arcade.rect.XYWH(SCREEN_WIDTH / 2,
                              SCREEN_HEIGHT / 2,
                              2,
                              SCREEN_HEIGHT)

arcade.draw.draw_rect_filled(r_equator, arcade.color.BLACK)
arcade.draw.draw_rect_filled(r_rotation, arcade.color.BLACK)
arcade.draw.draw_rect_filled(r, arcade.color.BROWN)
arcade.draw.draw_rect_filled(rr, arcade.color.BROWN)
arcade.draw.draw_rect_filled(rrr, arcade.color.BROWN)
arcade.draw.draw_rect_filled(rrrr, arcade.color.BROWN)
arcade.draw.draw_rect_filled(rrrrr, arcade.color.BROWN)

# ARC
arcade.draw.draw_arc_filled(200, SCREEN_HEIGHT / 2 + 20,
                            60, 100,
                            arcade.csscolor.FOREST_GREEN,
                            0, 180)

arcade.draw.draw_arc_filled(250, 245,
                            60, 93,
                            arcade.csscolor.FOREST_GREEN,
                            0, 180)

arcade.draw.draw_arc_filled(300, 270,
                            60, 86,
                            arcade.csscolor.FOREST_GREEN,
                            0, 180)

arcade.draw.draw_arc_filled(350, 245,
                            58, 80,
                            arcade.csscolor.FOREST_GREEN,
                            0, 180)

arcade.draw.draw_arc_filled(400, 300,
                            80, 55,
                            arcade.csscolor.FOREST_GREEN,
                            0, 180)



arcade.finish_render()  #  - Finish ↕
arcade.run()  #  Makes whatever was in between those two.
