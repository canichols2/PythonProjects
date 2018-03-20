class customExc(Exception):
   '''Raise just to test exceptions. and how args work in them.'''
def end():
   exit()
def menu():
   print("\nPlease select a value:"
   + "\n\ta|arr|array:  Run Arr's tests"
   + "\n\tc|classes:    Test classes"
   + "\n\te|exceptions: Test exceptions"
   + "\n\tq|exit|quit:  quit"
   )
   return input()

def array():
   print("Inside the array block")

def classes():
   print("inside the classes block")
def exception():
   print("Inside Exceptions block\nGoing to throw exception")
   raise customExc("My Text Exception")
def main():
   options = {
      "arr":array,
      "a":array,
      "c":classes,
      "classes":classes,
      "e":exception,
      "exceptions":exception,
      "exc":exception,
      "except":exception,
      "exit":end,
      "q":end,
   }
   while(1):
      choice = menu()
      try:
         options[choice]()
      except customExc as e:
         print("Caught customExc: "+e.args[0])
      except:
         print("I'm sorry, that isn't a choice. Please try again")
      
      
main()