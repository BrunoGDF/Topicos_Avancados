# Topicos_Avancados

#Primeira entrega

Mateus - preparacao de scripts sql para inserçao no banco, tanto ingles quanto em portugues

Ariene / Bruno - levantamento de requisitos, planejamento de sprints e organizacao de tasks no trello

Rafael / César / Henrique - Conexao com banco, rotas para cadastro de genero no grupo e uma rota para pre cadastro inicial

Gilberto - config do ambiente com python, docker postgres e bibliotecas de python

Everton - Criacao de tabelas, relacionamentos e modelagem

Willian - Estudou bibliotecas imdb, primeira parte de busca dos dados da imdb

# Usando a biblioteca do IMDB

"""
Created on Thu Mar  5 19:56:27 2020

@author: bruno
"""

#Para instalar a biblioteca, basta dar um "pip install imdbpy"

from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie and print its director(s)
the_matrix = ia.get_movie('0133093')
for director in the_matrix['directors']:
    print(director['name'])

# show all information that are currently available for a movie
print(sorted(the_matrix.keys()))

# show all information sets that can be fetched for a movie
print(ia.get_movie_infoset())

# update a Movie object with more information
ia.update(the_matrix, ['technical'])
# show which keys were added by the information set
print(the_matrix.infoset2keys['technical'])
# print one of the new keys
print(the_matrix.get('tech'))


______________________________________________________________________________________________________________

"""
Created on Thu Mar  5 19:56:27 2020

@author: bruno
"""

#Para instalar a biblioteca, basta dar um "pip install imdbpy"

from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie and print its director(s)
the_matrix = ia.get_movie('0133093')
for director in the_matrix['directors']:
    print(director['name'])

# show all information that are currently available for a movie
print(sorted(the_matrix.keys()))

# show all information sets that can be fetched for a movie
print(ia.get_movie_infoset())

# update a Movie object with more information
ia.update(the_matrix, ['technical'])
# show which keys were added by the information set
print(the_matrix.infoset2keys['technical'])
# print one of the new keys
print(the_matrix.get('tech'))
