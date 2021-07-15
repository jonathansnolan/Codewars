def valid_solution(board):

    #################################
    # Created another sudoku list going top to bottom instead of left to right:
    #################################
    if len(board) != 9:
        return False

    x = []

    for k in list(range(0,len(board))):
        i = []
        for u in list(range(0,len(board))):
            i.append(board[u][k])
        x.append(i)

    #################################
    # check to make sure first list isn't equal to any at bottom
    #################################

    for k in list(range(0,len(board))):
        for u in list(range(0,len(board))):
            if board[k] == board[u] and k != u:
                return False

    #################################
    # check to make sure second list isn't equal to any other
    #################################
    for k in list(range(0,len(x))):
        for u in list(range(0,len(x))):
            if x[k] == x[u] and k != u:
                return False

    #################################
    # check no zeros
    #################################

    for k in list(range(0, len(board))):
        if 0 in board[k]:
            return False

    #################################
    # check no overlapping
    #################################

    for k in list(range(0, len(board))):
        p = list(dict.fromkeys(board[k]))
        if len(p) != 9:
            return False
    #################################
    # check no overlapping
    #################################

    for k in list(range(0, len(board))):
        l = list(dict.fromkeys(x[k]))
        if len(l) != 9:
            return False

    ##################################
    n = []

    # BOX 1

    d = []

    for k in list(range(0,3)):
        for u in list(range(0,3)):
            d.append(board[k][u])
    n.append(d)

    # BOX 2

    d = []
    for k in list(range(0,3)):
        for u in list(range(3,6)):
            d.append(board[k][u])
    n.append(d)

    # BOX 3

    d = []

    for k in list(range(0,3)):
        for u in list(range(6,9)):
            d.append(board[k][u])
    n.append(d)

    # BOX 4

    d = []
    for k in list(range(3,6)):
        for u in list(range(0,3)):
            d.append(board[k][u])
    n.append(d)

    # BOX 5
    d = []
    for k in list(range(3,6)):
        for u in list(range(3,6)):
            d.append(board[k][u])
    n.append(d)
    # BOX 6
    d = []
    for k in list(range(3,6)):
        for u in list(range(6,9)):
            d.append(board[k][u])
    n.append(d)
    # BOX 7
    d = []
    for k in list(range(6,9)):
        for u in list(range(0,3)):
            d.append(board[k][u])
    n.append(d)
    # BOX 8
    d = []
    for k in list(range(6,9)):
        for u in list(range(3,6)):
            d.append(board[k][u])
    n.append(d)
    # BOX 9
    d = []
    for k in list(range(6,9)):
        for u in list(range(6,9)):
            d.append(board[k][u])

    n.append(d)

    ##############################
    # Check no over lappening
    ##############################

    for k in list(range(0, len(n))):
        r = list(dict.fromkeys(n[k]))
        if len(r) != 9:
            return False

    return True
