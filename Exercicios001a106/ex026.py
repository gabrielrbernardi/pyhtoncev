frase = str(input('Digite uma frase: ')).lower().strip()
pos1 = frase.count('a')
print('A letra aparece {} vezes'.format(pos1))
print('A primeira letra a aparece na posicao {}'.format(frase.find('a')))
print('A ultima letra a aparece na posicao {}'.format(frase.rfind('a')))