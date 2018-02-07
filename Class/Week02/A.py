def prompt_number():
   num = 0;
   while True:
      num = int(input("Positive Number > "));
      if ( num >= 0 ):
         break;
   return num;

def compute_sum(n1,n2,n3):
   return n1 + n2 + n3;

def main():
   n1 = prompt_number();
   n2 = prompt_number();
   n3 = prompt_number();
   print("the sum is : ",compute_sum(n1,n2,n3));

if __name__ == "__main__":
    main()
   