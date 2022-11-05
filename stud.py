class Student:
    def getStudentDetails(self):
        self.rollno=input("Enter Roll Num : ")
        self.name = input("Enter Name : ")
        self.physics =int(input("Enter Physics Marks : "))
        self.chemistry = int(input("Enter Chemistry Marks : "))
        self.maths = int(input("Enter Maths Marks : "))

    def printResult(self):
        self.percentage = (int)( (self.physics + self.chemistry + self.maths) /3 ); 
        print(self.rollno,self.name, self.percentage)

S1=Student()
S1.getStudentDetails()

print("Result : ")
S1.printResult()
