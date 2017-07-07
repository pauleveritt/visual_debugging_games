==================================
First Breakpoints and Drawing Text
==================================

We ran under the debugger. But we didn't do any debugging. Let's set a
breakpoint to stop execution at a certain place, allowing us to
investigate.

Objectives
==========

- Stop execution at a *breakpoint*

- Resume execution past the breakpoint

Steps
=====

#. Edit ``game.py`` to have the following:s

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 6-10

   - *Line 6*. Set the window's background color using a friendly constant
     defined in Arcade.

   - *Lines 7, 9, 10*. Tell Arcade where are the rendering boundaries, then
     run the graphics main loop.

   - *Line 8*. Draw some text on the screen at the 100,400 position.

#. *Line numbers*. If line numbers are visible, right click in the "gutter"
   to the left of the the code and choose ``Show Line Number``.

#. *Set breakpoint*. Click in the gutter area to the left of line 8, causing
   a red circle to appear. This is called a *breakpoint*.

#. *Debug*. Click the green play button on line 13 and choose ``Debug``.

#. *Inspect variables*. Python execution stops at the line with the breakpoint
   and shows you the available variables in the debugger. Nothing is in scope,
   so no variables.

#. *Resume Program*. Continue execution past the breakpoint by clicking the
   green "moving" arrow in the debug panel. When you mouseover, it will say
   ``Resume Program``.

#. *Exit*. Quit the program, either by closing the Arcade window or by
   clicking the red square in the debugger.

What's Going On
===============

- What are the arguments? Mouse over and quick preview

- Experiment with defining a variable before the breakpoint