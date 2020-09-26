#!/usr/bin/python3

valor_booleano_verdadeiro = True
valor_booleano_falso = False

string_value = 'Valor teste'
string_value1 = "Valor Teste 2"

string_block = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
"""

# Tipos comuns de variáveis
numero_inteiro = 3
numero_real = 1.3

print(valor_booleano_verdadeiro)
print(valor_booleano_falso)
print(string_value)
print(string_value1)
print(string_block)
print(numero_inteiro)
print(numero_real)

print(numero_real * -1)


# Estruturas de dados

lista = list()
lista1 = []
print('Listas iguais: {0}'.format(lista == lista1))

tupla = tuple()
tupla1 = ()
print('Tuplas iguais: {0}'.format(tupla == tupla1))

dicionario = dict()
dicionario1 = {
    'nome': 'Gabriel',
    'telefone': '3233434235',
    'idade': 13,
}
print('Dicionários iguais: {0}'.format(dicionario == dicionario1))

conjunto = set()

a = set({1,2,3})
b = set({2})
print(a - b)


numeros = [1,2,3,4,5,6,7,9,11,22,44,1200, 859]

print([x for x in numeros if x % 2 == 0])
print([x for x in numeros if x % 2 != 0])

print([x for x in numeros if (x % 1 == 0) and (x % x == 0) and (x % 2 != 0)])




