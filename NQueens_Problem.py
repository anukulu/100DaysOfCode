# This problem can be solved by using backtracking and recursion

import numpy as np

def Safe(board, col, row, N):

	# checking for the left side on the same row
	for i in range(0, col):
		if(board[row][i]):
			return False

	# checking for the upper left diagonal
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if(board[i][j]):
			return False

	# checking for the lower left diagonal
	for i, j in zip(range(row, N), range(col, -1, -1)):
		if(board[i][j]):
			return False

	return True

def NQueensSolve(board, col, N):

	if (col >= N):	# all the queens have been placed
		return True

	for i in range(N):	# iterating through the rows

		if (Safe(board, col, i, N)):	# if the queen is safe then make that position 1
			board[i][col] = 1

			if(NQueensSolve(board, col+1, N)): # after a queen is placed, program recurs to find safe position of other queens 
				return True

			board[i][col] = 0	# backtracking if the next queen cannot be placed (or is not safe)

	return False


N = int(input('Enter the board size : '))

board = np.zeros((N,N), dtype=int)

if(NQueensSolve(board, 0, N) == False):
	print('Solution does not exist')
else:
	print(board)



