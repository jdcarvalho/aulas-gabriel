#!/usr/bin/python3

import math

# Memória Volátil
x = ((2 + 2) * 4 + 50) * math.sqrt(64)
print(x)

# Memória não volátil
with open('arquivo.txt', 'w') as f:
    f.write(str(x))
    f.close()
