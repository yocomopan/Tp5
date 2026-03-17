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
arcade.set_background_color(arcade.color.LIMERICK)
arcade.start_render()  # + Start ↕
# ELLIPSE
"""
arcade.draw.draw_ellipse_filled(400,
                                400,
                                500,
                                369,
                                arcade.color.ANTIQUE_BRONZE,
                                tilt_angle=50, num_segments=5)
"""
# RECTANGLE


# CIRCLE
"""
arcade.draw.draw_circle_outline(200,
                                200,
                                60,
                                arcade.color.BUBBLE_GUM,
                                num_segments=8, tilt_angle=35)
arcade.draw.draw_circle_filled(400,
                                200,
                                60,
                                arcade.color.BUBBLE_GUM
                                , num_segments=8)
"""
# RECTANGLE FOREST

r_equator = arcade.rect.XYWH(SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2,
                             SCREEN_WIDTH, 2)
r_rotation = arcade.rect.XYWH(SCREEN_WIDTH / 2,
                              SCREEN_HEIGHT / 2,
                              2, SCREEN_HEIGHT)

arcade.draw_rect_filled(r_equator,arcade.csscolor.BLACK)
arcade.draw_rect_filled(r_rotation, arcade.csscolor.BLACK)

# ARC
"""
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

arcade.draw.draw_arc_filled(400, 290,
                            40, 29,
                            arcade.csscolor.DARK_RED,
                            0, 180)
"""
# TRIANGLE
"""
y = SCREEN_HEIGHT / 2 + 40
arcade.draw.draw_triangle_filled(500, y + 40,
                           470, y - 20,
                           530, y - 20,
                           arcade.color.FOREST_GREEN)
"""
# LIGNE
"""
arcade.draw.draw_line(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 110,
                      SCREEN_WIDTH, SCREEN_HEIGHT - 110,
                      arcade.color.BANANA_YELLOW, 10)

points = [(700, 300), (750, 600), (345, 675)]
arcade.draw.draw_line_strip(points, arcade.color.BUFF)

un_tuple = (23, True , ["a", "b"])

points = [(700, 300), (750, 600), (345, 675)]

line_list = [(139, 556), (720, 512), (773, 704), (710, 596)]
arcade.draw.draw_lines(line_list, arcade.color.FOREST_GREEN)
"""
# POLYGONE
"""
pointss = [(700, 300), (750, 600), (345, 675)]
arcade.draw.draw_polygon_filled(pointss, arcade.color.AERO_BLUE)
"""
pointsss = [((SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) + 215),
            ((SCREEN_WIDTH / 2) + 200, (SCREEN_HEIGHT / 2) + 215),
            ((SCREEN_WIDTH / 2) + 200, (SCREEN_HEIGHT / 2) - 250),
            ((SCREEN_WIDTH / 2) - 250, (SCREEN_HEIGHT / 2) - 250)]
arcade.draw.draw_polygon_outline(pointsss, arcade.color.BLACK, 5)

# TEXT

affichage = arcade.Text("Robin Bird", 20, SCREEN_HEIGHT - 40, arcade.color.BLACK_OLIVE, 20, font_name="Times New Roman")
affichage.draw()




arcade.finish_render()  #  - Finish ↕
arcade.run()  #  Makes whatever was in between those two.
