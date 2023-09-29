
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return(fibonacci(n - 1) + fibonacci(n - 2))

def printFibonacci(nterms):
  i = 1
  while i < nterms:
    print(fibonacci(i))
    i += 1