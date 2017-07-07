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

#. Click the green arrow on line 9 (the ``if __name__`` line) and choose
   ``Debug``.

#. A new window appears. It's our "game"!

#. Close the Arcade window.

#. Click the green arrow again and choose ``Debug`` again.

#. This time, kill the debugging session by clicking the red square in
   the left of the ``Debug`` window. *Note: If it turns into a skull, that
   means the process isn't really dead yet, so click it again.*

What's Going On
===============

- What it means to run under the debugger

- Cython speedups

- pyglet window in another window