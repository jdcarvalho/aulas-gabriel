#!/usr/bin/python3
# Operadores Unários
valor = 1
# valor +=1 == valor = valor + 1
valor += 1
valor -= 1
print('\n----------------------Operadores Unários----------------------')
print(valor)
print('\n----------------------Operadores Binários----------------------')
# Operadores Binários
numero1 = 1
numero2 = 2
print(numero2 + numero1)
print(numero1 - numero2)
# Operadores Ternários
print('\n----------------------Operadores Ternários----------------------')
idade = 18
maioridade = True if idade >= 18 else False
print(maioridade)
print('\n----------------------Operadores Relacionais----------------------')
idade = 13
maioridade = 18
print('idade > maioridade: {0}'.format(idade -> maioridade))
print('idade < maioridade: {0}'.format(idade < maioridade))
print('idade >= maioridade: {0}'.format(idade >= maioridade))
print('idade <= maioridade: {0}'.format(idade < maioridade))
print('idade == maioridade: {0}'.format(idade == maioridade))

nome = 'Miguel'
sobrenome = 'Carvalho'
print(nome +' '+sobrenome)

print('\n----------------------Índices de Lista----------------------')
lista = [1,2,3,4,5,6,7,8,9,10]

print('Tamanho da Lista: ', len(lista))
print('Primeiro elemento da lista: ', lista[0])
print('Último elemento da lista: ', lista[len(lista)-1])
print('Último elemento da lista: ', lista[-1])

print('\n----------------------Dicionários----------------------')
valor = {
    'nome': 'Gabriel',
    'telefone': 'Quebrado',
}
valor.update({
    'idade': 13,
    'nome_do_pai': 'Silvio',
})
valor['nascimento'] = '06/12/2007'
print(valor)
