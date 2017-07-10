=========================================================
Debugging During Testing and Moving Coins with Collisions
=========================================================

- Moving coins

- Collisions

Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 13-15, 17-20, 52, 57, 67-70

   - *Lines 17-20*. The regular sprite ``update`` function, called whenever
     the game's ``on_draw`` says to update (line 63). Here we move the coin
     down a pixel. Then, if it reaches the bottom, "respawn" by calling
     its ``reset_pos`` method.

   - *Lines 13-15*. Move this coin somewhere near the top and randomly
     positioned left/right.

   - *Line 52*. As we see next, we also want to keep a sprite list of just
     for coins.

   - *Line 57*. Add this coin to the coin list.

   - *Lines 67-68*. Arcade makes it easy to find which sprites overlap with
     a certain sprite. ``hit_list`` is thus, which coins collided with the
     player.

   - *Lines 69-70*. Kill each of the colliding coins.


What's Going On
===============
