# 2048-Search-and-solve
Recursive search and solve for 2048

Logic for generating and evaluating states of the 2D matrix game "2048". Attempts to solve randomized games by optimizing via
the evaluating function.

Moves are taken as the following steps:
- Moves evaluated to a search depth of 3 by default (3 moves into the future), or at a depth of 1 when free space is limited
- The board state that produces the best score (at any of the scanned depths) yields the next first move taken
- Randomized tile of value 2 or 4 is generated on board
- Repeat until a 2048 tile on board or no moves can be taken.

This heuristic solves consistently for a 5*5 board or larger and fails consistently for a 4*4 tile board.
