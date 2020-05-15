## biblioteca imdb = pip install IMDbPY
## biblioteca justWatch  = pip install JustWatch
## biblioteca request *alternativa para o imdb = pip install requests
from imdb import IMDb
from justwatch import justwatchapi, JustWatch
from collections import Counter
import requests


##### API Rapid imdb via Request --- metodo alternativo

melhores_filmes = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
novidades = "https://imdb8.p.rapidapi.com/title/get-news"
busca = "https://movie-database-imdb-alternative.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "152e8af0d7msha200170a6e2f5a3p1bf760jsnf830b2ea8546"
    }

limite = {"limit":"25","tconst":"tt0944947"}
query = {"i":"tt0111161","r":"json"} # parametros i = id ou nome filme/serie , type = filme/serie/ep, r = formato, plot = enredo, y = ano/reposi   

tops_filmes = requests.request("GET", melhores_filmes, headers=headers)
noticias = requests.request("GET", novidades, headers=headers, params=limite)
busca_filme = requests.request("GET", busca, headers=headers, params=query)

#print(noticias.text)

########

ia = IMDb()
just_watch = JustWatch(country='BR')

cont = 0

def buscaFilmeImdb (movie):
    filmes = ia.search_movie(movie)
    return filmes

def generoFilme (array):
    res = {'filme':[], 'generos':[]}
    for i in array:
        #print (ia.get_movie(i.movieID)['genres'])
        res['filme'].append(i['title'])
        res['generos'].append(ia.get_movie(i.movieID)['genres'])
    return res

def buscaFilmeAtor (x):
    personagem = ia.search_person(x)
    return personagem

def buscaTopFilmes ():
    filmes = ia.get_top250_movies()
    return filmes

def buscaFilmes():
    filmes = ia.get_bottom100_movies()
    return filmes

def generosDos10MelhoresFilmesImdb():
    tops = buscaTopFilmes()
    filmes = {'filme':[], 'generos':[]}
    melhorGenero = []
    for i in range(10):
        filmes['filme'].append(tops[i]['title'])
        filmes['generos'].append(ia.get_movie(tops[i].movieID)['genres'])
        melhorGenero.append(ia.get_movie(tops[i].movieID)['genres'])
    melhorGenero = str(melhorGenero).replace('[','').replace(']','').replace("'",'').replace('"','').replace(' ','').split(',')
    melhorGenero = Counter(melhorGenero)
    #print (melhorGenero.most_common()[0][0])
    return melhorGenero.most_common()[0][0]

#print (generosDos10MelhoresFilmesImdb())

#print (buscaFilmes())

#print(generoFilme(buscaFilmeImdb('avatar')))

#f = ia.search_movie('avatar')
#print(f[1])

genres = just_watch.get_genres()
#print(genres)

#showings_last_week = just_watch.get_upcoming_cinema(weeks_offset=6, nationwide_cinema_releases_only=False)
#print(showings_last_week)

#local_cinemas = just_watch.get_cinema_details()
#print(local_cinemas[0])

#results = just_watch.search_for_item(query='tropa de elite')
#print (results['items'][3]['title'])
#print (results['scoring'])

def buscaFilmeAvaliacao (string):
    resultado = just_watch.search_for_item(query= string)
    var = []
    for i in resultado['items'][0]['scoring']:
        var.append(i['value'])
    return var

def popularidadeFilme (filme):
    resultado = just_watch.search_for_item(query= filme)
    return resultado['items'][0]['tmdb_popularity']

def buscaFilmeJW (filme):
    resultado = just_watch.search_for_item(query= filme)
    return resultado['items'][0]

#print(popularidadeFilme('Tropa de Elite'))

def buscaPorGeneroDosMelhoresFilmes ():
    genero = generosDos10MelhoresFilmesImdb()
    for generos in just_watch.get_genres():
        if genero.lower() == generos['technical_name']:
            g = generos['short_name']
    jw = JustWatch(genres=[g])
    resultado = jw.search_for_item(content_types=['movie'])
    filme = {'nome':[],'popularidade':[],'preco':[]}
    aux = 0.0
    for i in resultado['items']:
        res = popularidadeFilme(i['title'])
        if (aux <= res):
            var = buscaFilmeJW(i['title'])
            aux = res
            filme['nome'].append(i['title'])
            filme['popularidade'].append(var['tmdb_popularity'])
            filme['preco'].append(var['offers']) 
    return  filme

#print (generosDos10MelhoresFilmesImdb())

#print(buscaPorGeneroDosMelhoresFilmes())
#print (buscaFilmeAvaliacao('tropa de elite'))

#print (just_watch.get_genres())