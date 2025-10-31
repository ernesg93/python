
def steps(number: int, count: int = 0) -> int:
    """
    Calcula los pasos de la conjetura de Collatz.
    Args:
        number: Número positivo entero o convertible a entero
        count: Contador interno (no usar externamente)
    Returns:
        int: Número de pasos para llegar a 1
    Raises:
        ValueError: Si el número no es positivo
    """
    
    # Validación primero
    try:
        number = int(number)
        if number < 1:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("Only positive integers are allowed")
    
    # Algoritmo iterativo (sin problemas de recursión)
    while number != 1:
        number = number // 2 if number % 2 == 0 else number * 3 + 1
        count += 1

    return count
