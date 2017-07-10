======================
Console and Bounciness
======================

We can press up (repeatedly) to move our player up, and with gravity,
the player comes back down. Wouldn't it be cool if, when the player hits
the bottom, they bounce a little?

Let's add bounciness and also show how to use a Python console at a
breakpoint.

Objectives
==========

- Use the Python Console at a breakpoint, including ipython

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

- *Debug at breakpoint*. Set a breakpoint on line 30
  (``self.change_y *= -BOUNCINESS``) and click |debug| to restart the
  game under the debugger. Execution stops at that line.



TODO

- We have a flaw. Shouldn't be less than zero at startup. Line 18.

- Click interactive console icon.

- Type in self.change_y

- Go to console, type in self.change_y * -BOUNCINESS

- Install ipython

- Rerun, go to console

What's Going On
===============

.. |debug| image:: ../images/debug.png
