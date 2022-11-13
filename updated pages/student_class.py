class student:
    def __init__ (self,n,r,m):
        self.name=n
        self.rno=r
        self.branch=m
    def display(self):
        print("name", self.name)
        print("rollno:",self.rno)
        print("Branch:",self.branch)
              
stl=student("saransh bhatnagar",20,"cse-ai")
st2=student("arnav khare",20,"bsc")
st3=student("ayush kumar",22,"animation")
              
stl.display()
st2.display()
st3.display()
