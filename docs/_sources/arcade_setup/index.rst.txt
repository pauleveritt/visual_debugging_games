============
Arcade Setup
============

Nothing is more frustrating than trying to start, only to find you aren't
setup correctly. Let's write a tiny program to ensure that:

- Arcade is installed correctly, and...

- PyCharm can run our small Python program

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/d3NxblctHJI"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

Objectives
==========

- Install Arcade

- Run a simple non-Arcade program

Steps
=====

#. *Project*. Make sure you have the ``arcade_tutorial`` project open in
   PyCharm.

#. *New file*. In the PyCharm menu, choose ``File -> New -> Python File``,
   then name file ``game.py``.

#. *Code*. In the new file contents, enter the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:

#. *Run*. On line 9, in the left gutter, click the green run arrow |run| and
   choose ``Run 'game'``.

#. *Error*. A panel should appear at the bottom with an error message -- we
   haven't installed ``arcade`` yet into this virtual environment!

#. *Install*. Click on the red-squigly line for ``arcade`` on line one, then
   click on the red light bulb that pops up. Choose the
   ``Install package arcade`` menu item.

#. *Run*. Once installed, click the green play button |run| (either on line 9
   or in the ``Run`` tool window) to re-run our program.

#. *Output*. You now see, in the ``Run`` window, the version number.

What's Going On
===============

In this step we ran a Python program. Cool! We used the Python that we
setup as the virtual environment for this project, then created a new file
called ``game.py`` and told that Python to run the file.

Actually, we told *PyCharm* to tell Python to run it, then PyCharm helped
along the way. For example, the output went to a nice output window.

But we had a problem the first time: the Arcade library isn't installed.
PyCharm offered to install this Python package into this project's
virtual environment.

.. |run| image:: ../images/run.png
