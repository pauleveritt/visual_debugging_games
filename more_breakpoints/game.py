import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)
        self.width = width
        self.height = height
        self.title = title

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Hello World', 100, 400, arcade.color.BLACK)


def main():
    game = MyGame(600, 600, 'Coin Game')
    arcade.run()
    return game


if __name__ == '__main__':
    main()
