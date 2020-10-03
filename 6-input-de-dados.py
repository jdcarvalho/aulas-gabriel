#!/usr/bin/python3

versao = 4

if versao == 1:
    # Versão 1
    print('Olá, como vai? Qual é o seu Nome?')
    x = input('Digite seu nome para continuar...')
    # Checagem se o valor existe na variável
    # No Python toda variável que for diferente de vazio ou de 0 é booleano verdadeiro
    # Caso seja vazio ou 0 então é booleano falso
    if x:
        print('Seja bem vindo: {0}'.format(x))
    else:
        print('Não quero falar com que não fala o nome')
elif versao == 2:
    # Código da versão 2
    # Melhoria onde enquanto o usuário não informar seu nome
    # o sistema deve exigir que ele informe pra poder continuar
    print('Olá, como vai? Qual é o seu Nome?')
    x = input('Digite seu nome para continuar...')
    while not x:
        x = input('Digite seu nome para continuar...')
    print('Seja bem vindo: {0}'.format(x))
elif versao == 3:
    # Código da versão 3
    # Se o usuário não informar nome por 3 vezes enviamos uma mensagem para que
    # se anime e coloque o nome
    print('Olá, como vai? Qual é o seu Nome?')
    x = input('Digite seu nome para continuar...')
    contador = 0
    while not x:
        contador = contador + 1
        if contador == 3:
            print('\nMermão dexe de onda viu? Fale seu nome!!!!')
        x = input('Digite seu nome para continuar...')
    print('Seja bem vindo: {0}'.format(x))
elif versao == 4:
    # Código da versão 4
    # Se o usuário não informar nome por 3 vezes até que ele informe
    # Vamos mudar as mensagens com que falamos com ele
    mensagens = [
        'Mermão, deixe de onda! Coloque logo seu nome!',
        'Vou chamar a polícia! Coloque seu nome!',
        'Tu é doido é doido? Coloque seu nome!',
        'Você vai morrer se não colocar o nome!',
        'Vou chamar mainha! Coloque seu nome!',
    ]
    print('Olá, como vai? Qual é o seu Nome?')
    x = input('Digite seu nome para continuar ')
    contador = 0
    while not x:
        contador = contador + 1
        if contador > 3:
            from random import randint
            # Índice será um número randômico entre 0 e o tamanho da
            # Variável de mensagens -1 porque o índice começa em 0
            indice = randint(0, len(mensagens)-1)
            print('\n')
            print(mensagens[indice])
        x = input('Digite seu nome para continuar...')
    print('Seja bem vindo: {0}'.format(x))
else:
    print('Erro de programação, versão errada')
