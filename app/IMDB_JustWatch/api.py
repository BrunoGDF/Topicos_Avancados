## biblioteca imdb = pip install IMDbPY
## biblioteca justWatch  = pip install JustWatch

from imdb import IMDb
from justwatch import justwatchapi, JustWatch

movie =''

ia = IMDb()
'''
def buscaFilmeImdb (movie):
    filmes = ia.search_movie(movie)
    return filmes

def buscaFilmeAtor (figurante):
    personagem = ia.search_person(figurante)
    return personagem

def buscaFilmeOscar ():
    resulta = ia.get_movie_awards()
    return resulta

print(buscaFilmeImdb('tropa de elite'))


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

movie = ia.get_movie('0133093')

print('Directors:')
for director in movie['directors']:
    print(director['name'])

print('Genres:')
for genre in movie['genres']:
    print(genre)

people = ia.search_person('Mel Gibson')
for person in people:
   print(person.personID, person['name'])

## 
'''
just_watch = JustWatch()


#genres = just_watch.get_genres()
#print(genres)

just_watch = JustWatch(country='BR')

results = just_watch.search_for_item(query='tropa de elite')
print (results)
#print (results['scoring'])

#print (just_watch.get_genres())

'''
def busca_genero(array){
    for array in just_watch.get_genres():

}
'''                                        