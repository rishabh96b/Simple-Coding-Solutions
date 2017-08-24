def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
    
#driver program
def main():
  n=int(input()) #take intger input from user
  for i in range(2, n+1):
    if (isPrime(i)):
      print(i) 
      
#call driver function
main()

