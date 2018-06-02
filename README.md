# ufloat
Add float class with SI units.

## Usage
You can make ufloat instance by:
```python
import ufloat
ufloat(value, unitclass)
```
* value : Anything that can use in `float(anything)` 
* unitclass : This is defined by `units.py`. Example, 'm', 'km', 'N', 'kN'...

### str() or print()
Return string, concat value and unit
```python
print(ufloat(100, m))
# 100 m
```

### operations
Calculate self value and other value. Unit is made up to self unit.
```python
width = ufloat(100, mm)
depth = ufloat(0.2, m)

area1 = width * depth      # area is to ufloat class.
print(area1)
# 20000 mm2

area2 = depth * width
print(area2)
# 0.02 m2
```

## Units

### Length

| name | class name | distance |
| --- | --- | --- |
| millimeter | mm | 10^-3 |
| centimeter | cm | 10^-2 |
| meter | m | 1 |
| kilometer | km | 10^3 |

### Mass

| name | class name | distance |
| --- | --- | --- |
| gram | g | 10^-3 |
| kilogram | kg | 1 |

### Time

| name | class name | distance |
| --- | --- | --- |
| seconds | s | 1 |

### Current

| name | class name | distance |
| --- | --- | --- |
| ampere | A | 1 |

### Temperature

| name | class name | distance |
| --- | --- | --- |
| kelvin | K | 1 |

### Amount of substance

| name | class name | distance |
| --- | --- | --- |
| mol | mol | 1 |

### Luminous intensity

| name | class name | distance |
| --- | --- | --- |
| candela | cd | 1 |

## Licence
MIT

## Autor
Ryuhei Fuita
