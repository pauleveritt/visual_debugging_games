============================
Enhanced Stepping and Motion
============================

We'll make the Player sprite move to the right, and stop at the right edge.
We will also see 3 important additions to our stepping toolset.

Objectives
==========

- Step out

- Run to cursor

- Only step through project code

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

#. *Re-run*. Click the green re-run button |rerun| to restart the game
   and break at line 38.

#. *Step into*. Click step into |stepinto| once to go into our
   ``__init__``, then once again. We're taken out of our project, into
   the ``__init__`` for Arcade's ``Window`` class.

#. *Close file and re-run*. Close the ``application.py`` and click
   re-run |rerun| to restart and stop on line 38.

#. *Step into my code*. This time, click step into my code |stepintomy|
   to step into ``MyGame.__init__``. Then click it a few more times. It
   doesn't leave code in your project and thus doesn't step into library
   code such as Arcade.

What's Going On
===============

As you move into and out of code, you'll need more productive ways to step.
Especially when you are chasing the same problem repeatedly. Clicking "step
over" a hundred times isn't a good option.

"Step out" is the first line of defense. You go into a function, looking for
evidence, and as soon as you have what you need, you step out.

"Run to cursor" is an oft-overlooked tip. Your eyes tell you exactly where
you'd like to jump to. Put your cursor there and let PyCharm handle how to
get there.

Finally, you'll frequently find that "step into" takes you out of your code,
into Python packages that you're not interested in investigating as part
of your debugging. "Step into my code" lets you use "step into" without
being taken down a rabbit hole.

.. |rerun| image:: ../images/stop_and_rerun.png
.. |debug| image:: ../images/debug.png
.. |stepintomy| image:: ../images/step_into_my_code.png
.. |stepinto| image:: ../images/frames_step_into.png
.. |stepover| image:: ../images/frames_step_over.png
.. |stepout| image:: ../images/frames_step_out.png
.. |runtocursor| image:: ../images/frames_run_to_cursor.png
.. |terminate| image:: ../images/stop.gif
.. |breakpoint| image:: ../images/db_set_breakpoint.png
.. |run| image:: ../images/run.png
