import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)

        self.player = Player('../images/player.png', 0.5)
        self.player.center_y = 50
        self.all_sprites_list = arcade.SpriteList()
        self.all_sprites_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()

    def update(self, delta_time):
        self.all_sprites_list.update()
        self.player.change_x = MOVEMENT_SPEED


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Coin Game')
    arcade.run()
    return game


if __name__ == '__main__':
    main()
