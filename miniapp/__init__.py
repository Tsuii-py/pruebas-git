"""miniapp: paquete pequeño con operaciones aritméticas.

Funciones:
- add(a, b)
- sub(a, b)
- mul(a, b)
- div(a, b): lanza ZeroDivisionError si b == 0
"""


def add(a, b):
    """Suma a y b."""
    return a + b


def sub(a, b):
    """Resta b de a."""
    return a - b


def mul(a, b):
    """Multiplica a por b."""
    return a * b


def div(a, b):
    """Divide a entre b. Lanza ZeroDivisionError si b == 0."""
    if b == 0:
        raise ZeroDivisionError('division by zero')
    return a / b
