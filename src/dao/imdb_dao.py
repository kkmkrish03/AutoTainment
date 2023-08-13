from imdb import Cinemagoer

ia = Cinemagoer()

# get a movie and print its director(s)
the_matrix = ia.get_movie('0133093')
for director in the_matrix['directors']:
    print(director['name'])
    
print(sorted(the_matrix.keys()))
print(ia.get_movie_infoset())
ia.update(the_matrix, ['technical'])
print(the_matrix.infoset2keys['technical'])
print(the_matrix.get('tech'))
movie = ia.get_movie('0133093')

# print the names of the directors of the movie
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)

# search for a person name
people = ia.search_person('Mel Gibson')
for person in people:
   print(person.personID, person['name'])