#DICTIONARIES
movie = {
  "Movie": "Top Gun: Maverick",
  "Imdb": 8.6, "year": 2022
}
print(movie)

#INSERTING
movie =	{
  "Movie:": "Top Gun: Maverick",
  "Imdb:": 8.6,
  "year:": 2022
}
movie["Director:"] = "Joseph Kosinski"
print('\nInsertion operation: ',movie)

#REPLACING
movie.update({"Imdb:" : 8.5})
print('\nAfter update: ',movie)

#ACCESSING DICTIONARY
print ("\nDict key-value are : ")
for i in movie :
    print(i, movie[i])

#VALUES()
x = movie.values()
print('\nUsing Values function:',x)

#KEYS()
X = movie.keys()
print('\nUsing the keys function: ',X)

#POP() & POPITEM()
x = movie.pop("year:")
print('\nUsing pop function: ',x)

x = movie.popitem()
print('\nUsing Popitem function: ',x)


