## accuring property from parent class to child class
from OopsDemo import Calulator


class ChildImp(Calulator):
    num2 = 200

    def __init__(self):
        Calulator.__init__(self, 2,9)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj2 = ChildImp()
print(obj2.getCompleteData())