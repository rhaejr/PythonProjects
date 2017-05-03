import time
board = '0#################'
right = False
while True:
    print(board)
    if board[-1] == '0':
        right = True
    if board[0] == '0':
        right = False
    if right:
        board = '{}{}'.format(board[1:], board[0])
    else:
        board = '{}{}'.format(board[-1], board[:-1])

    time.sleep(.05)