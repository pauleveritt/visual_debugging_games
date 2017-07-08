=======================================
Debugging During Testing and Collisions
=======================================

- Collisions

Steps
=====

#. Stop the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 52, 57, 67-70

   - *Line 52*. As we see next, we also want to keep a sprite list of just
     for coins.

   - *Line 57*. Add this coin to the coin list.

   - *Line 67-68*. Arcade makes it easy to find which sprites overlap with
     a certain sprite. ``hit_list`` is thus, which coins collided with the
     player.

   - *Line 69-70*. Kill each of the colliding coins.


What's Going On
===============
