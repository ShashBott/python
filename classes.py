class students():

    def __init__(self,name,prog,batch,roll,sap,sem):
        self.name=name
        self.prog=prog
        self.batch=batch
        self.roll=roll
        self.sap=sap
        self.sem=sem

    def DataWrite(self):
        print(self.name)
        MyFile=open("MyData.txt","w")
        MyList=[self.name,self.prog,str(self.batch),str(self.roll),str(self.sap),str(self.sem)]
        print(MyList)
        MyFile.writelines(MyList)
        MyFile.close()
        MyFile=open("Mydata.txt","r")
        print(MyFile.read())
        MyFile.close()
        
    def display(self):
        print("My Name is : ",self.name)
  

cls=students("shashwat","SOCS",36,500096292,69,2)
cls.DataWrite()
cls.display()
