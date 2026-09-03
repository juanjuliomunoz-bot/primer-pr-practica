"""Calcula el pago de horas extra segun el Codigo del Trabajo chileno (recargo 50%)."""

RECARGO_HORA_EXTRA = 1.5


def calcular_pago_horas_extra(valor_hora: float, horas_extra: float) -> float:
    if valor_hora < 0 or horas_extra < 0:
        raise ValueError("valor_hora y horas_extra deben ser no negativos")
    return valor_hora * RECARGO_HORA_EXTRA * horas_extra
