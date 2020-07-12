class className:
    # a = 2
    # b = 6
    def __init__(self,**kwargs):
        self.Data = kwargs   # self.Data = {'a':2,'b':6}
        
    def SUM(self,x,y):
        return (x + y + self.Data['b'])
    

Data = className(a=2,b=6)
Out = Data.SUM(1,2)
print(Out)