# GIL
# GLOBAL INTERPRETER LOG
# It is a mutex(lock) used by the c python interpreter that allows only one thread at a time to execute python bytecode,even if multiple threads exist


# multiprocessing

# from multiprocessing import Process
# import os
# def work():
#     print("am working")
#     print(os.getpid())

# p1 = Process(target=work)
# p2 = Process(target=work)

# if __name__ == "__main__":       # nammde file ann katan vndit
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()


# process doesnot share memory,it is independant
# threads share memory



# from multiprocessing import Process
# import os
# x = 5
# def work():
#     global x
#     x = x * 10
#     print("am working",x)
#     print(os.getpid())

# p1 = Process(target=work)
# p2 = Process(target=work)

# if __name__ == "__main__":       # nammde file ann katan vndit
#     print(x,"main Process")
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()



# list,dictionary,set. mutable


# list comprehension
# create a list with logic directly

# print numbers from 1 to 100
# a = [i for i in range(1,101)]
# print(a)

# print even numbers
# a = [i for i in range(1,101)if i%2 == 0]
# print(a)

# create a list with numbers that are multiple of 3 and 5

# num = [i for i in range(1,101)if i%5==0 and i%3 ==0]
# print(num)
 
# create a list of first 1000 numbers that has digit 6 in them
# eg:(6,16,26,36,46.......)

# n6 = [i for i in range(1,1001) if "6" in str(i)]
# print(n6)

#regular expression

# import re
# # pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
# pattern = r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}"
# data = "my adar number is 5378-8744-8584-7531"
# # \d = one decimal digit
# # \w = alpha numeric
# # \D =

# print(re.search(pattern,data))


# import re
# pattern = r"[a-z][a-zA-Z0-9!@#$%^&*()+_]+@[a-z]+.[a-z]+"
# data = "my email is t234566##$5HAFSUSBS@gmail.com"
# print(re.search(pattern,data))



# collection of email
# findall

# import re
# pattern = r"([a-z][a-zA-Z0-9!@#$%^&*()_]+)@([a-z]+).([a-z]+)"
# data = "my email is t23345##$%#HAFSUSBS@gmail.com,t233445##$%HAFSU@gmail.com"
# # z = re.findall(pattern,data)
# z= re.search(pattern,data)
# print(z.group(4))
# # for i in z:
#     # print(i)


# find website pattern
# https://www.google.com/