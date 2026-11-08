# Nine Men's Morris (Python)

A two-player, command-line version of the classic board game Nine Men's Morris, written in Python.
Built as part of my university Python coursework (University of Manchester).

## How to play

Run the game in a terminal that supports ANSI colours (e.g. Windows Terminal, VS Code, Spyder):

    python ninemenmorris.py

The board has 24 points, numbered 0-23. A reference board is printed next to the live board each turn.
Player 1 is `X` (red) and Player 2 is `O` (blue); `+` is an empty point.

1. **Placing phase:** each player has 9 counters and takes turns placing one on an empty point.
2. **Moving phase:** once both players have placed all their counters, players take turns sliding a counter to an adjacent empty point.
3. **Mills:** forming a line of three of your own counters (a "mill") lets you remove one of your opponent's counters.
4. A player who cannot make a move on their turn loses.

## What's implemented

- Board representation and the adjacency rules for all 24 points
- Detection of all 16 possible mills
- Placing, moving and removing counters, with input validation and error handling
- Turn handling for both phases, including checking whether a player can move at all
- Saving the game state to `game_state.txt` after every turn, and loading it back (`save_state` / `load_state`)

## Not implemented (known limitations)

- "Flying" when a player is down to three counters
- Losing by being reduced to two counters (the game currently ends only when a player has no legal move)
- The rule that counters in a mill are protected from removal
- Resuming a saved game from the start menu (the load function exists but is not wired into the game loop)

## Credits

The board drawing (`draw_board`) and the input helper (`request_location`) were provided in the coursework template.
The game logic and turn handling are my own work.
