#!/usr/bin/python3

import math

# Memória Volátil
x = ((2 + 2) * 4 + 50) * math.sqrt(64)
print(x)

# Coerção de tipo
# O resultado de X é um número real (float)
# Para inserí-lo no arquivo de texto é necessário
# realizar coerção de tipo e transformá-lo em string
conteudo = str(x)

# Memória não volátil
with open('arquivo.txt', 'w') as f:
    f.write(conteudo)
    f.close()
