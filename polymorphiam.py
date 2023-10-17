##polymorphism
class Pencil:
    def write(self):
        print("It is used to writing in grey colour")
class Pen:
    def write(self):
        print("It is used to wiriting in ink colour")
a=Pencil()
b=Pen()
for i in (a,b):
    i.write()

class Birds:
    def fly(self):
        print("Birds or flying are not flying")
class Parrot(Birds):
    def fly(self):
        super().fly()
        print("parrot is flying")
class Kiwi(Birds):
    def fly(self):
        super().fly()
        print("kiwi is not flying")
a=Parrot()
b=Kiwi()
obj=[Parrot(),Kiwi()]
for i in obj:
    i.fly()

##Task
def func():
    return "welcome to the ocean acadamey"
result=(func().upper())
print(result)

##Task1
class Animals:
    def make_sound(self):
        print("Animals make a different sounds")
class Dog(Animals):
    def make_sound(self):
        super().make_sound()
        print("Dog make a sound is loool loool")
class Cat(Animals):
    def make_sound(self):
        super().make_sound()
        print("Cat make a sound is meow meow")
class Cow(Animals):
    def make_sound(self):
        super().make_sound()
        print("Cow make a sound is maaaaaaa")
obj=[Dog(),Cat(),Cow()]
for i in obj:
    i.make_sound()
##Task 2
class Shape:
    def calculate_area(self):
        print("calculate the different shapes")
class Circle(Shape):
    def __init__(self,r):
        self.r=r
        print(f"value of r is {self.r}")
    def calculate_area(self):
        super().calculate_area()
        a=3.14*self.r**2
        print(f"Area of the circle is {a}")
class Rectangle(Shape):
    def __init__(self,w,l):
        self.w=w
        self.l=l
        print(f"vlaue of w is {self.w}")
        print(f"value of l is {self.l}")
    def calculate_area(self):
        super().calculate_area()
        a=self.w*self.l
        print(f"Area of rectangle is {a}")
class Traingle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
        print(f"value of b is {self.b}")
        print(f"value of h is {self.h}")
    def calculate_area(self):
        super().calculate_area()
        a=self.b*self.h/2
        print(f"Area of the Traingle is {a}")
r=int(input("enter the value of r"))
obj=Circle(r)
obj.calculate_area()
w=int(input("enter the value of w"))
l=int(input("enter the value of l"))
obj=Rectangle(w,l)
obj.calculate_area()
b=int(input("enter the value of b"))
h=int(input("enter the value of h"))
obj=Traingle(b,h)
obj.calculate_area()
      
##Dector function
def outer(f):
    def inner():
        f()
        return "Hello World"
    return inner()
print(outer())
def func():
    print("welcome")
result=outer(func)
print(result)




        
        
        


















































