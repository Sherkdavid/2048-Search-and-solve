# 2048-Search-and-solve
Recursive search and solve for 2048

Logic for generating and evaluating states of the 2D matrix game "2048". Attempts to solve randomized games by optimizing via
the evaluating function.

Moves are taken as the following process:
- Moves evaluated to a search depth of 3 (3 moves into the future), or at a depth of 1 when free space is limited.
- The board state that produces the best score (at any depth) is the next first move taken
- Random tile generated on board
- Repeat until 2048
