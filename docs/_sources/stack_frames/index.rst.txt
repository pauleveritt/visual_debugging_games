==================================
Stack Frames and Vertical Movement
==================================

Our player can move side to side. We'd like to move the player up, then
have gravity pull the player back down.

As part of developing this, we'll show how to debugger can move us between
stack frames in the execution.

Objectives
==========

- Show moving between the stack frames when stopped at a breakpoint

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

#. *Play the game*. Click the debug button |debug| to run the game. Move
   the player left and right, then press up to move up. Press several
   times quickly to up further.

#. *Set breakpoint*. Set a breakpoint on line 61 (``game = MyGame``).

#. *Re-run*. Click the re-run button |rerun| to start execution from the
   beginning. Execution stops inside the ``main()`` function.

#. *Stack frame*. Look at the ``Frames`` panel in the left side of the
   debug window. It shows two non-ghosted lines: ``<module>`` and
   ``main``. Click on the ``<module>`` line to change to that frame.
   Note the change of variables to show what is now in scope.

#. *Step into*. Click the step into button |stepinto|. You are now on
   line 28, and in a new frame (``__init__``). You now have new variables
   in scope.

#. *Clear breakpoint and terminate*. Click the red circle |breakpoint| to
   clear it, then click |terminate| to stop the game.

What's Going On
===============

As your program executes, you might jump into a function, or into the
constructor for a class. In Python, each of these jumps creates a "stack
frame" which holds all the information at that point before you jump. That
way, when you return, all your variables have the right data.

When you are debugging, you might ask: "How did I get to this breakpoint?"
This is especially true when something else called the code at the
breakpoint. Perhaps you have "stop at exception turned on" and you weren't
the one tracing the path to the breakpoint. Or, as in Arcade, something else
is calling your code (e.g. ``on_draw``).

The debugger makes it easy to move forwards and backwards through
stack frames on the "call stack", inspecting data as you move.

Note though that some operations (e.g. watches) might not be meaningful in
other stack frames. You might watch the value of ``len(self.title)`` but
if there is no ``self.title`` in another stack frame, the watch will not
show anything.

.. |rerun| image:: ../images/stop_and_rerun.png
.. |debug| image:: ../images/debug.png
.. |new| image:: ../images/new.png
.. |delete| image:: ../images/delete.png
.. |stepinto| image:: ../images/frames_step_into.png
.. |terminate| image:: ../images/stop.gif
.. |breakpoint| image:: ../images/db_set_breakpoint.png