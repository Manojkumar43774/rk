
# Q1: Write a Python program that takes a user's name as input and prints a greeting message.
# name= input("Enter name:")
# print(f"Hello {name}, Good Morning")

# Q2: Write a Python program that takes two numbers as input and prints their sum.
# value1= int(input("Enter value1:"))
# value2= int(input("Enter value2:"))
# print(value1+value2)

# Q3: Write a Python program that takes two numbers as input and swaps their values.
# value1= int(input("Enter value1:"))
# value2= int(input("Enter value2:"))
# value1, value2= value2, value1
# value1=5
# value2=9
# print(f"After swap value1:{value1} and value2:{value2}")
# Ques1: Write a program that takes an integer as input and prints whether it is odd or even.
# a=int(input("Enter number:"))
# if a%2==0:
#     print("Even")
# else:
#     print("odd")

# Ques2:Write a program that takes a number as input and prints whether it is positive, negative, or zero.
# a=int(input("Enter number:"))
# if a==0:
#     print("Zero")
# elif a<0:
#     print("Negative")
# else:
#     print("Positive")

# Ques3:Write a program that asks the user for their marks and prints "Pass" if marks are >=40, otherwise print "Fail".
# marks = float(input("Enter your marks: "))
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")
# Qus1 : write a program  take user input as integer then cast into string  then compare '8' if match then true else false.
# Uplaksha Kumar
# Qus1 : write a program user input is int, whether divisble by 4 if divisible then true else false.
# Akshara
# Qus1 : write a program to check whether greater than 2  yes or no.
# Mihir
#  or, and , not
# Q1: Write a program to check if a given number is between 10 and 50.
# a=int(input("Number="))
# if a>=10 and a<=50:
#     print('Yes')
# else: 
#     print('No')
# Q2:Write a program that takes a number as input and prints "Valid" if it is both even and divisible by 5, otherwise prints "Invalid".
# a=5
# b=7
# comparison operator:
# 1. a==b  No
# 2. a!=b  Yes
# 3. a>b   No
# 4. a<b   Yes
# 5. a>=b  No
# 6. a<=b  yes

# Q2:Write a program that takes a number as input and prints "Valid" if it is both even and divisible by 5, otherwise prints "Invalid".
# a= int(input("Enter number:"))
# if a%2==0 and a%5==0:
#     print("valid")
# else:
#     print("Invalid")

# Q3:A person is eligible to vote if they are 18 or older. Write a program that checks if a user can vote.
# a=int(input("Age:"))
# if a>=18:
#     print("Can vote")
# else:
#     print("can't vote")

# Q4:Write a program that prints "Outside Range" if a given number is not between 100 and 200.
# a=int(input("Number:"))
# if a>=100 and a<=200:
#     print("In Range")
# else:
#     print("Out Range")

# for i in range(1,11):
#     print(i)
# i=0
# while i<10:
#     print(i)
#     i+=1

# Q1:Write a program to print all even numbers from 1 to 20 using a for loop.
# for i in range(1,20):
#     if i%2==0:
#         print(i)

# Q3:Write a program that takes an input N and calculates the sum of numbers from 1 to N using both for and while loops.
# n=int(input("enter number: "))
# sum=0
# for i in range(1,n):
#     sum=sum+i
# print(sum)

# n=int(input("enter number: "))
# sum=0
# i=0
# while i<n:
#     sum=sum+i
#     i+=1
# print(sum)

# Q4:Write a program that calculates the factorial of a number using both for and while loops.
# n=int(input("enter number: "))
# fact=1
# for i in range(1,n+1):
#     if i==4:
#         pass
#     fact=fact*i
# print(fact)

# n=int(input("enter number: "))
# fact=1
# i=1
# while i<n+1:
#     fact=fact*i
#     if i>=24:
#         break
#     i+=1
# print(fact)
    #  0, 1,  2  ,3      ,4
    #  [1,'m','a','87687','hello everyone']

# value=[1,'m','87687','hello everyone',87687,42,3]
# value.append(20)   #add value at last
# value.insert(2, 'a')  # insert value at index define is 2
# value.extend([14,5765,'akhit']) #add multiple values

# value.remove(1)   #remove the specified value
# value.pop()   #remove the last element from list
# value.pop(2)  #remove the value from index
# # print(type(value[1]))
# value=[1,2,3,4,5,6,7,8,9,9,0,1]
    #  0,1,2,3,4
# Q1: Write a code to print value from 0 to 5 by skipping 3 values.
# print(value[0:5:4])
# Q2: Code to reverse list
# print(value[::-2])
# Q3: Code to iterate the list 5 to till end.
# for i in range(5,len(value)):
#     print(value[i])


# Q1: Sum Items in List:
# value=[1,2,3,4,5,6,7,8,9,9,0,1]
# sum=0
# for i in range(0,len(value)):
#     sum=sum+value[i]
# print(sum)

# 2: Multiply Items in List
# value=[1,2,3,4,5,6,7,8,9,9,1]
# multiply=1
# for i in range(0,len(value)):
#     multiply=multiply*value[i]
# print(multiply)

# 3: Get Largest Number in List
# value=[1000,2,30,4999,5,61,7,8,9,9,10000]
# large=0
# for i in range(0,len(value)-1):
#     if value[i]>value[i+1] and value[i]>= large:
#         large=value[i]
#     elif value[i+1]>=large:
#         large=value[i+1]
# print(large)

# 4: Get Smallest Number in List
# print(min(value))
# min=value[0]
# for i in value:
#     if i<min:
#         min=i
# print(min) 

# 5: Count Strings in List
# cnt=0
# for i in value:
#     if type(i)==str:
#         cnt=cnt+1
# print(cnt)

# 6: Remove Duplicates from List
# print(list(set(value)))


# 7: Remove Even Number from List
# value=[1000,2,30,4999,5,61,7,9,9,10000]
# new_list=[]
# for i in value:
#     if i%2!=0:
#         new_list.append(i)
# print(new_list)

# 8: Convert List to Strings
# value=['m','a','n','o','j']
# for i in range(0,len(value)):
#     if type(value[i])==int:
#         value[i]=str(value[i])

# str=''.join(value)
# print(str)

# 9: Find Index of List Item
# value=[1000,2,30,4999,5,61,7,'9',9,10000]
# select_ele=input("enter from list:")
# for i in range(0,len(value)):
#     if value[i]== select_ele or value[i]== int(select_ele):
#         print(i)

# 10: Split List by First Characters
# value=[1000,2,30,4999,5,61,7,'9',9,10000]
# for i in range(0,len(value)):
#     if type(value[i])== str:
#         index=i
#         break
# split_list1=value[0:index]
# split_list2=value[index:]
# print(split_list1,split_list2)

# Tuple:
# immutable and order element
# tp=('m',2,'me','k','l','m','n','o','p')
# print(type(tp))
# print(tp)
# print(len(tp))
# tp=(1)
# print(tp[2])

# indx= tp.index('m',0,len(tp))
# print(indx)

# 1. find the size of tuple?
# print(len(tup))

# min and max element in tup?
# tup=(1,2,3,4,5)
# min_tup= min(tup)
# max_tup= max(tup)
# print(min_tup,max_tup)
# min=tup[0]
# max=tup[0]
# for i in tup:

#     if i<=min:
#         min=i
#     if i>=max:
#         max=i

# print(min,max)


# tup=(1,2,3,4,5)
# tup2=(6,7,8)
# s=tup+tup2
# print(s)

# set={1,2,67}
# print(set)


# list1=[10309,['m','a'],'n',['o'],['j',['k','u'],['m','a'],'r']]

# def flatten(a):
#     emp_lis=[]
#     for i in a:
#         # if isinstance(i, list):
#         if type(i)==list:
#             emp_lis.extend(flatten(i))
#         else:
#             emp_lis.append(i)
#     return emp_lis

# k=flatten(list1)
# print(k[0:])

# di={'Emp':{'Name':'Manoj'}}
# print(type(di))



# d1={'a':1,'b':2}
# d2={'b':3,'d':4}
# d1.update(d2)
# print(d1)

# dict1={'a':1,'b':2,'b':3,'d':4}
# list_key=list(dict1.keys())
# list_values=list(dict1.values())
# print(list_key,list_values)

# def flatten_dict(d, parent_key='', sep='_'):
#     flatten={}
#     for k,v in d.items():
#         new_key=f"{parent_key}{sep}{k}" if parent_key else k
#         if isinstance(v,dict):
#             flatten.update(flatten_dict(v,new_key,sep))
#         else:
#             flatten[new_key]=v
#     return flatten


# nested_dict={'a':1,'b':{'c':2,'d':{'e':3,'f':4}}}
# print(flatten_dict(nested_dict))


# def recursion(fact):
#     if fact==0 or fact==1:
#         return 1
#     else:
#         return fact*recursion(fact-1)

# fact=5
# print(recursion(fact))

# add= lambda x,y: x+y
# print(add(5,2))

# num=[1,2,3,4]
# square=list(map(lambda x:x**2,num))
# print(square)

# sq=lambda x:x**2*3
# print(sq(5))

# r, w ,a , r+
# open close

# file=open('file.txt','r')
# for line in file:
#     print(line.strip())
# file.close()

# with open('file.txt','r') as file:
#     cont=file.read()
#     print(cont)

# file=open('file.txt','w')
# file.write("Hello, We are Good.\n")
# file.write("We are learning python")
# file.close()

# with open('file.txt','w') as file:
#     file.write("Hello, this is another approach.\n")


# file=open('file.txt','a')
# file.write("Hello, We appended.\n")
# file.write("We are learning python")
# file.close()


# with open('file.txt','a') as file:
#     file.write("Hello, this is another approach for append.\n")

# file=open('file.txt','r+')
# file.write("Hello, We appended.\n")
# file.write("We are learning python")
# for line in file:
#     print(line.strip())
# file.close()

# with open('file.txt','r+') as file:
#     file.write("Hello, this is another approach for append.\n")
#     cont=file.read()
#     print(cont)

# Context Manager
# class conteKeyword:
#     def __init__(self, filename,mode):
#         self.filename=filename
#         self.mode=mode
#         self.file=None
#     def __enter__(self):
#         self.file=open(self.filename,self.mode)
#         return self.file
#     def __exit__(self,exc_type,exc_value,traceback):
#         if self.file:
#             self.file.close()
# try:        
#     with open('Creating_file.txt','w') as file:
#         file.write("Hello,File Created.\n")
#         # cont=file.read()
#         # print(cont)
# except FileNotFoundError:
#     print("File not found, Manoj")

# try:
#     x=10
#     x=1/10
#     # x=int("abc")
# # except (ZeroDivisionError,ValueError) as e:
# except Exception as e:
#     print(f"cannot divide by zero:{e}")
# else:
#     print("Run Successfully")
# finally:
#     print("closing the program")
# def divide(a,b):
#     if b==0:
#         raise Exception("Division error")
#     return a/b

# print(divide(10,10))

# class arrore(Exception):
#     def __init__(self,message):
#         self.message=message
#         super().__init__(message)
# b=0
# if b==0:
#     raise arrore("something went wrong")

# class car:
#     price=40000
#     def __init__(self, brand,model):
#         self.brand=brand
#         self.model=model

#     def display(self):
#         print(f"car: {self.brand}{self.model}")

# car1=car("toyota","fortuner")
# car3=car("maruti","ciaz")

# car3.brand='honda'
# car3.display()
# # print(car3.price)
# car3.price=500000
# print(car3.price)

# __init__ 

# 1.inheritance
# 2.method overriding and overloading
# 3.encapsulation and abstraction
# 4.self keyword and class vs instance methods

# modules:
# 1. creating and import modules
# 2. standard lib modules
# 3.third
# 4.venv 

# single inheritance:
# class parent:
#     def display(self):
#         print("parent")

# class child(parent):
#     def show(self):
#         print("child")

# obj= child()
# obj.display()
# obj.show()

# #multiple inheritance
# class parent_f:
#     def display_f(self):
#         print("father")

# class parent_m:
#     def display(self):
#         print("mother")

# class child(parent_f,parent_m):
#     def show(self):
#         print("child")

# obj= child()
# obj.display_f()
# obj.display()
# obj.show()


#multilevel inheritance
# class parent_gf:
#     def display_gf(self):
#         print("grandfather")

# class parent_f(parent_gf):
#     def display(self):
#         print("father")

# class child(parent_f):
#     def show(self):
#         print("child")

# obj= child()
# obj.display_gf()
# obj.display()
# obj.show()

# hierarchical inheritance
# class parent:
#     def display_gf(self):
#         print("father")

# class child1(parent):
#     def display(self):
#         print("child1")

# class child2(parent):
#     def show(self):
#         print("child2")

# obj= child1()
# obj2=child2()
# obj.display_gf()
# obj2.display_gf()
# obj.display()
# obj2.show()

# hybrid inheritance
# class grandfather:
#     def grandfather(self):
#         print("grandfather")

# class father(grandfather):
#     def father(self):
#         print("father")

# class mother(grandfather):
#     def mother(self):
#         print("mother")

# class child(father,mother):
#     def show(self):
#         print("child")

# obj= child()
# obj.grandfather()
# obj.father()
# obj.mother()
# obj.show()


# method overriding:
# class father():
#     def father(self):
#         print("father")

# class child(father):
#     def father(self):
#         super().father()
#         print("child")

# obj= child()
# obj.father()

# method overloading
# class method_overload:
#     def show(self, name=None):
#         if name is not None:
#             print(f"hello,{name}")
#         else:
#             print("hello bro")

# obj= method_overload()
# obj.show()
# obj.show('Manoj')

# Encapsulation
# class bank:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder #public variable
#         self._balance=balance #protected variable
#         self.__pin='1234' #private variable

#     def deposit(self,amount):
#         self._balance +=amount
#         print(f"Deposited {amount}. New balance: {self._balance}")

#     def __get_pin(self):
#         return self.__pin
    
# account=bank('Aman',1000)

# print(account.account_holder)
# print(account._balance)
# # print(account.__pin)
# print(account._bank__pin)

# Abstraction
# from abc import ABC, abstractmethod
# class vehcile(ABC):
#     @abstractmethod
#     def start(Self):
#         pass

#     @abstractmethod
#     def stop(self):
#         print("stopped")
#         pass

# class car(vehcile):
#     def start(self):
#         print("car is start")

#     def stop(self):
#         print("car is stop")

# obj=car()
# obj.start()
# obj.stop()

# importing module
# import module_cr
# from module_cr import greet,add,PI
# from module_cr import *
# print(greet("Manoj"))
# print(add(5,10))
# print(PI)

# builtin standard module
# import math
# print(math.sqrt(16))

# python virtual env
# python -m venv myenv

# 1.Write a lambda function to add 10 to a given number.
# add_10 = lambda x,y: x +y+ 10
# print(add_10(5,4))  


# 2.Write a lambda function to multiply two numbers.
# multiply = lambda x,y: x *y
# print(multiply(5,4))  

# 3.Write a lambda function to find the maximum of two numbers.
# max_var = lambda x,y: x if x>y else y
# print(max_var(5,4))  

# 4.Write a lambda function that returns True if a number is even, otherwise False.
# max_var = lambda x: True if x%2==0 else False
# print(max_var(9)) 

# 5.Use a lambda function with filter() to get all even numbers from a list.
# number=[1,2,3,4,5,6,7,8,9]
# even_num= list(filter(lambda x:x%2==0, number))
# print(even_num)

# 6.Use a lambda function with map() to get the squares of all elements in a list.
# number=[1,2,3,4,5,6,7,8,9]
# even_num= list(map(lambda x:x**2, number))
# print(even_num)

# 7.Write a lambda function to check if a given string contains a vowel.
# vowel=lambda v: any(c in "aeiouAEIOU" for c in v)
# print(vowel("hello"))
# print(vowel("hhhh"))


# Recursion
# write a function to calculate factorial of a number.
# def fct(n):
#     if n==0 or n==1:
#         return 1
#     return n*fct(n-1)
# print(fct(5))
# WAP to find nth fibonacci number.
# def fib(n):
    # iohinjkhnjknjk
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return fib(n-1)+fib(n-2)

# print(fib(3))
# print(fib(4))
# print(fib(5))
# Wap to find the sum of digits of a number.
# def summ(n):
#     if n==0:
#         return 0
#     return (n%10) + summ(n//5)

# print(summ(1457))

# print(145%10)
# print(145//10)
