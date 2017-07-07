from random import randrange, choice

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
GRAVITY = 0.3
BOUNCINESS = 0.5


class Coin(arcade.Sprite):
    def reset_pos(self):
        self.center_y = randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class Player(arcade.Sprite):
    def update(self):
        self.change_y -= GRAVITY
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
            if self.change_y < 0:
                self.change_y *= -BOUNCINESS
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)

        self.player = Player('player.png', 0.5)
        self.player.center_y = 20
        self.all_sprites_list = arcade.SpriteList()
        self.all_sprites_list.append(self.player)

        self.coins = arcade.SpriteList()
        for i in range(20):
            coin = Coin('coin.png', 0.2)
            coin.center_x = randrange(SCREEN_WIDTH)
            coin.center_y = randrange(SCREEN_HEIGHT)
            self.coins.append(coin)
            self.all_sprites_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()

    def update(self, delta_time):
        self.all_sprites_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player,
                                                        self.coins)
        for coin in hit_list:
            coin.kill()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            pass
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Coin Game')
    arcade.run()
    return game


if __name__ == '__main__':
    main()
