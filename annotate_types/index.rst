=========================
Annotate Types and Scores
=========================

One last feature in our game: keeping score. As we collect coins, we should
get a point added to our score. Also, we should display a text label that
shows the score, which updates as the score increases.

Arcade deeply uses Python 3.5/3.6 type hinting, which is why it requires
Python 3.6. PyCharm can help you with adding type hinting, via the debugger.

.. warning::

  You have to explicitly turn on the collection of type information during
  debugging. This is because it has a big performance hit during debugging.
  Thus, you should only collect type information when working on adding
  type hints, then disable this feature for regular debugging.

Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 60, 65-66, 75

   - *Line 60*. We're keeping score, so start at zero.

   - *Lines 65-66*. Display the current score, during ``on_draw``, using
     a Python 3.5 f-string.

   - *Line 75*. Whenever you kill a coin, increase the score.

- *Enable type hint collection*. In settings/preferences, go to
  ``Build, Execution, Deployment | Python Debugger | Collect run time types
  information for code insight`` and click the checkbox, then close
  settings.

- *Debug*. Run the game under the debugger, as normal, with no breakpoints.
  Move the player around, etc.

- *Quit the game*. Either close the Arcade window or use terminate to stop
  the debugging session.

- *Click on a method*. We want to see what is ``delta_time``, so click on
  the method definition for ``MyGame.update``. Meaning, put your cursor in
  ``update`` for ``def update(self, delta_time)``.

- *Annotate types*. PyCharm has a "code intention" to perform the action
  we're looking for. Do ``Alt-Enter`` and choose ``Annotate types``. Press
  enter to accept the defaults for the two annotations in the red boxes.

- *Turn off type hint collection*. Remember to go back into the preferences
  and disable ``Collect run time types information for code insight``.

What's Going On
===============

This is quite cool: PyCharm is providing the type hints for you. How does
it do it? When you run code under the debugger, PyCharm sees all the input
and output values for functions and methods. It can then see the type
of those. PyCharm puts this to work by offering to write the type
information for you.