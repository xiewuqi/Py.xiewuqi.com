class Parent(object):
    
    def override(self):
        print("PARENT overiide()")
    
    def implicit(self):
        print("PARENT implicit()")
    
    def latered(self):
        print("PARENT altered()")

        
class Child(Parent):
    
    def override(self):
        print("CHILD override()")
    
    def latered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).latered()
        print("CHILD, AFTER PARENT altered()")
   
        
dad = Parent()
son = Child()


dad.implicit()
son.implicit()


dad.override()
son.override()


dad.latered()
son.latered()

