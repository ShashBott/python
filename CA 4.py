class book():
    
    def __init__(self,name,writer,word_length,fontsize):
        self.name=name
        self.writer=writer
        self.word_length=word_length
        self.fontsize=fontsize

    def display(self):
        print(self.name)
        print(self.writer)
        print(self.word_length)

    def modification(self):
        setattr(b1,"name",input("Enter new name "))
        setattr(b1,"writer",input("Enter new writer "))
        setattr(b1,"word_length",int(input("Enter new word length "))) 

    def cal(self):
        if self.fontsize==12:
            self.pages=self.word_length/300
            print(self.pages)
            return(self.pages)
        else:
            print("No other cases are accepted ")
  

b1=book("hariputtar","saxena",12000,12)
print(type(b1))
b1.display()
print("\nDo you want to modify the inputs? ")
inp=input("\nEnter Y/N:")
if inp.casefold()=="y":
   b1.modification()
b1.display()
b1.cal()
