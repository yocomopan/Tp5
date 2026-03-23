"""
2026-02-18
Ivan Zheryakov
Arcade TP5 theorie


Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.LIMERICK

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.coordinate_text = arcade.Text(f"()",0,0)

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        """
        arcade.draw.draw_ellipse_filled(550,
                                        350,
                                        300,
                                        400,
                                        arcade.color.BURNT_ORANGE,
                                        tilt_angle=340, num_segments=100)
        """


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

        r_equator = arcade.rect.XYWH(WINDOW_WIDTH / 2,
                                     WINDOW_HEIGHT / 2,
                                     WINDOW_WIDTH, 2)
        r_rotation = arcade.rect.XYWH(WINDOW_WIDTH / 2,
                                      WINDOW_HEIGHT / 2,
                                      2, WINDOW_HEIGHT)

        arcade.draw_rect_filled(r_equator, arcade.csscolor.BLACK)
        arcade.draw_rect_filled(r_rotation, arcade.csscolor.BLACK)


        # TRIANGLE


        arcade.draw.draw_triangle_filled(424,622, 424,584,337, 620, arcade.color.YELLOW)

        # LIGNE
        """
        arcade.draw.draw_line(WINDOW_WIDTH - 250, WINDOW_HEIGHT - 110,
                              WINDOW_WIDTH, WINDOW_HEIGHT - 110,
                              arcade.color.BANANA_YELLOW, 10)

        points = [(700, 300), (750, 600), (345, 675)]
        arcade.draw.draw_line_strip(points, arcade.color.BUFF)

        un_tuple = (23, True , ["a", "b"])

        points = [(700, 300), (750, 600), (345, 675)]

        line_list = [(139, 556), (720, 512), (773, 704), (710, 596)]
        arcade.draw.draw_lines(line_list, arcade.color.FOREST_GREEN)
        """

        # ARC

        arcade.draw.draw_arc_filled(499, 597,
                                    157, 96,
                                    arcade.color.ANTIQUE_BRONZE,
                                    0, 180,
                                    tilt_angle=19)
        arcade.draw.draw_arc_filled(
            599, 360,
            460, 350,
            arcade.color.BURNT_ORANGE,
            0, 180,
            tilt_angle=235)

        # RECTANGLE
        top_fill = arcade.rect.XYWH(
            512, 493,
            90, 135)
        bottom_fill = arcade.rect.XYWH(
            717, 175,
            100, 50)
        arcade.draw_rect_filled(top_fill, arcade.color.BURNT_ORANGE)
        arcade.draw_rect_filled(bottom_fill, arcade.color.BURNT_ORANGE)

        # POLYGONE

        pointsss = [((WINDOW_WIDTH / 2) - 350, (WINDOW_HEIGHT / 2) + 315),
                    ((WINDOW_WIDTH / 2) + 300, (WINDOW_HEIGHT / 2) + 315),
                    ((WINDOW_WIDTH / 2) + 300, (WINDOW_HEIGHT / 2) - 350),
                    ((WINDOW_WIDTH / 2) - 350, (WINDOW_HEIGHT / 2) - 350)]
        bird_body = [
            (602, 321),
            (502, 536),
            (449, 536),
            (424, 584),
            (424, 622),
            (553, 622),
            (571, 552),
            (613, 473),
            (748, 303),
            (934, 137),
            (749, 149)]
        arcade.draw.draw_polygon_outline(pointsss, arcade.color.BLACK, 5)
        arcade.draw.draw_polygon_filled(bird_body, arcade.color.ANTIQUE_BRONZE,)



        # TEXT

        affichage = arcade.Text("Robin Bird",
                                20, WINDOW_HEIGHT - 40,
                                arcade.color.BLACK_OLIVE,
                                20, font_name="Times New Roman")
        affichage.draw()
        self.coordinate_text.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.coordinate_text = arcade.Text(f"({x},{y})",x,y)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()



#
# import arcade
# from arcade import open_window
#
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# WINDOW_TITLE = "Tutoriel Arcade"
#
#
# def main():
#     arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Tutoriel Arcade")
#
#
# arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
# arcade.set_background_color(arcade.color.LIMERICK)
# arcade.start_render()  # + Start ↕
# # ELLIPSE
#
# arcade.draw.draw_ellipse_filled(400,
#                                 300,
#                                 500,
#                                 300,
#                                 arcade.color.ANTIQUE_BRONZE,
#                                 tilt_angle=50, num_segments=5)
#
# # RECTANGLE
#
#
# # CIRCLE
# """
# arcade.draw.draw_circle_outline(200,
#                                 200,
#                                 60,
#                                 arcade.color.BUBBLE_GUM,
#                                 num_segments=8, tilt_angle=35)
# arcade.draw.draw_circle_filled(400,
#                                 200,
#                                 60,
#                                 arcade.color.BUBBLE_GUM
#                                 , num_segments=8)
# """
# # RECTANGLE FOREST
#
# r_equator = arcade.rect.XYWH(WINDOW_WIDTH / 2,
#                              WINDOW_HEIGHT / 2,
#                              WINDOW_WIDTH, 2)
# r_rotation = arcade.rect.XYWH(WINDOW_WIDTH / 2,
#                               WINDOW_HEIGHT / 2,
#                               2, WINDOW_HEIGHT)
#
# arcade.draw_rect_filled(r_equator,arcade.csscolor.BLACK)
# arcade.draw_rect_filled(r_rotation, arcade.csscolor.BLACK)
#
# # ARC
# """
# arcade.draw.draw_arc_filled(200, WINDOW_HEIGHT / 2 + 20,
#                             60, 100,
#                             arcade.csscolor.FOREST_GREEN,
#                             0, 180)
#
# arcade.draw.draw_arc_filled(250, 245,
#                             60, 93,
#                             arcade.csscolor.FOREST_GREEN,
#                             0, 180)
#
# arcade.draw.draw_arc_filled(300, 270,
#                             60, 86,
#                             arcade.csscolor.FOREST_GREEN,
#                             0, 180)
#
# arcade.draw.draw_arc_filled(350, 245,
#                             58, 80,
#                             arcade.csscolor.FOREST_GREEN,
#                             0, 180)
#
# arcade.draw.draw_arc_filled(400, 290,
#                             40, 29,
#                             arcade.csscolor.DARK_RED,
#                             0, 180)
# """
# # TRIANGLE
# """
# y = WINDOW_HEIGHT / 2 + 40
# arcade.draw.draw_triangle_filled(500, y + 40,
#                            470, y - 20,
#                            530, y - 20,
#                            arcade.color.FOREST_GREEN)
# """
# # LIGNE
# """
# arcade.draw.draw_line(WINDOW_WIDTH - 250, WINDOW_HEIGHT - 110,
#                       WINDOW_WIDTH, WINDOW_HEIGHT - 110,
#                       arcade.color.BANANA_YELLOW, 10)
#
# points = [(700, 300), (750, 600), (345, 675)]
# arcade.draw.draw_line_strip(points, arcade.color.BUFF)
#
# un_tuple = (23, True , ["a", "b"])
#
# points = [(700, 300), (750, 600), (345, 675)]
#
# line_list = [(139, 556), (720, 512), (773, 704), (710, 596)]
# arcade.draw.draw_lines(line_list, arcade.color.FOREST_GREEN)
# """
# # POLYGONE
# """
# pointss = [(700, 300), (750, 600), (345, 675)]
# arcade.draw.draw_polygon_filled(pointss, arcade.color.AERO_BLUE)
# """
# pointsss = [((WINDOW_WIDTH / 2) - 250, (WINDOW_HEIGHT / 2) + 215),
#             ((WINDOW_WIDTH / 2) + 200, (WINDOW_HEIGHT / 2) + 215),
#             ((WINDOW_WIDTH / 2) + 200, (WINDOW_HEIGHT / 2) - 250),
#             ((WINDOW_WIDTH / 2) - 250, (WINDOW_HEIGHT / 2) - 250)]
# bird_body = [((0), (0)),
#             ((240), (400)),
#             ((), (500)),
#             ((100), (500))]
# arcade.draw.draw_polygon_outline(pointsss, arcade.color.BLACK, 5)
# arcade.draw.draw_polygon_outline(bird_body, arcade.color.ANTIQUE_RUBY, 5)
#
# # TEXT
#
# affichage = arcade.Text("Robin Bird", 20, WINDOW_HEIGHT - 40, arcade.color.BLACK_OLIVE, 20, font_name="Times New Roman")
# affichage.draw()
#
#
#
#
# arcade.finish_render()  #  - Finish ↕
# arcade.run()  #  Makes whatever was in between those two.
