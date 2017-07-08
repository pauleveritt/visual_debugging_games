=======================
Consoles and Bounciness
=======================

- Bounciness


Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 9, 29-30

   - *Line 9*. Add a constant to control how much to "bounce" when
     hitting the bottom.

   - *Lines 29-30*. If you go past the bottom, apply some bounciness to
     the Y position until your change in Y reaches 0.



What's Going On
===============
