

# class Student:
#
#     counter = 1
#
#     def __init__(self, input_name):
#         self.roll = Student.counter
#         self.name = input_name
#
#         Student.counter += 1
#
#     def __str__(self):
#         return f"name :{self.name} roll num:{self.roll}"
#
#
#
#
#
# s1 = Student('A')
# print(s1)
#
# s2 = Student('b')
# print(s2)



# class Account:
#     counter = 1
#
#     def __init__(self, opening_balance = 100):
#         self.__balance = opening_balance
#         self.id = Account.counter
#         Account.counter +=1
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print('invalid transaction')
#
#     def withdraw(self, amount):
#         if amount > 0 and amount < self.__balance:
#             self.__balance -= amount
#         else:
#             print('invalid transaction')
#
#
#     def __str__(self):
#         return f"{self.id} has balance {self.__balance}"
#
#
#
# acc1 = Account()
# acc1.deposit(500)
# print(acc1)
#
# acc2 = Account(200)
# acc2.withdraw(30)
# print(acc2)



class Animal:

    def eats(self):
        print('animal is very hungry')

class Cute():

    def cute(self):
        print('this animal is cute')

class Dog(Animal):

    def barks(self):
        print('dog barks')

class Puppy(Dog, Cute):

    def barks(self):
        print('puppy barks')

    def plays(self):
        print('puppy is a small dog')

dog = Dog()
dog.eats()

p = Puppy()
p.eats()
p.barks()
p.plays()
p.cute()






