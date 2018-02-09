#!/bin/python

import sys

def waysToGiveACheck(board):

    board = expandBoard(board)
    pcol = board[1].index("P")
    prow = 0
    try:
        kpos = [(i, line.index('k'))for i,line in enumerate(board) if 'k' in line][0]
    except:
        return 0
    board[1][pcol] = '#'
    if checkState(board, kpos):
        return 4

    count = 0

    for promotion in ('N', 'B', 'Q', 'R'):
        board[0][pcol] = promotion
        if checkState(board, kpos):
            count += 1

    return count

def expandBoard(board):
    return [list(b[0]) for b in board]

def validPos(pos):
    return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7

# N, B, R, Q and P, K
# n, b, r, q and p, k
def checkState(board, kpos):
    # check if the k is being checked
    krow, kcol = kpos

    # check the knights
    anyCheckingKnights = any(True for t in (
        (krow+1, kcol-2), (krow+2, kcol-1), 
        (krow+2, kcol+1), (krow+1, kcol+2), 
        (krow-1, kcol+2), (krow-2, kcol+1), 
        (krow-2, kcol-1), (krow-1, kcol-2)
        ) if validPos(t) and board[t[0]][t[1]] == 'N')

    if anyCheckingKnights:
        return True

    # the following check the straight line directions
    for col in range(0, kcol)[::-1]:
        if board[krow][col] in ('R', 'Q'): return True
        elif board[krow][col] == '#': continue
        else: break
    
    for col in range(kcol+1, 8):
        if board[krow][col] in ('R', 'Q'): return True
        elif board[krow][col] == '#': continue
        else: break

    for row in range(0, krow)[::-1]:
        if board[row][kcol] in ('R', 'Q'): return True
        elif board[row][kcol] == '#': continue
        else: break

    for row in range(krow+1, 8):
        if board[row][kcol] in ('R', 'Q'): return True
        elif board[row][kcol] == '#': continue
        else: break

    # the following check the diagonal line directions
    for col in range(kcol+1, 8):
        if not validPos((krow+col-kcol,col)): break
        if board[krow+col-kcol][col] in ('B', 'Q'): return True
        elif board[krow+col-kcol][col] == '#': continue
        else: break

    for col in range(kcol+1, 8):
        if not validPos((krow-(col-kcol),col)): break
        if board[krow-(col-kcol)][col] in ('B', 'Q'): return True
        elif board[krow-(col-kcol)][col] == '#': continue
        else: break

    for col in range(0, kcol)[::-1]:
        if not validPos((krow-(kcol-col),col)): break
        if board[krow-(kcol-col)][col] in ('B', 'Q'): return True
        elif board[krow-(kcol-col)][col] == '#': continue
        else: break

    for col in range(0, kcol)[::-1]:
        if not validPos((krow+kcol-col,col)): break
        if board[krow+kcol-col][col] in ('B', 'Q'): return True
        elif board[krow+kcol-col][col] == '#': continue
        else: break

    return False


# read board from text file
with open('board.txt') as f:
    board = [[line]for line in f.read().split('\n')]


print waysToGiveACheck(board)
exit()

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        board = []
        for board_i in xrange(8):
            board_temp = map(str,raw_input().strip().split(' '))
            board.append(board_temp)
        result = waysToGiveACheck(board)
        print result

