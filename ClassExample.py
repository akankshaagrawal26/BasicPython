class Student(object):
    def __init__(self,name,age):
        self.age = age
        self.name = name
        print("my name and age is :" + self.name + " " + str(self.age))

    def display(self):
        print("This is display method in student class")


class Employee:
    def __init__(self,cd):
        self.cd = cd
        print("Employee code is :" + " " + str(self.cd))

    def display(self):
        print("This is display method in employee class")


class Multiple(Employee,Student):
    def __init__(self):
        Student.__init__(self, 'akkki', 10)
        Student.display(self)
        #super(Multiple, self).__init__(100)
        super(Multiple, self).__init__(101)
        super(Multiple, self).display()
        Employee.__init__(self,10)


    def show(self):
        print("In show of multiple class")


mult = Multiple()
mult.display()
mult.show()





'''
The first class in order of inheritance ,that method only super methods are invoked
'''