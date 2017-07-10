==================================
Attach to Process and Moving Coins
==================================

- Moving coins

Steps
=====

#. Terminate the game, if it is running, and make sure you have no breakpoints
   set.

#. Edit ``game.py`` to have the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:
        :emphasize-lines: 13-15, 17-20

   - *Lines 17-20*. The regular sprite ``update`` function, called whenever
     the game's ``on_draw`` says to update (line 63). Here we move the coin
     down a pixel. Then, if it reaches the bottom, "respawn" by calling
     its ``reset_pos`` method.

   - *Lines 13-15*. Move this coin somewhere near the top and randomly
     positioned left/right.

- Click terminal.

- python game.py

- Run | Attach to Local Process...

- Choose game.py

- Debug PID# tool window appears

- Put a breakpoint on line 14

- Execution stops as soon as first coin goes to bottom

- TODO Why does resume not make the next coin stop?

What's Going On
===============
