from jikanpyv4 import Jikan
jikan = Jikan()

def get_movies_by_genre(genre):
        # Get the genre ID for the given genre name
        genre_id = jikan.search('genre', genre=genre)['type'][0]['mal_id']
        # Get the movies in the specified genre
        movies = jikan.genre(type='anime', genre_id=genre_id)['anime']
        return movies
    
def get_jikan_genre():
    return jikan.genres(type='anime')

def get_jikan_producer(id):
    producer = jikan.producers(id=id)
    print(producer)
    return producer

def search_jikan_genre_by_name():
    jikan.search('anime', page=2, parameters={'genre': 48})
    
def recommendations():
    jikan.recommendations('anime')
    
def schedules():
    jikan.schedules()
  
if __name__ == "__main__":
    print(schedules())
