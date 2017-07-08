======================
Watches and Keypresses
======================

Instead of moving on its own, our player will move right/left only when
we press the right/left arrow key.

- keypress handling to change left/right

- keyhold to move, keyrelease to stop

- For now, skip "up" (will be bounciness later)


Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 33, 35-42, 44-49

   - *Line 33*. Get rid of moving the player automatically.

   - *Lines 35-42*. Handle key presses (pressing down). If it is the up
     key, ignore it for now. If left, then move a *negative* number of
     movement speed pixels to the left. For right, a positive number.

   - *Lines 44-49*. When the key is released, reset the ``change_x``
     value to 0, meaning, don't change the sprites x direction.


What's Going On
===============
