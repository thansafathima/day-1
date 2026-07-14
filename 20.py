# # 14-07-2026

# # inheritance

# # parent
# # child

# class Person1:

#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def smile(self):
#         print("person can smile hahaha")
#     def speak(self):
#         print("person1 can speak")

# class Person2(Person1):

#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")
#     def write(self):
#         print("person can write")
#     def speak(self):
#         print("person2 can speak")


# class Person3(Person2):

#     def __init__(self):
#         pass
#     def read(fly):
#         print("Person can fly")
#     def swim(self):
#         print("Person can swim")
#     def speak(self):
# #         print("Person3 can speak")


# class Person4(Person3):

#     def __init__(self):
#         pass
#     def sleep(self):
#         print("Person can sleep")
#     def eat(self):
#         print("Person can eat")
#     def speak(self):
#         print("Person4 can speak")
#         super().speak()

# p4 = Person4()
# p4.speak()


# MULTILEVEL inheritance


# class Person1:

#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def smile(self):
#         print("person can smile hahaha")
#     def speak(self):
#         print("person1 can speak")

# class Person2(Person1):

#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")
#     def write(self):
#         print("person can write")
#     def speak(self):
#         print("person2 can speak")


# class Person3(Person2):

#     def __init__(self):
#         pass
#     def read(fly):
#         print("Person can fly")
#     def swim(self):
#         print("Person can swim")
#     def speak(self):
#         print("Person3 can speak")


# class Person4(Person3,Person2,Person1):

#     def __init__(self):
#         pass
#     def sleep(self):
#         print("Person can sleep")
#     def eat(self):
#         print("Person can eat")
#     def speak(self):
#         print("Person4 can speak")
#         super().speak()
# p4 = Person4()
# p4.speak()

# mro=method resolution order

# Polymorphism

# poly-many
# morph - forms


# operator overloading
# method overloading
# method overriding

# operator overloading
# add
# ======
# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self,otr):
#         return self.m1+self.m2,otr.m1+otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1+s2)


# sub
# ====

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __sub__(self,otr):
#         return self.m1-self.m2,otr.m1-otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1-s2)

# MULT
# ====

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __mul__(self,otr):
#         return self.m1*self.m2,otr.m1*otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1*s2)

# div
# ====


# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __truediv__(self,otr):
#         return self.m1/self.m2,otr.m1/otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1/s2)


# gt= greater than


# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __gt__(self,otr):
#         return self.m1>self.m2,otr.m1>otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1>s2)


# Method overloading


# method overriding

# class A:
#     def __init__(self):
#         pass
#     def hello(self):
#         print("hello")
# class B(A):
#     def __init__(self):
#         pass
#     def hello(self):
#         print("B hello")

# b=B()
# b.hello()



# method overloading

class A:
    def __init__(self):
        pass
    def hello(self):
        print("A hellooo")

class B:
    def __init__(self):
        pass
    def hello(self):
        print("B hello")

b = B()
b.hello()

# b = b.hello()
# b.hello()