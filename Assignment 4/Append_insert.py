#Lists
movies = ['Memento','Gone girl','Scarface']

#APPEND     
movies.append('Arrival')
print("Inserted at the end(append): ",movies)

#INSERT
movies.insert(3,'Black panther')
print("\nInserted at a particular position: ",movies)

#EXTEND
shows = ['GOT','Succession','Mad men']
movies.extend(shows)
print("\nExtended the list: ",movies)

#REMOVE
movies.remove('Memento')
print("\nRemoved from the list: ",movies)

#POP
movies.pop(4)
print("\nRemoved from a specific postion: ",movies)

#REVERSE
movies.reverse()
print("\nReversed List: ",movies)

#SORT
movies.sort(reverse=True)
print("\nSorted Desc order: ",movies)

#Min(),Max(),Sum()
minm = min(movies)
print('\nMinimum: ',minm)
maxn = max(movies)
print('Maximum: ',maxn)
digits = [1,6,55,2,34,8]
summ = sum(digits)
print('Total Sum: ',summ)

#INDEX
index = movies.index('Mad men')
print('\nIndex: ',index)

#ENUMERATE
y = enumerate(movies)
print(list(y))

#JOIN
D = '--'
Str = D.join(movies)
print('\nAfter joining: ',movies)

#SPLIT
Str = "Song of Ice and Fire"
print('\nAfter Splitting: ',Str.split())

