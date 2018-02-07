def filename():
   return input("filename: ")

def countFile(filename):
   words = 0
   lines = 0
   file = open("test.txt",'rb')
   for line in file:
      lines += 1;
      words += len(line.split())
   file.close();
   print("the file contains ",lines," lines and ",words," words.")

countFile(filename())