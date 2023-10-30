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

