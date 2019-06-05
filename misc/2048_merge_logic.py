""" Clone of 2048 game.
Credit to:
    http://flothesof.github.io/2048-game.html
    https://github.com/enixdark/principlescomputing-001/tree/master/Week0

Game instruction:
    https://github.com/enixdark/principlescomputing-001/blob/master/Week0/Instructions.md
To run:
    python logic.py
"""

def merge(line):

    results = [0 for n in line]
    itm = [0 for n in line]

    # move all non-zero numbers to the left
    for i, j in enumerate(line):
        if j != 0:
            zero_index = itm.index(0)
            itm[zero_index] = j

    # merge like numbers but do not reuse a number

    # prepare a list to check whether or not a number
    #   has been used
    merged = [False for n in line]

    # a = the current number
    # b = the next number except when the index
    #   runs out
    for i, j in enumerate(itm):
        a = j
        if i+1 < len(itm):
            b = itm[i+1]
            if b == a:
                # change merged flags to True for each
                #   numbers used
                if merged[i] == False and merged[i+1] == False:
                    r = b + a
                    results[results.index(0)] = r
                    merged[i] = True
                    merged[i+1] = True
            else:
                # add number to results when it has not been used
                if merged[i] == False:
                    results[results.index(0)] = a
        else:
            # when the index runs out, add the number if it
            #   has not been used
            if merged[i] == False:
                results[results.index(0)] = a

    return results





## test

    """
    Correct merges: 
        [2 0 2 2] ->  [4 2 0 0]
        [0 2 2 0] -> [4 0 0 0]
        [2 2 2 8] -> [4 2 8 0]
        [0 2 2 4] -> [4 4 0 0]
        [2 2 2 2] -> [4 4 0 0]
        [256 256   2   4] -> [512   2   4   0]
        [256 128  64  32] -> [256 128  64  32]
        [2 0 2 0] -> [4 0 0 0]
        [2 0 2 4] -> [4 4 0 0]
        [0 0 2 2] -> [4 0 0 0]
        [8 16 16 8] -> [8 32 8 0]
    """



lines = ([2, 0, 2, 2], 
    [0, 2, 2, 0],
    [2, 2, 2, 8],
    [0, 2, 2, 4],
    [2, 2, 2, 2],
    [256, 256, 2, 4], 
    [256, 128, 64, 32],
    [2, 0, 2, 0],
    [2, 0, 2, 4],
    [0, 0, 2, 2],
    [8, 16, 16, 8],
)

for line in lines:
    print(f"{line} -> {merge(line)}")

