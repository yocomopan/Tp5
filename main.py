"""
2026-02-18
Ivan Zheryakov
Arcade TP5 theorie

Lien de l'image:
https://hips.hearstapps.com/hmg-prod/images
/american-robin-adult-male-in-grass-royalty-free-image-1755043928.pjpeg?crop=0.669
xw:1.00xh;0.265xw,0&resize=980:*

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
        self.coordinate_text = arcade.Text(f"()", 0, 0)

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes need to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # LEGS
        arcade.draw.draw_line(667, 156,
                              681, 83,
                              arcade.color.ANTIQUE_BRONZE, 20)  # 1

        arcade.draw.draw_line(560, 160,
                              579, 86,
                              arcade.color.BATTLESHIP_GREY, 25)  # 2

        arcade.draw.draw_line(550, 187,
                              564, 148,
                              arcade.color.ANTIQUE_BRONZE, 30)  # 2

        arcade.draw.draw_line(667 + 6, 156 - 30,
                              681, 83,
                              arcade.color.BATTLESHIP_GREY, 20)  # 1

        # BIRD BODY AND TAIL
        arcade.draw.draw_arc_filled(
            499, 597,
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

        top_fill = arcade.rect.XYWH(
            512, 493,
            100, 135)
        bottom_fill = arcade.rect.XYWH(
            717, 175,
            100, 50)
        bottom_refill = arcade.rect.XYWH(
            720, 200,
            60, 100)

        arcade.draw_rect_filled(top_fill, arcade.color.BURNT_ORANGE)
        arcade.draw_rect_filled(bottom_fill, arcade.color.BURNT_ORANGE)
        arcade.draw_rect_filled(bottom_refill, arcade.color.ANTIQUE_BRONZE)

        bird_body = [
            (602, 321),
            (502, 536),
            (449, 536),
            (424, 584),
            (424, 622),
            (553, 622),
            (571, 552),
            (613, 473),
            (748, 313),
            (791, 281),
            (833, 227),
            (934, 137),
            (749, 149)]

        bird_tail = [
            (888, 175),
            (1080, 109),
            (1078, 91),
            (862, 145)]

        arcade.draw.draw_polygon_filled(bird_tail, arcade.color.ANTIQUE_BRONZE, )
        arcade.draw.draw_polygon_filled(bird_body, arcade.color.ANTIQUE_BRONZE, )

        arcade.draw.draw_arc_filled(
            780, 145,
            150, 85,
            arcade.color.DUTCH_WHITE,
            0, 180,
            tilt_angle=3)
        arcade.draw.draw_triangle_filled(
            855, 141,
            937, 138,
            840, 167,
            arcade.color.DUTCH_WHITE)

        # FEATHER PATTERN
        arcade.draw.draw_ellipse_filled(
            443, 461,
            20, 20,
            arcade.color.ORANGE_PEEL,
            tilt_angle=340, num_segments=5)
        arcade.draw.draw_ellipse_filled(
            471, 491,
            20, 20,
            arcade.color.ORANGE_PEEL,
            tilt_angle=50, num_segments=5)
        arcade.draw.draw_ellipse_outline(
            434, 417,
            50, 50,
            arcade.color.ORANGE_PEEL,
            border_width=3, num_segments=5, tilt_angle=10)
        arcade.draw.draw_ellipse_filled(
            427, 483,
            20, 20,
            arcade.color.ORANGE_PEEL,
            tilt_angle=140, num_segments=5)
        arcade.draw.draw_ellipse_filled(
            441, 415,
            30, 30,
            arcade.color.ORANGE_PEEL,
            tilt_angle=60, num_segments=5)
        arcade.draw.draw_ellipse_filled(
            472, 450,
            25, 25,
            arcade.color.ORANGE_PEEL,
            tilt_angle=90, num_segments=6)
        arcade.draw.draw_ellipse_outline(
            498, 476,
            20, 20,
            arcade.color.ORANGE_PEEL,
            tilt_angle=120, border_width=2, num_segments=6)
        arcade.draw.draw_ellipse_filled(
            497, 425,
            40, 40,
            arcade.color.ORANGE_PEEL,
            tilt_angle=140, num_segments=5)
        arcade.draw.draw_ellipse_outline(
            456, 360,
            80, 80,
            arcade.color.ORANGE_PEEL,
            tilt_angle=25, border_width=2, num_segments=5)
        arcade.draw.draw_ellipse_outline(
            462, 358,
            45, 45,
            arcade.color.ORANGE_PEEL,
            tilt_angle=25, border_width=4, num_segments=5)
        arcade.draw.draw_ellipse_filled(
            442, 380,
            20, 20,
            arcade.color.ORANGE_PEEL,
            tilt_angle=342, num_segments=6)

        # EYE
        arcade.draw.draw_circle_filled(486,
                                       610,
                                       15,
                                       arcade.color.BLACK)
        arcade.draw.draw_circle_outline(486,
                                        610,
                                        15,
                                        arcade.color.ARYLIDE_YELLOW)

        # BEAK
        arcade.draw.draw_triangle_filled(424, 622,
                                         424, 584,
                                         337, 620,
                                         arcade.color.YELLOW)
        arcade.draw.draw_triangle_filled(421, 610,
                                         462, 587,
                                         421, 585,
                                         arcade.color.YELLOW)

        # TEXT
        arcade.draw_point(10, WINDOW_HEIGHT - 30,
                          arcade.color.BLACK_OLIVE, size=10)
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
        self.coordinate_text = arcade.Text(f"({x},{y})", x, y)

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
