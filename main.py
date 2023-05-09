from typing import Union

def Hello():
    return {"HELLO FASTAPI"}


def Isprime(numero): 
     for n in range(2,numero):
       if numero % n == 0:
          return False  
     return True


def Fibonnacci(numero: int):
     a=0
     b=1
     for n in range(0, numero):
        c=a+b
        a=b
        b=c
     return a