# -*- coding: utf-8 -*-
## Animal（家畜） is-a object (yes, sort of confusing) lock at the extra cerdit
class Animal(object):
    pass
    
## Dog is-a Animal??
class Dog(Animal):

    def __init__(self, name):
    ## ??
    self.name = name

## Cat is-a Animal??
class Cat(Animal):
    
    def __init__(self, name):
        ## ??
        self.name = name
        
## ?
class Person (object):
    
    def __init__(self, name):
        ## ??
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## Employee（雇员）??
class Employee(Person):
    
    def __init__(self, name, salary):
        ## ?? ham what is this starnge magic?
        super(Employee, self).__init__(name)
        ## ？？
        self.salary = salary
        
## ??
class Fish(object):
    pass

##  三文鱼??
class Salmon(Fish):
    pass
    
## 大比目鱼??
class Hilibut(Fish):
    pass
    
    
## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## def ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ？
frank.pet = rover

## ?
flipper = Fish()

## ?
crous = Salmon()

## ??    
harry = Halibut()

print "怎样确定脚本运行成功呢？"


