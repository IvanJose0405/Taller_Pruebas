def test_Hello():
    saludo = Hello()
    assert saludo == "HELLO FASTAPI"
    
def test_Isprime():
    numero=Isprime(10)
    assert numero == False
    
def test_Fibonacci():
    numero=Fibonacci(7)
    assert numero == 13