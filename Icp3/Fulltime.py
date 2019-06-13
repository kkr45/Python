import Inheritance
class fulltime(Inheritance.employee):
    def __init__(self, name, family, salary, dept):
        Inheritance.employee.__init__(self, name, family, salary, dept)
        self.type = "fulltime"


emp3 = fulltime("sk", "gamer", 120000, "creative")
print(emp3.type)


