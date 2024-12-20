# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

## Hint: end=" " means that the cursor is not moved to the next line; a space is printed instead


for row in tic_tac_toe_board:
   for column in row:
      print(column, end=" ")
   print()