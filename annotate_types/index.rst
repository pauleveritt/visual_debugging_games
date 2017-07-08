=========================
Annotate Types and Scores
=========================

- Display score

Steps
=====

#. Stop the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 60, 65-66, 75

   - *Line 60*. We're keeping score, so start at zero.

   - *Lines 65-66*. Display the current score, during ``on_draw``, using
     a Python 3.5 f-string.

   - *Line 75*. Whenever you kill a coin, increase the score.


What's Going On
===============
