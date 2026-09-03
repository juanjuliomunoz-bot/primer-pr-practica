# Calculadora de Horas Extra

Utilidades sencillas en Python para calcular el pago de horas extra de un trabajador.

## Uso

```python
from horas_extra import calcular_pago_horas_extra

pago = calcular_pago_horas_extra(valor_hora=5000, horas_extra=3)
print(pago)  # 22500.0
```

## Instalación

No se necesitan dependencias externas, solo Python 3.

## Tests

```bash
python -m unittest discover
```
