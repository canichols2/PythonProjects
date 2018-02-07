def filename():
   return input("filename: ")


def countFile(filename):
   words = 0
   lines = 0
   file = open(filename,'rb')
   contents = file.readlines()
   file.close();

   print("the file contains ",lines," lines and ",words," words.")

countFile(filename())