============================
Enhanced Stepping and Motion
============================

We'll make the Player sprite move to the right, and stop at the right edge.

Steps
=====

#. Stop the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 10-15, 24,  33-34

   - *Line 10*. Move the player, based on the value (possibly changed)
     of ``change_x``.

   - *Lines 12-15*. If we go past the edge, move the player back be
     on screen. This basically makes a left/right "edge".

   - *Line 24*. Let's start the player sprite a bit up from the bottom.

   - *Lines 33-34*. Every time Arcade updates (many times per second),
     re-draw the player and move it ``MOVEMENT_SPEED`` pixels to the left.

#. *Play the game*. Click the green debug button |debug| to run the game,
   with no breakpoints, to see it in action.



- Breakpoint in on_draw, raises exception, and...stops

- Same, but with bad image filename

- Disable python exception stopping

- Step into through __init__ goes into SptriteList, thus step through
  my code

- Run to cursor

What's Going On
===============


.. |rerun| image:: ../images/stop_and_rerun.png
.. |debug| image:: ../images/debug.png
.. |stepinto| image:: ../images/frames_step_into.png
.. |stepover| image:: ../images/frames_step_over.png
.. |terminate| image:: ../images/stop.gif
.. |breakpoint| image:: ../images/db_set_breakpoint.png