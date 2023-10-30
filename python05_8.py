#!/usr/bin/env python3

#1.Construindo um dicionário com as minhas coisas favoritas e imprimindo o dicionário
fav_dict = {'Cantora' : 'Beyoncé', 'Livro' : 'Cosmos', 'Árvore' : 'Quaresmeira'}
print(f'Dicionário com as minhas coisas favoritas: {fav_dict}')

#2.Imprimindo meu livro favorito
print(f'O meu livro favorito é: {fav_dict["Livro"]}')

#3.Imprimindo meu livro favorito, mas com uma variável na chave
fav_thing = 'Livro'
print(f'O meu livro favorito é: {fav_dict[fav_thing]}')

#4.Imprimindo a minha árvore favorita
print(f'A minha árvore favorita é: {fav_dict["Árvore"]}')

#5.Adicionando meu organismo favorito ao dicionário, imprimindo o novo dicionário e o tornando o novo valor de fav_thing
fav_dict['Organismo'] = 'Baleia'
print(fav_dict)
fav_thing = 'Organismo'
print(f'O meu organismo favorito é: {fav_dict[fav_thing]}')

#6.Obtendo um valor da linha de comando para fav_thing e imprimindo o valor correspondente
fav_thing = input("Insira seu input: ")
print(fav_dict[fav_thing])

#7.Alterando o valor do organismo favorito e imprimindo novo dicionário
fav_dict['Organismo'] = 'Gato'
print(f'Dicionário com as minhas coisas favoritas com o novo organismo favorito: {fav_dict}')

#8. Obtendo fav_thing da linha de comando e um novo valor para essa chave utilizando input
fav_thing = input("Insira seu input: ")
fav_dict[fav_thing] = input("Insira seu input: ")
print(f'Dicionário com as minhas coisas favoritas alterado: {fav_dict}')

