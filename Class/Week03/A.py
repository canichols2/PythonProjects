class Student:
   def __init__(self):
      self.first="";
      self.last="";
      self.id=0;
   def __init__(self,first):
      self.first=first;
      self.last="";
      self.id=0;
   def __init__(self,first,last):
      self.first=first;
      self.last=last;
      self.id=0;
   def __init__(self,first,last,id):
      self.first=first;
      self.last=last;
      self.id=id;

def getInfo():
   first = input("First Name> ")
   last = input("Last Name> ")
   id = int(input("ID> "))
   return Student(first,last,id)
   
def displayStudent(s):
   print()
   print("Your information:")
   print(s.id,"-",s.first,s.last)

def main():
   displayStudent(getInfo())

main();