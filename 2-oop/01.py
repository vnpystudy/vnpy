class Student():
    pass

class PythonStudent():
    name = None
    age = 18
    scourse = "Python"

    def doHomework(self):

        print("我在做作业")

        return None

yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)

yueyue.doHomework()
