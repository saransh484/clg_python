#TUPLES
tuple1 = (85, 4.98, 86, 25.04, 37, 35, 24.4, 70, 15)
tuple2 = (356, 94, 2)

#SLICING
_slice = tuple1[3:5]
print('\ntuple[start:stop]: ',_slice)
_slice = tuple1[5:]
print("The end index isn't defined: ",_slice)
_slice = tuple1[-8:-4]
print('Defined with negative values: ',_slice)

#CONCATENATION
tuple3 = tuple2 + tuple1
print('\nThe new tuple after concatenation: ',tuple3)

#REPETITION
str='She was young the way an actual young person is young.'
str.count('young')
str2='young'
str.count(str2)
print("\nRepetition of word '{}': ".format(str2),str.count('young'))

#APPEND and REMOVE
t = (45,67,36,85,32)
cnvrt = list(t)
print(cnvrt)
print (type(cnvrt))
cnvrt.append (787)
print(cnvrt)
t = tuple(cnvrt)
print ('\nTuple after appending: ',t)

numTuple = (13, 21, 54, 4, 7, 39, 15, 23, 12)
print ("\nTuple Items = ", numTuple)
numTuple = numTuple [:3] + numTuple [4:]
print ("\nAfter Removing 4th Tuple Item = ", numTuple)
numTuple = numTuple [:5] + numTuple [7:]
print ("\nAfter Removing 5th and 6th Tuple Item = ", numTuple)
