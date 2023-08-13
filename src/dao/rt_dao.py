import rottentomatoes as rt

print(rt.tomatometer("happy gilmore"))
print(rt.audience_score('top gun maverick'))
print(rt.rating('everything everywhere all at once'))
print(rt.genres('top gun'))
print(rt.weighted_score('happy gilmore'))
print(rt.year_released('happy gilmore'))
print(rt.actors('top gun maverick', max_actors=5))

movie = rt.Movie('top gun')
print(movie)
print(movie.weighted_score)
