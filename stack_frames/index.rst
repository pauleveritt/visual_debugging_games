==================================
Stack Frames and Vertical Movement
==================================

- Handling the up key

- Gravity

Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 6, 11, 13, 20-23, 46

   - *Line 6*. We are introducing the concept of gravity, a constant that
     will affect vertical motion.

   - *Line 11*. If there is a change in the Y position, apply gravity to
     it, meaning, decrease the amount of Y movement.

   - *Line 13*. Just like for x, we need to handle changes to y. If the
     sprite is assigned a change to y, then move the y location of the
     player.

   - *Lines 20-23*. Same as for left/right boundaries. If we hit the
     bottom, reset to 0. If we hit the top, reset to one less than the
     height of the screen.

   - *Line 46*. If the up arrow is pressed, assign the player's
     ``change_y`` value based on the "speed".

- You can press up multiple times

What's Going On
===============
