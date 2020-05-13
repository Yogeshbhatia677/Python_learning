import imdbpy
hr=imdb.IMDb()
movie_name=input('enter the movie name')
movies=hr.search_movie(str(movie_name))
index=movies[0].getID()
movie=hr.get_movie(index)
title=movie['tile']
year=movie['year']
cast=movie['cast']
list_of_cast=','.join(map(str,cast))
print("title",title)
print("year of release",year)
print("full cast",list_of_cast)