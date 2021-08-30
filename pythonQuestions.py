1. What is the output of the following code? first = [1, 2, 3, 4, 5] second = first second.append(6) print(first) print(second)

# first = [1, 2, 3, 4, 5] 
# second = first
# second.append(6) 
# print(first) 
# print(second)


2.Will the do-while loop work if you don’t end it with a semicolon? *
# i = 1
# while True:
#    print(i)
#    i = i + 1
#    if(i > 5):
#       break
# The do-while loop which is not in python it can be done by the above syntax using while loop with break/if /continue statements.


3.show us how you’ll get the max alphabetical character from a string
# by usin max() function 
# string = "khand" 
# print max(string)

4.Can you name ten built-in functions in Python and explain each in brief? 
# abs()	Returns the absolute value of a number
# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true
# ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()	Returns the binary version of a number
# bool()	Returns the boolean value of the specified object
# bytearray()	Returns an array of bytes
# bytes()	Returns a bytes object
# callable()	Returns True if the specified object is callable, otherwise False
# chr()	Returns a character from the specified Unicode code.
# classmethod()	Converts a method into a class method

5. How to Get Current Python Directory?
# print(os.getcwd())

6.Python and multi-threading. Is it a good idea? List some ways to get some Python code to run in a parallel way. 
# Python doesn't allow multi-threading. Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your 'threads' can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread.

7.How do you keep track of different versions of your code? *
#  using a version control system like git/mercurial/svn

8.What is monkey patching and is it ever a good idea? *
# This is considered bad because it means that an object's definition does not completely or accurately describe how it actually behaves. Also, it creates a discrepancy between the original source code on disk and the observed behaviour.

9.What do these mean to you: @classmethod, @staticmethod, @property? *
# A class method takes cls as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
# When to use what?
# We generally use class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
# We generally use static methods to create utility functions.

10.Write a program to read and write the binary data using python? 
#  1.write the binary data
# file = open("document.bin","wb")
# sentence = bytearray("This is good".encode("ascii"))
# file.write(sentence)
# file.close()

#  2.read the binary data
# file=open("array.bin","rb")
# number=list(file.read(3))
# print (number)
# file.close()

11.Decorator vs generator. Where does the decorator fit well ? write fibonacci using decorator, class decorator. 
# Generator functions act just like regular functions with just one difference that they use the Python yieldkeyword instead of return . A generator function is a function that returns an iterator. A generator expression is an expression that returns an iterator. Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop.
# Code:
# def test_sequence():
#     num = 0
#     while num<10:
#         yield num
#         num += 1
# for i in test_sequence():
#        print(i, end=",")
# Output:
# 0,1,2,3,4,5,6,7,8,9

12. A decorator in Python is any callable Python object that is used to modify a function or a class. It takes in a function, adds some functionality, and returns it. Decorators are a very powerful and useful tool in Python since it allows programmers to modify/control the behavior of function or class. Decorators are usually called before the definition of a function you want to decorate. There are two different kinds of decorators in Python:
# Function decorators
# Class decorators
# Code:
# def test_decorator(func):
#     def function_wrapper(x):
#         print("Before calling " + func.__name__)
#         res = func(x)
#         print(res)
#         print("After calling " + func.__name__)
#     return function_wrapper
# @test_decorator
# def sqr(n):
#     return n ** 2
# sqr(54)
# Output:
# Before calling sqr
# 2916
# After calling sqr

13.How different is String in python2.7 vs python3 
# Python  2
# Print functional brackets are optional.
# Prefix string with u to make Unicode string.
# Division of integers always returns integer - 5/2=2.
# Raw_input () reads string.
# input() evaluates data read.
# generator .next().

# Python  3
# Print functional brackets are compulsory.
# String Unicode by default.
# Division of integers may result in the float - 5/2=2.5.
# Raw_input() not available.
# Input always reads the string.
# Next (generator).
# Py2 to a py3 utility.
# Dictionary .keys() and .values() returns a view not a list.
# Can no longer use comparison operators on non natural comparisons.

14.What is memoizing? Write fibonacci using it. 

# Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again

# def fib(n):
 
 
#     # Base case
#     if (n <= 1):
#         return n
 
#     # recursive calls
#     return fib(n - 1) + fib(n - 2)
 
# # Driver Code
# if __name__=='__main__':
#     n = 6
#     print (fib(n))
