import arcade


def main():
    arcade.open_window(600, 600, 'Coin Game')
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()
    arcade.draw_text('Hello World', 100, 400, arcade.color.BLACK)
    arcade.finish_render()
    arcade.run()


if __name__ == '__main__':
    main()
