
from math import*


class Prime:
    def __init__(self):
        pass


    def isPrime(self,n):
        num=n
        for s in range(2,n):
            if n%s ==0:
                num=num+1
        if num==n:
            return True
        else:
            return False
    def primeNumbers(self,start,stop):
        """Returns the sum of prime numbers from start to stop"""
        nlist=[]
        for s in range(start,stop):
            if self.isPrime(s):
                nlist.append(s)
        return len(nlist)


    def primeSieve(self,n):
        """Uses Sieve of Eratosthenes algorithm to return a list of
            prime numbers until n"""
        nlist=list(range(2,n+1))
        for rem in nlist:
            a=2
            while True:
                mult=rem*a
                if mult in nlist:
                    nlist.remove(mult)
                if mult>n:
                    break
                a=a+1
        
        return nlist
    
        

def main():
    "Example"
    a=Prime()
    print(a.isPrime(2))
    print(a.primeNumbers(2,200))
    print(a.primeSieve(100))

if __name__=='__main__':
    main()
    



    













