"""error_estimado_interpolacion — cuaderno 01.

Libro: ecuación (18.18).  Rn = f[x_{n+1},...,x_0] * prod(x - x_i)
"""

from ejercicios.interpolacion.error_estimado_interpolacion import (
    error_estimado_interpolacion,
)


def interpolacion_cuadratica(x0, y0, x1, y1, x2, y2, x, x3=None, y3=None):
    """Devuelve ``(y, error)``.

    y     : valor interpolado con la parábola que pasa por los tres nodos.
    error : ``None`` si no hay cuarto dato; si lo hay,
            ``R2 = f[x3,x2,x1,x0] * (x - x0)(x - x1)(x - x2)``.

    x3, y3 son OPCIONALES: puedes terminar el método sin usarlos y, cuando
    escribas ``error_estimado_interpolacion``, regresar aquí y activarlos.
    """
    m1 = (y1 - y0) / (x1 - x0)
    m2 = (y2 - y1) / (x2 - x1)

    b0 = y0
    b1 = m1
    b2 = (m2 - m1) / (x2 - x0)

    y = b0 + b1 * (x - x0) + b2 * (x - x0) * (x - x1)

    error = None
    if x3 is not None and y3 is not None:
        error = error_estimado_interpolacion(x0, y0, x1, y1, x2, y2, x3, y3, x)

    return y, error
