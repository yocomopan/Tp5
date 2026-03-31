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
import random

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
        # BACKGROUND

        r_equator = arcade.rect.XYWH(WINDOW_WIDTH / 2,
                                     WINDOW_HEIGHT / 2,
                                     WINDOW_WIDTH, 2)
        r_rotation = arcade.rect.XYWH(WINDOW_WIDTH / 2,
                                      WINDOW_HEIGHT / 2,
                                      2, WINDOW_HEIGHT)

        arcade.draw_rect_filled(r_equator, arcade.csscolor.BLACK)
        arcade.draw_rect_filled(r_rotation, arcade.csscolor.BLACK)

        # LEGS
        arcade.draw.draw_line(667, 156,
                              681, 83,
                              arcade.color.ANTIQUE_BRONZE, 20) # 1

        arcade.draw.draw_line(560, 160,
                              579, 86,
                              arcade.color.BATTLESHIP_GREY, 25) # 2

        arcade.draw.draw_line(550, 187,
                              564, 148,
                              arcade.color.ANTIQUE_BRONZE, 30) # 2

        arcade.draw.draw_line(667+6, 156-30,
                              681, 83,
                              arcade.color.BATTLESHIP_GREY, 20) # 1
        # GRASS
        def randomness(gg, gh, cc):
            grass_height = random.randint(10, 147)
            grass_growth = random.randint(-5, 5)
            color_list = [arcade.color.OLD_MOSS_GREEN, arcade.color.FOREST_GREEN, arcade.color.ANDROID_GREEN]


        distance = 0
        toodistance = -6
        color_list = [arcade.color.OLD_MOSS_GREEN, arcade.color.FOREST_GREEN, arcade.color.ANDROID_GREEN]
        for i in range(10):
            arcade.draw.draw_line(distance ,0,distance
                                  randomness(gg),randomness(gh) ,
                                  randomness(cc), 10)


        # un_tuple = (23, True , ["a", "b"])

        # Bird Body

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

        arcade.draw.draw_polygon_outline(pointsss, arcade.color.BLACK, 5)
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
        # EYE
        arcade.draw.draw_circle_filled(486,
                                       610,
                                       15,
                                       arcade.color.BLACK)
        arcade.draw.draw_circle_outline(486,
                                        610,
                                        15,
                                        arcade.color.ARYLIDE_YELLOW)

        # Beak

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