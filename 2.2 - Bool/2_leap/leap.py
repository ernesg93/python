
def leap_year(year: int) -> bool:
    """
    Determine if a year is a leap year in the Gregorian calendar.
    
    Args:
        year: Year to evaluate
        
    Returns:
        True if it's a leap year, False otherwise
    """
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0
