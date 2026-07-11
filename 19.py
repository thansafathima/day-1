# object oriented programming
# object ?  object is an instance of a class
# real life entity


# attribute.  defines an object
# behaviours    methods or funtionalities
 
# class is a blueprint
# to create a object

# methods. functions inside a class

# class Car:
#     def start():
#         print("car has started")
#     def stop():
#         print("car stopped")
# c1 = Car

# c1.start()
# c1.stop()

# class Bike:
#     def start():
#         print("bike has started")
#     def stop():
#         print("bike has stopped")
# c1 = Bike
# c1.start()
# c1.stop()
# # constructor
# # used to initialize an object
# # __init__()


# class Car:
#     def __init__(self,n,c):
#        self.name = n
#        self.color = c 
#     #    print (object created)
#     def start(self):
#         print(f"{self.name} has started")
#     def stop(self):
#         print("car stopped")

# c1 = Car("swift","black")
# c2 = Car("swift","red")
# c2.start()

# question
# create a class student
# with 6 attributes name,m1,m2,m3,m4,m5
# 3 methods

# sum of marks()
# average of marks()
# dislay()

# class Student:
#     def __init__(self,n,m1,m2,m3,m4,m5):
#         self.name = n
#         self.mark1 = m1
#         self.mark2 = m2
#         self.mark3 = m3
#         self.mark4 = m4
#         self.mark5 = m5 
#     def start(self):
#         print(self.name)      
#         print(f"sum{self.mark1+self.mark2+self.mark3+self.mark4+self.mark5}")
#     def stop(self):
#         print(f"avg{(self.mark1+self.mark2+self.mark3+self.mark4+self.mark5)/5}")

# s1 = Student("thansa",45,49,45,47,47)

# s1.start()



class Student:
    def __init__(self,n,m1,m2,m3,m4,m5):
        self.name = n
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5 
    def sum_of_marks(self):
        return self.m1+self.m2+self.m3+self.m4+self.m5
    def average_of_marks(self):
        return self.sum_of_marks()/5
    def display(self):
        print(f"student {self.name} has marks of {self.m1} ,{self.m2} ,{self.m3} ,{self.m4} ,{self.m5},the sum of marks is{self.sum_of_marks()}and the average is{self.average_of_marks()}")
s1 = Student("thansa",45,47,49,43,42)
s1.display()



quiz game with a timer