============================
Enhanced Stepping and Motion
============================

We'll make the Player sprite move to the right, and stop at the right edge.

Objectives
==========

- Step out

- Only step through project code

- Run to cursor

Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
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

#. *Close game*. Close the Arcade window to stop the game.

#. *First breakpoint*. Put a breakpoint on line 38 (``game = MyGame``).

#. *Debug game*. Click the debug button |debug| to run the game. It
   stops at that breakpoint.

#. *Step into*. Click the step into button |stepinto| to go into
   the ``MyGame`` constructor.

#. *Step out*. Click the step out button |stepout| to leave the code
   that you stepped into, and go back to the point that called it
   (line 38).

#. *Re-run*. Click the green re-run button |rerun| to restart the game
   and break at line 38.

#. *Run to cursor*. Click somewhere in line 26 (the ``append``) to put
   the cursor on that line. Now click the run to cursor button
   |runtocursor| to continue executing until you reach that line.
   Execution stops there, just as if that line had a breakpoint.


What's Going On
===============


.. |rerun| image:: ../images/stop_and_rerun.png
.. |debug| image:: ../images/debug.png
.. |stepinto| image:: ../images/frames_step_into.png
.. |stepover| image:: ../images/frames_step_over.png
.. |stepout| image:: ../images/frames_step_out.png
.. |runtocursor| image:: ../images/frames_run_to_cursor.png
.. |terminate| image:: ../images/stop.gif
.. |breakpoint| image:: ../images/db_set_breakpoint.png
.. |run| image:: ../images/run.png
