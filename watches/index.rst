======================
Watches and Keypresses
======================

Instead of moving on its own, our player will move right/left only when
we press the right/left arrow key.

- keypress handling to change left/right

- keyhold to move, keyrelease to stop

- For now, skip "up" (will be bounciness later)

Objectives
==========

- Use a dynamic watch to simplify tracking variables

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

#. *Add a watch*. Click the ``New Watch`` button |new| directly under
   ``Variables``, in the left column beside the variable display. In
   PyCharm versions after 2017.1, this is a green plus with watch
   glasses underneath. Enter ``key === arcade.key.UP`` as the watch
   value.

#. *Set a breakpoint*. We want to stop on keypresses and quickly see
   if it is the up arrow. Put a breakpoint on line 37
   (``if key == arcade.key.UP``).

#. *Re-run*. Click the re-run button |rerun| to run again under
   the debugger.

#. *Press a key*. As the game is playing, press a key. Execution stops.

#. *Inspect the watch*. The watch makes it easy to see if the comparison
   is true, instead of scrolling down and memorizing key codes.

#. *Delete watch*. Click once to select the "variable" that has the
   watch, then click the minus button |delete| to remove that watch.

#. *Clear breakpoint and terminate*. Click the breakpoint |breakpoint|
   to remove it, then click the red square |terminate| to stop the game.

What's Going On
===============

.. |rerun| image:: ../images/stop_and_rerun.png
.. |debug| image:: ../images/debug.png
.. |new| image:: ../images/new.png
.. |delete| image:: ../images/delete.png
.. |stepover| image:: ../images/frames_step_over.png
.. |terminate| image:: ../images/stop.gif
.. |breakpoint| image:: ../images/db_set_breakpoint.png