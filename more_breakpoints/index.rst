======================================
More Breakpoints and Class-Based Games
======================================

Our "game" opened a window. But Arcade games are usually classes that
implement methods to handle the important parts of games. Let's convert
our Arcade program into a call with an ``on_draw`` function that puts
stuff on the screen.

We'll also look at two more parts of breakpoints. You can change your
breakpoints to different lines, without needed to restart your program. You
can also browse around in the variables, plus see variables inline.

Objectives
==========

- Explore variables at a breakpoint

- Move breakpoints without restarting

Steps
=====

#. Terminate the game, if it is running.

#. Edit ``game.py`` to have the following:

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

#. *Clear breakpoint*. If you still have a red circle |breakpoint|
   from the previous step, click on it to remove the breakpoint.

#. *Break in the constructor*. Click in the gutter on line 8
   (``self.title``) to set a breakpoint |breakpoint| on that line.

#. *Re-run debugger*. In the Debug window, click the green bug
   |debug| to restart the debugger.

#. *Inspect variables*. Execution stops in the ``MyGame`` constructor. You
   can see that ``title``, ``self``, and more are defined. Click the
   triangle beside ``self`` to see the attributes on the instance.

#. *Inline variables*. You can also see that, at a breakpoint, PyCharm will
   show variable values as if they were comments in your code. In our case,
   line 5 (``def __init__``) shows the inline values.

#. *Resume Program*. Click the "moving" green arrow |resume| in the
   debug window to resume execution. It is past the one break point,
   so everything is running as normal.

#. *Set second breakpoint*. Click in the left gutter beside line 12
   (``arcade.draw_text``). Execution stops, on that line. Now, only
   ``self`` is in scope.

#. *Resume Program*. Click |resume| to resume execution. It stops
   immediately again.

#. *Clear and resume*. Click the red circle |breakpoint| beside line 12
   to clear that breakpoint. Then, click the moving green arrow |resume|
   to resume execution. This time, it doesn't stop for execution.

#. *Close the game*. Either close the Arcade window or click the red square
   |terminate| to terminate execution.

What's Going On
===============

We ran under the debugger, we set a breakpoint, and we viewed some values.
Great!

When we set the second breakpoint, execution immediately stopped. But not
at the first breakpoint. Why? Because Python had already gone past that
line in our program. If we re-ran our program, that line of startup code
would be executed and we'd stop at that breakpoint.

The second breakpoint worked without restarting the application. That's
because Arcade is constantly calling ``on_draw``. Thus, as soon as we
set our breakpoint, Arcade called ``on_draw`` and execution stopped at
that breakpoint.

As an experiment, you could prove that ``on_draw`` was being called
repeatedly by appending ``str(time.time())`` to the label displayed in
Arcade.

.. |breakpoint| image:: ../images/db_set_breakpoint.png
.. |resume| image:: ../images/debug_resume.png
.. |debug| image:: ../images/debug.png
.. |terminate| image:: ../images/stop.gif
