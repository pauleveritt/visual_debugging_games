=========================================================
Debugging During Testing and Moving Coins with Collisions
=========================================================

Our player moves, but our coins don't. Let's have the coins move down, and
when it reaches the bottom, it "respawns" near the top. Also, when a player
collides with a coin, the coin disappears.

Let's also use this point to show a hidden feature of debugging: use
during testing and test-driven development. As you are writing a test,
you are in discovery mode and, since your code is still emerging, things are
going to break. This is a good place to use debugging, as part of test
writing.

Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 13-15, 17-20, 52, 57, 67-70

   - *Lines 17-20*. The regular sprite ``update`` function, called whenever
     the game's ``on_draw`` says to update (line 63). Here we move the coin
     down a pixel. Then, if it reaches the bottom, "respawn" by calling
     its ``reset_pos`` method.

   - *Lines 13-15*. Move this coin somewhere near the top and randomly
     positioned left/right.

   - *Line 52*. As we see next, we also want to keep a sprite list of just
     for coins.

   - *Line 57*. Add this coin to the coin list.

   - *Lines 67-68*. Arcade makes it easy to find which sprites overlap with
     a certain sprite. ``hit_list`` is thus, which coins collided with the
     player.

   - *Lines 69-70*. Kill each of the colliding coins.

#. *Run under the debugger*. Just to see what we've done with the coins,
   click the debug button |debug| to run the game, without any breakpoints.
   You see the coins moving down, and when the player hits one, it "respawns"
   higher up.

#. *Generate a test*. Let's test the Coin's ``reset_pos`` method. PyCharm
   can help you generate the test code. Click on line 13 (``def reset_pos``)
   and choose ``Navigate | Test``.

#. *Create new test*. There isn't a test to navigate to, so PyCharm asks if
   you want to create one. Choose ``Create New Test...``

#. *Select method*. Click the checkbox to generate a test ``test_reset_pos``
   and click ``OK``.

#. *Run the test*. Right-click in the ``test_coin.py`` editor and choose
   ``Run 'Unittests in test_co...`` to run the file under the project-default
   test runner (Python's standard ``unittest``.)

PyCharm opens a Run tool window with the output of the test run. This run
tool window is different: it is a run configuration of type Python Unittests
and has a lot of UI specific to test running.

Our first test fails. That's normal: we told it to fail.

#. *Enter test*. Let's fill in a simple test:

   .. literalinclude:: test_coin.py
        :language: python
        :linenos:

#. *Rerun test*. Click the green play button in the test window to rerun the
   test. The test now passes.

We'd like to know more than "doesn't equal". The coin should be near the top.
Let's use the debugger to investigate.

#. *Set breakpoint*. Click in the gutter to set a breakpoint |breakpoint|
   on line 9 in the test (``c.update()``).

#. *Run test under debugger*. Right-click in the editor and choose
   ``Debug 'Unittests in test_co...`` to start debugging the test. Execution
   stops on that line.

#. *Step into*. Click the step into button |stepinto| to go into the coin's
   ``update`` method. Click the step into my code button |stepintomy| 3 times
   until execution is on line 14 of ``game.py`` (``self.center_y =``).

#. *Use Evaluate Expression*. Click the evaluate expression button
   |evaluate| and get the minimum value of ``SCREEN_HEIGHT + 20``, which is
   620. We now know what to put in our test. Do the same for
   ``SCREEN_HEIGHT + 100`` which gives 700.

#. *Add test assertion*. Let's assert that the value is between the
   correct range: ``self.assertTrue(620 < c.center_y < 700)``. Add this line
   after ``c.update()``.

#. *Remove breakpoint*. Click the red circle to remove the breakpoint in the
   test file.

#. *Re-run*. Click the debug button |debug| in the debug window to re-run
   the tests under the debugger, which now passes.

What's Going On
===============

We wrote a simple Python unittest, which executes under the test runner
configured for the run configuration. By default, PyCharm assigns the test
runner under ``Settings | Tools | Python Integrated Tools``. If you don't
``nose`` or ``pytest``, this defaults to Python's standard ``unittest`` test
runner from the standard library.

The Debug tool window changes to have all the capabilities of a visual test
runner. But the two-tab interface -- ``Debugger`` and ``Console`` -- are
still available.

Regarding the game, we use Arcade's built-in collision detection code. You
pass it an Arcade sprite and a second sprite list, and Arcade returns each
of the sprites in the sprite list which overlap with the passed-in sprite.

Our coins move down the screen and, when they reach the bottom, respawn
themselves somewhere close to the top of the screen.

.. |debug| image:: ../images/debug.png
.. |rerun| image:: ../images/stop_and_rerun.png
.. |resume| image:: ../images/debug_resume.png
.. |terminate| image:: ../images/stop.gif
.. |breakpoint| image:: ../images/db_set_breakpoint.png
.. |stepinto| image:: ../images/frames_step_into.png
.. |stepintomy| image:: ../images/step_into_my_code.png
.. |evaluate| image:: ../images/variables_evaluate_expr.png
