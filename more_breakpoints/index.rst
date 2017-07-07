======================================
More Breakpoints and Class-Based Games
======================================

- Move to a class

- Move break point to different place without restarting

- Variable explorer and inline values

Objectives
==========

- Explore variables at a breakpoint

- Move breakpoints without restarting

Steps
=====

#. Edit ``game.py`` to have the following:s

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 4-12, 16, 18

   - *Line 4*. Arcade games are usually classes that fill in magic methods.
     Here we make a subclass of Arcade's ``Window`` base class.

   - *Lines 5-6*. Pass in window information, then give to the base class.

   - *Lines 10-12*. The magic method ``on_draw`` is called many times per
     second, to perform graphics operations.

   - *Line 16*. Make an instance of the game (then return it, in case you
     want to test the ``main`` function.)

#. *Clear breakpoint*. If you still have a red circle from the previous
   step, click on it to remove the breakpoint.

#. *Break in the constructor*. Click in the gutter on line 8
   (``self.title``) to set a breakpoint on that line.

#. *Re-run debugger*. In the Debug window, click the green circle with
   an arrow to restart the debugger.

#. *Inspect variables*. Execution stops in the ``MyGame`` constructor. You
   can see that ``title``, ``self``, and more are defined. Click the
   triangle beside ``self`` to see the attributes on the instance.

#. *Resume Program*. Click the "moving" green arrow in the debug window to
   resume the program. It is past the one break point, so everything is
   running as normal.

#. *Set second breakpoint*. Click in the left gutter beside line 12
   (``arcade.draw_text``). Execution stops, on that line. Now, only
   ``self`` is in scope.

#. *Resume Program*. Click the moving green arrow to resume execution. It
   stops immediately again.

#. *Clear and resume*. Click the red circle beside line 12 to clear that
   breakpoint. Then, click the moving green arrow to resume execution. This
   time, it doesn't stop for execution.

What's Going On
===============

- Why didn't the first breakpoint get triggered?

- Didn't need to restart when setting second breakpoint...why?

- How could you prove execution stopped? (str(time.time())