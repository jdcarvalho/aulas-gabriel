#!/usr/bin/python3

versao = 2

miguel = {
    'nome': 'Miguel',
    'idade': 13,
    'sabe_programar': False,
    'sabe_jogar': True,
    'joga_agario': True,
    'joga_cs': 'Ruuuuuim',
}

gabriel = {
    'nome': 'Gabriel',
    'idade': 13,
    'sabe_programar': False,
    'sabe_jogar': True,
    'joga_agario': False,
    'joga_cs': 'Nada haver',
}

if versao == 1:
    if ((miguel['sabe_jogar'] and gabriel['sabe_programar']) or (miguel['idade'] > 12 and gabriel['idade'] == 13)):
        print('Nada haver irmão!')
    else:
        print('Ta tudo errado essas pergunta...')
elif versao == 2:
    if ((miguel['joga_cs'] or gabriel['joga_cs']) and (miguel['joga_agario'] or (miguel['sabe_jogar'] and miguel['sabe_programar']))):
        print('Nada haver irmão!')
    else:
        print('Ta tudo errado essas pergunta...')
else:
    print('Ta tudo errado esse programa ai...')
