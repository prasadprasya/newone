'''def SI(p,t,r):
    return (p*t*r)/100

x, y, z = input("Enter a three value: ").split()
x=int(x)
y=int(y)
z=int(z)
print(SI(x,y,z))'''


'''A = P(1 + R/100) t 
Compound Interest = A – P
'''
#Armstrong
def armstrong(n):
	number = str(n)

	n = len(number)
	output = 0
	for i in number:
	    output = output+int(i)**n    #output = output+pow(int(i),n)

	if output == int(number):
		return(True)
	else:
		return(False)
x = input("Enter a number:")		
print(armstrong(x))
print(len("123246546")) #len is not used for integers


#factorial recurrsion
def factorial(n):
    return 1 if n==0 or n==1 else n*factorial(n-1)
print(factorial(5))
# factorial with out recurrsion
def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while n>1:
            fact*=n
            n-=1
        return fact
print(factorial(5))


#list comprehension
numbers = ("1","5","8")
lst = [int(x) for x in numbers]
print(lst)

x, y, z = [int(x) for x in input("Enter two value: ").split()]

print(x,y,z)

#Area of circle
import math
def Area(r):
    PI = math.pi
    return PI*(r**2)
print(Area(5))

#Generate prime numbers between two numbers
start = int(input("Start from:"))
end = int(input("End at:"))
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
    
#logic in prime number
def prime(n):
    if n>1:
        for i in range(2,n):
            if(n % i==0):
                return ("{} is not a prime number".format(n))
                
            
            else:
                return ("{} is a prime number".format(n))
    else:
        return ("number should not be 0 or negative")
print(prime(40))

#fibonacci using recurrsion
def fibonacci(n):
    if n<=0:
        print("invalid")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else: 
        return (fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(15))

'''#fibonacci using formula
fib=(((1+math.sqrt(5))**n)-((1-math.sqrt(5))**n))/((math.sqrt(5)*2**n))
# check given number fibonaci or not'''
def perfect_square(x):
    if x>0:
        s = math.sqrt(x)
    return s*s == x
def is_fibonacci(n):
    if perfect_square(5*n**2+4) or perfect_square(5*n**2-4):
        return "yes"
    else:
        return "No"
print(is_fibonacci(377))

#decorator 
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
@smart_div
def div(a,b):
    return(a/b)
print(div(2,4))

'''iterator'''
fruits=[1,2,5,8,6]
'''We can also use a for loop to iterate through an iterable object:'''
y=iter(fruits)
print(next(y))
print(next(y))

'''iterator class'''
class range1:
  def __init__(self,n):
    self.n=n
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= self.n:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
for i in range1(20):
    print(i)


'''generater class'''

class range1:
  def __init__(self,n):
    self.n=n
  def __iter__(self):
    self.a = 1
    yield self

  def __next__(self):
    if self.a <= self.n:
      x = self.a
      self.a += 1
      yield x
    else:
      raise StopIteration
for i in range1(20):
    print(i) 
    
'''generater'''
def gen():
    for i in range(20):
        yield i
print(gen())  
x = gen()
for j in x:      
    print(j)


'''generator that reverses a string'''
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
print(rev_str('hello'))
# For loop to reverse the string
for char in rev_str("hello"):
    print(char,end='')
    

'''or'''

x='prasad'
print(x[::-1])