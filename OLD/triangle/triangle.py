# Triangle
# Welcome to Triangle on Exercism's Python Track.


# def equilateral(sides):
#     return is_valid(sides) and len(set(sides)) == 1


# def isosceles(sides):
#     return is_valid(sides) and len(set(sides)) < 3


# def scalene(sides):
#     return is_valid(sides) and len(set(sides)) == 3


# def is_valid(sides):
#     return all(sides) and (sum(sides) >= max(sides)*2)


def is_triangle(sides):
    '''
    Comprueba si es un triángulo dada una lista con tres valores (lados):
        1- Veridica que no exista un lado nulo.
        2- Verifica que se cumpla la desigualdad triangular.
    '''
    if sides[0] != 0 and sides[1] != 0 and sides[2] != 0:
        if (sides[0] <= sides[1] + sides[2]) and (sides[1] <= sides[2] + sides[0]) and (sides[2] <= sides[0] + sides[1]):
            return True
        else:
            return False
    else:
        return False


def equilateral(sides):
    '''
    An equilateral triangle has all three sides the same length.
    '''
    if is_triangle(sides) == True:
        if (sides[0] == sides[1]) and (sides[0] == sides[2]) and (sides[1] == sides[2]):
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    '''
    An isosceles triangle has at least two sides the same length.
    '''
    if is_triangle(sides) == True:
        if (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]):
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    '''
    A scalene triangle has all sides of different lengths.
    '''
    if is_triangle(sides) == True:
        if (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2]):
            return True
        else:
            return False
    else:
        return False
