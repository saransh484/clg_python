#slicing

string = "Programming with python"

sl = slice(2,7)
print("2nd to 7th letter of string'",string ,"'is : ",string[sl])

#slicing with +ve step 
sl = slice(2,7,2)
print("2nd to 7th letter with step 2 of string'",string ,"'is : ",string[sl])

#slicing with -ve step
sl = slice(7,2,-2)
print("negative slicing of 7nd to 2nd letter with step -2 of string'",string ,"'is : ",string[sl])

#reverse string using slice
sl = slice(-1,6,-1)
print("negative slicing of -1st to 6th letter with -1 step of string'",string ,"'is : ",string[sl])
