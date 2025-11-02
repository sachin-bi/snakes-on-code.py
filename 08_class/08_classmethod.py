class Example:

    schoolName = "APC PUBLIC SCHOOL"

    def __init__(self, stdName):
        self.stdName = stdName

    @classmethod
    def changeSchool(cls, schName):
        cls.schoolName = schName
        print(f"school changed to {cls.schoolName}")

    @staticmethod
    def greet(name, car):
        print(f"Hi i'm {name} and i like {car}")

    def stdData(self):
        print(f"current std name is {self.stdName} and school is {self.schoolName}")


obj = Example("sachin")
obj.greet("Rama","Speed T4")
obj.stdData()
obj.changeSchool("xyz school")

obj2 = Example("ram2")
obj2.stdData()