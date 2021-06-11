def fibonacci(n):

  """
  this function has one parameter (n).
  this function should return the nth value
  in the fibonacci series.
  the function is implemented using recursion.

  each number in the fibonacci sequence 
  is the sum of the two numbers that precede it. 
  
  the sequence goes: 
  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

  """

  if n < 0:
    print("Incorrect")
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):

  """
 The first few Lucas numbers are

 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, ....

  """

  a = 2
  b = 1

  if(n == 0):
    return a

  for i in range(2, n + 1):
    c = a + b
    a = b
    b = c

    return b


