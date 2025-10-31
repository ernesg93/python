
def is_triangle(sides: list) -> bool:
    """
    Check if three sides can form a valid triangle according to exercise rules.
    
    Args:
        sides: List of three side lengths [a, b, c]
        
    Returns:
        True if sides form a valid triangle (including degenerate triangles),
        False otherwise
    Note:
        Uses relaxed triangle inequality (a + b ≥ c) as per exercise instructions.
    """

    # option 1
    return all(side > 0 for side in sides) and max(sides) <= sum(sides) / 2

    # # option 2 (comment on option 1)
    # if len(sides) != 3: return False
    # a, b, c = sorted(sides)
    # return a > 0 and a + b >= c

def equilateral(sides: list) -> bool:
    """
    Check if triangle is equilateral (all sides equal).
    
    Args:
        sides: List of three side lengths
        
    Returns:
        True if equilateral triangle, False otherwise
    """
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides: list) -> bool:
    """
    Check if triangle is isosceles (at least two sides equal).
    
    Args:
        sides: List of three side lengths
        
    Returns:
        True if isosceles triangle, False otherwise
    """
    return is_triangle(sides) and len(set(sides)) <= 2

def scalene(sides: list) -> bool:
    """
    Check if triangle is scalene (all sides different).
    
    Args:
        sides: List of three side lengths
        
    Returns:
        True if scalene triangle, False otherwise
    """
    return is_triangle(sides) and len(set(sides)) == 3