from checkmate import checkmate

def main():
    #Success
    board = """\
R...
.K..
..Q.
....\
"""

    #Fail
#     board = """\
# ..
# .K\
# """

    checkmate(board)
main()