=====================================
Conditional Breakpoints and Animation
=====================================


Game:

- Set an initial position

- Change the string being displayed

- Implement animation via Arcade's ``update`` method

Objectives
==========

- Conditional breakpoints

- Suspend all breakpoints

- Clear all breakpoints

- Break on exceptions

Steps
=====

#. Edit ``game.py`` to have the following:s

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 9, 13-15, 17-18

   - *Line 9*. We will constantly update the position of the label, so
     let's initialize it with a starting position.

   - *Line 13*. Center the text on the screen height.

   - *Line 14-15*. Use Python 3.6 f-strings to make a label and draw it to
     the middle of the screen. Note that this is going to change every time
     line 18 updates the position.

   - *Line 18*. Move the position one pixel to the right. This gets called
     "a lot" by Arcade (where "a lot" can be configured.) ``delta_time`` is
     how long it has been since ``update`` was last called.

#. *Run under debugger*. Make sure there are no breakpoints and click the
   green button (either on line 27 or in the debug window) to run it
   under the debugger, just to see what it looks like.

#. *Set first breakpoint*. Investigate the delta_time.

#. *Set conditional breakpoint*.

#. *Shut up the breakpoints*.

#. *Clear all the breakpoints*.

#. *Stop on exceptions*. Generate a problem by draw_text with ``y``
   where ``message`` is.

What's Going On
===============
