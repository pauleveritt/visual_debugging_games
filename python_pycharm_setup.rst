========================
Python and PyCharm Setup
========================

We're writing games in Python, so that means we need a Python setup.
In this section, we'll download and install Python 3.6, get PyCharm to
use for our coding, and create a project.

.. note::

    This tutorial focuses on Windows, but everything covered
    works fine on macOS and Linux as well.

Python
======

Installing Python on Windows is quite easy. Head to the
`Python download page <https://www.python.org/downloads/>`_
and follow the instructions to download Python 3.6.1 (or higher.)
During the install, make sure to click the checkbox on the first screen
to put Python in the Windows ``PATH``.

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/gZa6vvH8MUU"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>


PyCharm
=======

When you're writing code, you need a tool that helps you with your
Python. This tutorial uses the free and open source program called
`PyCharm Community Edition <https://www.jetbrains.com/pycharm/download/>`_.
PyCharm is an IDE (integrated development environment) and the Community
Edition has everything we need for writing a game and doing visual
debugging.

There's a lot to learn, but don't worry, we'll introduce it gradually.

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/SVBrw2__jrM"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

Project
=======

As PyCharm is launching, it will ask you to create a new *project*. Let's
make one called ``Arcade Tutorial``. Let's also make a
*virtual environment*. When working on projects in Python, you
often install *packages* which others have published. You don't want
packages for one project to conflict with another. Virtual environments
give this kind of isolation.

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/EVWx7cYXPi4"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

- On the ``Welcome to PyCharm`` screen, click ``Create a New Project``.

- In the ``New Project`` dialog, store your project as ``arcade_project``.

- Also, click the ``...`` at the end of the ``Interpreter`` line and choose
  ``Create VirtualEnv``.

- On the ``Create Virtual Environment`` screen, make a new virtual
  environment based on the Python 3.6 that you installed above. The
  ``Location`` can be anywhere, e.g. a ``.virtualenvs`` directory in your
  home directory. Then click ``Ok``.

- Back on the new project dialog, click ``Create``.
