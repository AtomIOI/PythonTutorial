#This is a simple tutorial explaining some of the basic programming concepts using Python 
# Encapsulation
## Encapsulation is achieved when each object keeps its state private, inside a class. Other objects don’t have direct access to this state. Instead, they can only call a list of public functions — called methods.
### An example of this in python would be a banking application. You want the customer to be able to check their balance, deposit and withdraw. 
###However, you must ensure that they cannot take more than they have in the account. To accomplish this encapsulation requires that to preform these tasks they must call functions of the bank class that would handle the cases with proper checks.
### Here we create the bank class with a private variable called balance which is initialized to 0 when the object is created: 
```
class Bank:
    def __init__(self):
        self.balance = 0
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
        return "success"

    def withdraw(self, sub):
        if self.__balance - sub > 0:
            self.__balance = self.__balance - sub
            return "success"
        else:
            return "insufficient balance"
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
success
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
insufficient balance
0
```