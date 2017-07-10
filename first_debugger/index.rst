=================================
First Debugger and Arcade Windows
=================================

Let's start writing our game by opening a window. Along the way,
we'll have our first debugger experience.

Objectives
==========

- Run a program under the debugger, instead of directly in Python

- Open a game window with a title and correct size

Steps
=====

#. Change the main block to call a ``main`` function which uses Arcade
   to open a window:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 4-6, 10

   - *Lines 4-6*. Create a main function that draws a window and runs
     the Arcade main loop.

   - *Line 10*. Change the main block to call this main function.

#. *Debug*. Click the green arrow |run| on line 9 (the ``if __name__``
   line) and choose ``Debug 'game'``.

   .. note::

     If you are on macOS or Linux, you might get a prompt to
     install "Cython" extensions. If so...click the link. You'll get
     tremendous speedups for debugging.

#. A new window appears. It's our "game"!

#. *Close*. Close the Arcade window.

#. *Re-run*. Click the green arrow again and choose ``Debug`` again.

#. *Terminate*. This time, kill the debugging session by clicking the red
   square |terminate| in the left of the ``Debug`` window.

   .. note::

      If the terminate button |terminate| turns into a skull, that means
      the process isn't really dead yet, so click it again.

What's Going On
===============

We run a program using the debugger. What specifically does that mean?

PyCharm using a tool called
`pydevd <https://pypi.python.org/pypi/pydevd>`_ which manages the running
of code. PyCharm talks to ``pydevd`` which talks to your code, as part of
"debugging".

What's up with the Cython part? The ``pydevd`` project provides compiled
extensions for some of the bottlenecks involved in debugging. PyCharm
provides the pre-compiled extensions on Windows, but not on macOS and Linux.
Once compiled for a specific interpreter version, these can be used across
your PyCharm projects.

Just like there are many ways to run your Python code in PyCharm, there are
also many ways to start debugging. In recent versions of PyCharm, we put an
arrow in the gutter beside a module's main block.

To finish debugging this game, we can either close the window normally, or
tell the debugger to "terminate" the Python process. We will use the latter
in most places of the tutorial, to prevent switching windows.

.. |run| image:: ../images/run.png
.. |terminate| image:: ../images/stop.gif
