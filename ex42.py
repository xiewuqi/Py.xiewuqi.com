# -*- coding: utf-8 -*-
## Animal（家畜） is-a object (yes, sort of confusing) lock at the extra cerdit
class Animal(object):
    pass # 站位，保持程序完整，没有特殊意义。
    
## 创建一个狗的类，它是畜生的一种。 这个dog类接受 self，名字做参数。
class Dog(Animal):

    def __init__(self, name):
    # 从名字中接收变量 ??
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        # ??
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
    
    
## rover 是一个 狗的实例。
rover = Dog("Rover")

## satan is-a Cat??
satan = Cat("Satan")

## maer is-a person??
mary = Person("Mary")

## marry.pet is-a satan ??
mary.pet = satan

## frank is-a Emoloyee has-a Frank, 120000??
frank = Employee("Frank", 120000)

## frnk的宠物 is-a rover（名字）
frank.pet = rover

# filpper的是一种鱼 ?
flipper = Fish()

## crouse is-a 三文鱼 ?
crouse = Salmon()

## harry is-a 大比目鱼的一种 ??    
harry = Halibut()




