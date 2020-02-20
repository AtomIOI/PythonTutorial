[![Build Status](https://travis-ci.org/AtomIOI/PythonTutorial.svg?branch=master)](https://travis-ci.org/AtomIOI/PythonTutorial)
#Basics in Python
### This is a simple tutorial explaining some of the basic programming concepts using Python 
### All code used as an example is also in a separate python file in the "Tutorial" folder with the name of the concept as well as tests under the "Tests" folder that demonstrate functionality.

# Encapsulation 
## Encapsulation is achieved when each object keeps its state private, inside a class. Other objects don’t have direct access to this state. Instead, they can only call a list of public functions — called methods.
### An example of this in python would be a banking application. You want the customer to be able to check their balance, deposit and withdraw. 
### However, you must ensure that they cannot take more than they have in the account. To accomplish this encapsulation requires that to preform these tasks they must call functions of the bank class that would handle the cases with proper checks.
### Here we create the bank class with a private variable called balance which is initialized to 0 when the object is created: 
```
class Bank:
    def __init__(self):
        self.__balance = 0
```
### Then we add the methods for accessing the variable:
```
class Bank:
    def __init__(self):
        self.__balance = 0

    def checkBalance(self):
        return self.__balance

    def deposit(self, add):
        self.__balance = self.__balance + add
        return "Success"

    def withdraw(self, sub):
        if self.__balance - sub > 0:
            self.__balance = self.__balance - sub
            return "Success"
        else:
            return "Insufficient balance"
```
### If we attempted to create a Bank object and we attempted to change the balance directly it would fail:
```
banker = Bank()
banker.balance = 100
print(banker.checkBalance())
```
### That code would print out this:
```
0
```
### But if we used the method provided:
```
banker = Bank()
print(banker.checkBalance())
print(banker.deposit(100))
print(banker.checkBalance())
```
### Then we get this output:
```
0
Success
100
```
### Finally thanks to encapsulation we can protect against overdrawing:
```
banker = Bank()
print(banker.checkBalance())
print(banker.withdraw(100))
print(banker.checkBalance())
```
### The method made the proper checks and returned that we had an insufficient balance:
```
0
Insufficient balance
0
```

# Abstraction
## Abstraction means that each object should only expose a high-level mechanism for using it. This mechanism should hide internal implementation details. It should only reveal operations relevant for the other objects.
### Following the bank example, abstraction would mean that we can create a payment method that pays all the due bills.
### This method must check the list and assign payments to each company individually but thanks to abstraction the user only has to call one function.
### We reuse the Bank class and add the payBills method and a constant to keep track of the bills:
```
class Bank:
    def __init__(self):
        self.__balance = 0
        self.__bills = 100
    .
    .
    .
    def payBills(self):
        if self.__balance - self.__bills < 0:
            return "Insufficient balance to pay bills, please make a deposit first"
        else:
            self.withdraw(self.__bills)
            self.__bills = 0
            return "Bills paid"
```  
### Now we can call one function to pay bills:
```
bank = Bank()
print(bank.payBills())
```
### Which will print this, since we have a 0 balance to start:
```
Insufficient balance to pay bills, please make a deposit first
```
### But if we make a deposit first:
```
bank = Bank()
bank.deposit(200)
print(bank.payBills())
print(bank.checkBalance())
```
### Then we get this output:
```
Bills paid
100
```

# Inheritance
##  Inheritance means that you create a (child) class by deriving from another (parent) class. The child class reuses all fields and methods of the parent class (common part) and can implement its own (unique part).
### Inheritance is most simply explained by using people as an example. In this we go from the general person, which has first and last name attributes, to a specialized person with new attributes.
### We first create the Person class with first and last name attributes and a print name method:
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    return self.firstname + " " + self.lastname
```
### Then we can create a child class which inherits from Person:
```
class Student(Person):
  pass
```
### The class is currently identical to the parent "Person" class, but we are going to override the constructor with our own so that we can add a graduation year:
```
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
```
### Now if we created a person object and asked it to say it's name the student object would be able to do the same:
```
person = Person("John", "Smith")
print(person.printname())
student = Student("Adam", "Kovic", 2019)
print(student.printname())
print(student.graduationyear)
```
### This would have the output, we inherited the lname and fname attributes from the Person class:
```
John Smith
Adam Kovic
2019
```

# Polymorphism
## Polymorphism gives a way to use a class exactly like its parent so there’s no confusion with mixing types. But each child class keeps its own methods as they are.
### Polymorphism uses the idea of an interface, which is basically a skeleton class which contains methods that you implement in each child class.
### The largest benfit to this concept is that you can mix several types in a list but still perform the method on the list since each object will use its own implementation.
### The Person class example from the last topic can be reused here, in this case we will use the printinfo method as an example:
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printinfo(self):
    return self.firstname + " " + self.lastname
```
### We create a new class called doctor that inherits from Person, this time we override the printinfo method to include "Dr." when printing a doctor objects info:
```
class Doctor(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)

  def printinfo(self):
    return "Dr." + self.firstname + " " + self.lastname
```
### If we create a list with both Person and Doctor objects then ask to printinfo for that list:
```
doctor = Doctor("James", "Willems")
doctorTwo = Doctor("Elyse", "Willems")
person = Person("Alanah", "Pearce")
personTwo = Person("Jacob", "Fullerton")

nameList = [doctor, person, doctorTwo, personTwo]
for obj in nameList:
    print(obj.printinfo())
```
### We will get the correct output for each object specification:
```
Dr.James Willems
Alanah Pearce
Dr.Elyse Willems
Jacob Fullerton
```