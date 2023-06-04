class students():
    global p
    p=1.10

    def __init__(self,name,surname,batch,marks):
        self.name=name
        self.surname=surname
        self.batch=batch
        self.marks=marks


    def fullname(self):
        return '{} {}'.format(self.name,self.surname)
    
    def display(self):
        print("Email is : " +self.name+"."+self.surname+"@upes.com")

    def new(self):
        self.marks=self.marks*p
        print(self.marks)
        
        
cls=students("shashwat","saxena",36,88)
print("Full Name of student is: ")
print(cls.fullname())
cls.new()
cls.display()

