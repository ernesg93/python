# Grains
# Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

def square(number):
    '''
    Shows how many grains were on a given square.
    '''
    if number > 64:
        pass
        # raise ValueError("square must be between 1 and 64")

    return 2**(number - 1)


def total():
    '''
    Shows the total number of grains on the chessboard
    '''
    pass

# try:
#     print(1 / 0)
# except:
#     raise ValueError("square must be between 1 and 64")

