import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)
        self.title = title
        self.position = 100

    def on_draw(self):
        arcade.start_render()
        y = self.height / 2
        message = f'{self.title}: {self.position}'
        arcade.draw_text(message, self.position, y, arcade.color.BLACK, 12)

    def update(self, delta_time):
        self.position += 1


def main():
    game = MyGame(600, 600, 'Coin Game')
    arcade.run()
    return game


if __name__ == '__main__':
    main()
