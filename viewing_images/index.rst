==========================
Viewing Images and Sprites
==========================

- Sprites for the coins, randomly positioned

Steps
=====

#. Stop the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 1, 11-12, 42-46

   - *Line 1*. We want a random x/y initial coin location, so import
     ``random.randrange``.

   - *Lines 11-12*. We need another kind of sprite. This class handles a
     coin, which later will move on the screen. For now, just a placeholder.

   - *Lines 42-46*. Make 20 coins and put them in a random x/y position,
     then append them to the ``all_sprites`` list.


What's Going On
===============
