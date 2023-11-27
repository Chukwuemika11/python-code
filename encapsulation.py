class student:
    def __init__(self,name, RegNo, Dept):
        self.name = name
        self.RegNo = RegNo
        self.Dept = Dept

    def  show(self):
        print (f' Name: ' % self.name)    