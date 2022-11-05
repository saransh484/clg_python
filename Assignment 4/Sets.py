#SETS

#UNION 
a = {"I", "Went","home","early"}
b = {"as", "I","was", "cold."}
c = a.union(b)
print('After union operation on a & b: ',c)

#INTERSECTION
x = {"His", "house", "is", "similar", "to", "mine."}
y = {"They", "are", "very", "similar."}
z = x.intersection(y)
print('\nAfter intersection operation on x & y: ',z)

#SYMMETRIC DIFFERENCE
set_a = {1, 5, 4, 7, 2}
set_b = {8, 3, 5, 1, 9}
print('\nSymmetric difference: ',set_a.symmetric_difference(set_b))

#CONVERT LIST TO SET
List = ['Pagani', 'Bentley', 'Cadillac']
s = set(List)
print('\nList to Set: ',s)
