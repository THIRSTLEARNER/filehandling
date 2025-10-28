def simple_decorator(func):
   def wrapper():
       print("Before the function call")
       func()
       print("After the function call")
   return wrapper
@simple_decorator
def greet():
   print("Hello, World!")
greet()


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())


def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())


def lower(func):
   def inner():
      return func().lower()
   return inner

@lower
def otherfuntion1():
   return "IAM SPEED"

print(otherfuntion1())