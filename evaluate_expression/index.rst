===============================
Evaluate Expression and Sprites
===============================

Our game involves a player collecting coins. In this step, we'll make a
new sprite for coins, and put them on the screen, randomly positioned.

We'll also show stopping at a breakpoint and typing in some Python as
part of debugging. We'll use PyCharm's "Evaluate Expression" popup window
which provides a friendly UI for playing with the Python interpreter.

Objectives
==========

- Dynamically evaluate expressions while debugging

Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 1, 11-12, 42-46

   - *Line 1*. We want a random x/y initial coin location, so import
     ``random.randrange``.

   - *Lines 11-12*. We need another kind of sprite. This class handles a
     coin, which later will move on the screen. For now, just a placeholder.

   - *Lines 42-46*. Make 20 coins and put them in a random x/y position,
     then append them to the ``all_sprites`` list.

#. *Download coin image*. Download this image and save it as ``coin.png``:

   .. image:: coin.png
      :scale: 50%

#. *Set breakpoint*. We're going to evaluate the length of the sprites array
   as we add coins. Set a breakpoint on line 43
   (``coin = Coin('coin.png', 0.2)``) as the place we'll do our investigation.

#. *Debug*. Click resume |debug| to start debugging our game. Execution stops
   on that line.

#. *Open Evaluate Expression*. Click on evaluate expression |evaluate| in
   the debug stepping toolbar. This opens the ``Evaluate Expression`` dialog.

#. *Enter expression to evaluate*. Type in ``len(self.all_sprites_list)``
   and press enter. In the ``Result`` output, you'll see ``1``.

#. *Resume*. Click the resume |resume| button to continue execution to the
   same breakpoint, but in the second trip through the loop.

#. *Re-evaluate*. Click the ``Evaluate`` button to re-evaluate the expression.
   The result should now be 2.

#. *Clear and terminate*. Clear your breakpoint and click terminate
   |terminate| to stop the program.

What's Going On
===============

Sometimes at a breakpoint we want to do more than just look at variables.
We might want to run a function, perform a method, do a comparison, or even
overwrite some local state. Evaluate Expression puts a nice UI on inputting
Python.

As you might have noticed, you have autocomplete available in the input
window for the expression. If you find a useful expression, a shortcut can
add the expression as a watch. This example, in fact, would have made a
better watch.

.. |debug| image:: ../images/debug.png
.. |evaluate| image:: ../images/variables_evaluate_expr.png
.. |terminate| image:: ../images/stop.gif
.. |resume| image:: ../images/debug_resume.png
