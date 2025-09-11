class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)
st1=Student("sru","5b5",87)
st1.display()
st2=Student("abd","543",67)
st2.display()