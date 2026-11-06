# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        0 dead dead
        1 alive alive
        2 alive dead
        3 dead alive
        #temp values !=2nd matrix
        rows=len(board)
        cols=len(board[0])
        directions=(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)
        
        #traverse
        for r in range(rows):
            for c in range(cols):
                liveNeighbors=0
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    #make sure neighrob in board
                    if 0<=nr<rows and 0 <=nc<cols:
                        #1 and 2 mean orignally alive
                        if board[nr][nc] in (1,2):
                            liveNeighbors+=1
                #game of life rules
                if board[r][c]==1:
                    #live cells dies with <2 or more than 3
                    if liveNeighbors<2 or liveNeighbors>3:
                        board[r][c]=2
                else:
                    # deadcell=>alive
                    if liveNeighbors==3:
                        board[r][c]=3
                    #dead cells become alive

        #2nd pass convert the temp states
          for r in range(rows):
            for c in range(cols):
                if board[r][c]==2:
                    board[r][c]=0
                elif board[r][c]==3:
                    board[r][c]=1