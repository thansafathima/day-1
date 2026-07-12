#exceptions
# events that affect the exexution of our program

# errors
# syntax errors
# type error
# Indentation error

# try:
#     a = 5
#     b = 0
    # print(a/b)
# except:
#     print("you have an error")
# print("mohan")


# try:
#     a = 5
#     b = 0
#     print(a/b)
# except Exception as e:
#     print("you have an error ",e)


# print("mohan")


# try:

#     a = 5
#     b = 0
#     print (a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero") 
# except ValueError:
#     print("Check values")
# except  TypeError:
#     print("check types")   



# try:

#     a = int(input("enter a number"))
#     b = 10
#     print (a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero") 
# except ValueError:
#     print("Check values")
# except  TypeError:
#     print("check types")  
# print("mohan")

# # try block should have atleast one except or finally




# try:

#     a = int(input("enter a number"))
#     b = 10
#     print (a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero") 
# except ValueError:
#     print("Check values")
# except  TypeError:
#     print("check types")  
# finally:
#     print("this will always execute")
# print("mohan")


# if there is even any exception or any error or not,if there is finally it will always execute the finally


# raise.  it is used to call the exception directly
# to  create custom error class

# class Myerror(Exception):
#     pass


# name = "das"
# if name == "das":
#     raise Myerror("name should not be das")


# a = 5
# del(a)
# print(a)

# a will remove from the memory


# FILE HANDLING

# READ?
# WRITE?

# Text based

# file1 = open("data.txt","r")
# print(file1.read())
# file1.close()


# file2 = open("myfile.txt","w")
# file2.write("today is wednesday")
# file2.close()

file3 = open("myfile.txt","a")
file3.write("\nHello1")
file3.close()


# file3 = open("myfile.txt","a")
# for i in range(1,101):
#     file3.write(f"\nThansa {i}")
# file3.close()



# without using close

# with open("myfile.txt") as file1:
#     print(file1.read())


# OS

# import os
# os.mkdir("images")


# os.remove(#"name of the file")
# os.rename("current name","new name")


# to check if there is a path,take it in desktop and click copy as path amd create a variable and copy it
# make the slashes as double

pat = 
if os.path exists(pat):
    if os.path.isfile(pat)
        print(path exists)
    elif os.path.isdir(pat):
        print("folder exists")
