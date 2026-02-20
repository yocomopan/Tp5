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
arcade.start_render()  # Start ↕
arcade.draw.draw_ellipse_filled(400,
                                400,
                                500,
                                369,
                                arcade.color.DEEP_LEMON,
                                tilt_angle=50, num_segments=5)

arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 2, arcade.csscolor.DARK_GREEN)
r = arcade.rect.XYWH(200, SCREEN_HEIGHT / 2, 30, 60)
r_equator = arcade.rect.XYWH(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, 2)

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
arcade.draw.draw_ellipse_filled(400,
                                300,
                                10,
                                10,
                                arcade.color.DEEP_SKY_BLUE,
                                tilt_angle=50, num_segments=7)


arcade.draw.draw_rect_filled(r, arcade.color.BROWN)
arcade.draw.draw_rect_filled(r, arcade.color.BLACK)

arcade.finish_render()  #  Finish ↕
arcade.run()  #  Makes whatever was in between those two.
