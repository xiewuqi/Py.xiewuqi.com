# -*- coding: utf-8 -*-
## Animal（家畜） is-a object (yes, sort of confusing) lock at the extra cerdit
class Animal(object):
    pass
    
## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
    ## ??
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## ??
        self.name = name
        
## person is-a object?
class Person (object):
    
    def __init__(self, name):
        ## Person has-a name ??
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## Employee（雇员）is-a person??
class Employee(Person):
    
    def __init__(self, name, salary):
        ## ?? ham what is this starnge magic?
        super(Employee, self).__init__(name)
        ## ？？
        self.salary = salary
        
## fish is-a object??
class Fish(object):
    pass

## 三文鱼 is-a fish??
class Salmon(Fish):
    pass
    
## 大比目鱼 is-a fish??
class Halibut(Fish):
    pass
    
    
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat??
satan = Cat("Satan")

## maer is-a person??
mary = Person("Mary")

## marry.pet is-a satan ??
mary.pet = satan

## frank is-a Emoloyee has-a Frank, 120000??
frank = Employee("Frank", 120000)

## frnk.pet is-a rover
frank.pet = rover

# 有鱼鳍的是雨 ?
flipper = Fish()

## crouse is-a 三文鱼 ?
crouse = Salmon()

## harry is-a 大比目鱼 ??    
harry = Halibut()




