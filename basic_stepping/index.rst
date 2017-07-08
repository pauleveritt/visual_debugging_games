==========================
Basic Stepping and Players
==========================

TODO Ensure that every step ends with, and starts with, "Terminate"

Objectives
==========

- Step over, into, and out of code

Steps
=====

#. Stop the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 3-4, 7-8, 15, 16-18, 20, 22, 25

   - *Lines 3-4*. Let's start defining some game-wide constants.

   - *Line 7-8*. We are going to start defining a "player", using the
     sprite base class.

   - *Line 15*. Note that we removed the initialization of ``self.title``
     and ``self.position``.

   - *Lines 16-18*. Make an instance of our Player sprite, initialize our
     little database of sprites, and add the player to it.

   - *Line 20*. Our ``on_draw`` is no longer interested in f-strings and
     putting a label of text on the screen.

   - *Line 22*. When Arcade wants to draw/redraw, have it draw all of our
     sprites.

   - *Line 25*. Later we'll have our sprites do some updating of their
     positions.

#. *Image*. Download this image and save it as ``player.png`` beside the
   ``game.py`` file:

   .. image:: player.png

#. *First breakpoint*. Put a breakpoint on line 35, the ``main()`` call
   in the main block.

#. *Debug*. Click the green button |debug| to start debugging the game.

#. *Step Into*. Click the |stepinto| button to move execution into the
   calling of ``main``.

#. *Step Over*. Click the |stepover| button twice, moving through and
   out of ``main``.

#. Click the red terminate button |terminate| to kill the program.

We just stopped at a breakpoint, stepped *into* the main function, and
then stepped through some code until execution continued past our
breakpoint. This time, let's step into our game.

#. *Re-run*. Click the green |debug| button to debug and stop at the
   same breakpoint.

#. *Step Into*. Click the step into |stepinto| button to move to line
   29, then click |stepinto| *again* to move into the ``MyGame``
   constructor. You should now be on line 13 (``super()``).

#. *Step Into*. Click |stepinto| one more time. This opens a new file,
   Arcade's ``application.py``, which as the superclass which we just
   called.

#. *Terminate*. Click |terminate| to quit the program.

#. *Close tab*. Close the ``application.py`` tab.

What's Going On
===============

.. |rerun| image:: ../images/stop_and_rerun.png
.. |debug| image:: ../images/debug.png
.. |stepinto| image:: ../images/frames_step_into.png
.. |stepover| image:: ../images/frames_step_over.png
.. |terminate| image:: ../images/stop.gif
.. |breakpoint| image:: ../images/db_set_breakpoint.png