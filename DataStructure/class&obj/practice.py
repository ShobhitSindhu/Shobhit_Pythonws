class school:
    def name(self):
        print("shobhit")
        
s1 = school()
s1.name()
'''_________________________________________________________________'''

'''Self Concept in the class'''

class school:
    def __init__(self,fullname):
        self.name = fullname
        print("adding new students in db....")
s1 = school("shobhit")
print(s1.name)
''' Summary = Self you call anything like abcd etc and __init__ is constructor its get called even if you dont initialize it'''
'''------------------------------------------------------------------------'''
class school:
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name 
        print("setting up the names....")
    def first_Name(self):
        print(self.first)
    def last_Name(self):
        print(self.last)
    @staticmethod
    def hello():
        print("___completed___")
s1 = school("Shobhit","Sindhu")
s1.first_Name()
s1.last_Name()
s1.hello()
'''------------------------------------------------------------------------'''
