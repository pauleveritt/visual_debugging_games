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

#. *Debug at breakpoint*. Set a breakpoint on line 30
   (``self.change_y *= -BOUNCINESS``) and click |debug| to restart the
   game under the debugger. Execution stops at that line.

#. *Switch to console*. The debugger tool window is on the ``Debugger`` tool
   tab. Click the other tab, labelled ``Console``, to open the console tab.

#. *Show Python Prompt*. Click the show Python prompt button |prompt| in the
   debugger console tool window.

#. *Enter expression*. Type in ``self.change_y`` and press enter to get the
   value at that line of execution. This means we are moving down.

#. *Press up then down arrows*. The console has history, which you can access
   with the up/down arrows.

#. *Get the multiple*. Enter ``self.change_y * -BOUNCINESS`` to see what would
   be the value of the assignment on that line. We would bounce up.

#. *Resume*. Click the resume button |resume| a few times.

#. *Look at new value*. Press up arrow twice to see ``self.change_y`` and
   its new value.

PyCharm's console is useful, but ``ipython`` is much more featured. We can
use it by simply installing the package. If present in the virtual
environment, PyCharm will use it.

#. *Open settings/preferences*. ``Ctrl+Alt+S`` on Windows, ``Cmd-,`` on
   macOS.

#. *Interpreter*. Go to ``Project | Project Interpreter``.

#. *Install package*. Click the ``+`` then type in ``ipython``. Click
   ``Install Package``. When done, dismiss the dialog and click ``OK`` to
   close settings/preferences.

#. *Rerun*. Click the debugger's re-run button |rerun|.

#. *Prompt*. Click the ``Console`` tab again, and click the show Python
   prompt button |prompt|.

#. *Use ipython*. Note that the prompt is now ``In[1]:`` which is the
   ipython prompt.

#. *Clear and terminate*. Clear your breakpoint and click the terminate
   button |terminate|.

What's Going On
===============

In the previous section, we did interactive Python at a breakpoint by
using the ``Evaluate Expression`` dialog. Some people prefer the familiar
Python prompt, which PyCharm can give you under the "Console" tab where
we send the stdout for the program being debugged.

While PyCharm's built-in prompt has the basic features, ``ipython`` is very
advanced and actively developed. Experienced developers are used to it, so
PyCharm supports it (both here in the debugger and in the Python Console
tab.)

.. |debug| image:: ../images/debug.png
.. |prompt| image:: ../images/icon_showCommandLine.png
.. |rerun| image:: ../images/stop_and_rerun.png
.. |resume| image:: ../images/debug_resume.png
.. |terminate| image:: ../images/stop.gif
