highestRate = {}
lowestRate = {}
totalPrice=0
totalCount = 0

def printRate(rateObj):
   print ('{} ({}, {}) - ${}'.format(
      rateObj['utility_name'],
      rateObj['zip'],
      rateObj['state'],
      rateObj['comm_rate']))

def filename():
   return input("filename: ")


def countFile(filename):
   file = open(filename,'r')
   # read first line of file and get properties
   properties = file.readline().rstrip('\n').split(',')
   rates = []
   global highestRate
   global lowestRate
   global totalPrice
   global totalCount
   # for the rest, foreach through each line.
   for line in file.readlines():
      props = line.rstrip('\n').split(',')
      obj = {}
      for i in range(0,len(props)):
         obj[ properties[ i ] ] = props[i]
      if 'comm_rate' in highestRate :
         if( float(highestRate['comm_rate']) < float(obj['comm_rate'])):
            # print("new HighestRate:",obj)
            highestRate = obj
      else:
         highestRate = obj
      if 'comm_rate' in lowestRate :
         if( float(lowestRate['comm_rate']) > float(obj['comm_rate'])):
            # print("new LowestRate:",obj)
            lowestRate = obj
      else:
         lowestRate = obj
      totalPrice += float(obj['comm_rate'])
      totalCount += 1
      rates.append(obj)
   for x in rates[:5]:
      print(x)
      

   file.close();



countFile(filename())
# print("rateObj:",highestRate)
print()
print()
print()
print("The average commercial rate is:",totalPrice/totalCount)
print()
print("The highest rate is:")
printRate(highestRate)
print()
print("The lowest rate is:")
printRate(lowestRate)