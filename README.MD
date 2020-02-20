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