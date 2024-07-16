class Marksheet:
    def __init__(self,name,roll,mark):
        self.name = name
        self.roll = roll
        self.mark = mark

    def getmark(self):
        print(f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.mark}\n")

stu1 = Marksheet("Ranjith V",40,{"maths": 99, "English": 98, "Science": 99})
stu2 = Marksheet("Dakshin Kumar M",11,{"maths": 90, "English": 98, "Science": 99})
stu3 = Marksheet("Sankar A",46,{"maths": 90, "English": 98, "Science": 99})
stu1.getmark()
stu2.getmark()
stu3.getmark()
