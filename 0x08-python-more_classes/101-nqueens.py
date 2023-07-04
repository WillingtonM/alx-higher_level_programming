#!/usr/bin/python3

"""N-queens puzzle.

Determines possible solutions to placing N
N non-attacking queens on NxN chessboard.

N must be an integer >= 4.

Attributes:
    board: A list of lists representing chessboard.
    solutions: A list of lists containing solutions.

Solutions are represented in format [[r, c], [r, c], [r, c], [r, c]]
where `r` &`c` represent the row and column, respectively, where a
queen must be placed on chessboard.
"""
import sys

def initialise_board(n):
    """Initialize `n`x`n` sized chessboard with 0's."""
    chess_board = []
    [chess_board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chess_board]
    return (chess_board)


def chs_brd_deepcopy(chs_board):
    """Return deepcopy of chessboard."""
    if isinstance(chs_board, list):
        return list(map(chs_brd_deepcopy, chs_board))
    return (chs_board)

def get_sol(chs_board):
    """Return the list of lists representation of solved chessboard."""
    solution = []
    for r in range(len(chs_board)):
        for c in range(len(chs_board)):
            if chs_board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def x_out(chs_board, row, column):
    """X out spots on a chessboard.
    """
    for c in range(column + 1, len(chs_board)):
        chs_board[row][c] = "x"
    for c in range(column - 1, -1, -1):
        chs_board[row][c] = "x"
    for r in range(row + 1, len(chs_board)):
        chs_board[r][column] = "x"
    for r in range(row - 1, -1, -1):
        chs_board[r][column] = "x"
    c = column + 1
    for r in range(row + 1, len(chs_board)):
        if c >= len(chs_board):
            break
        chs_board[r][c] = "x"
        c += 1
    c = column - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chs_board[r][c]
        c -= 1
    c = column + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chs_board):
            break
        chs_board[r][c] = "x"
        c += 1
    c = column - 1
    for r in range(row + 1, len(chs_board)):
        if c < 0:
            break
        chs_board[r][c] = "x"
        c -= 1

def rec_solve(chs_board, row, chs_queens, chess_solutions):
    """Solve recursively N-queens puzzle.
    """
    if chs_queens == len(chs_board):
        chess_solutions.append(get_sol(chs_board))
        return (chess_solutions)

    for c in range(len(chs_board)):
        if chs_board[row][c] == " ":
            tmp_board = chs_brd_deepcopy(chs_board)
            tmp_board[row][c] = "Q"
            x_out(tmp_board, row, c)
            chess_solutions = rec_solve(tmp_board, row + 1,
                                        chs_queens + 1, chess_solutions)

    return (chess_solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chs_board = initialise_board(int(sys.argv[1]))
    chess_solutions = rec_solve(chs_board, 0, 0, [])
    for sol in chess_solutions:
        print(sol)
