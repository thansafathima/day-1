#list
# collection of data
# properties

# 1.list can have any element of any size
# data =[1,2,3.4,"name",True,[1,2,3],90]

# 2.list are ordered

# a = [1,2,3,4]
# b = [2,3,1,4]
# print(a == b)    it will be false

# 3.list are indexed

# a = [3,5,2,1,6]
# print(a[0])                     the answer would be 3

# [start:stop:step]

# a = [1,9,6,7,3,6,4,99,33,22]
# print(a[3:8])           the answer would be[7, 3, 6, 4, 99]

# a = [1,9,6,7,3,6,4,99,33,22]
# print(a[::-1]).           the answer would be [22, 33, 99, 4, 6, 3, 7, 6, 9, 1]


# a = "mohan"
# print(a[-2])         the answer would be 'a'

# # 4.list are mutable
# a = [12,4,6,8,9]
# a[0] = "mohan"
# print(a).             ans:['mohan', 4, 6, 8, 9]

# string are immutable

# b = "mohan"
# b[0] = h
# print (b)        
# answer:      
# NameError: name 'h' is not defined,because string is immutable


# 5.dynamic
# 6.list are nested

# a = [12,33,44,[100,399],44]
# print(a[3][0]).       the ans would be 100

# inbuilt methods in a list

# to add elements
# ------------------
# append()
# ==========
# add elements to the end of the list

# a = [11,44,77,56,89,99]
# a.append(100)
# print(a)

# answer.....[11, 44, 77, 56, 89, 99, 100]

# extend()
# ===========
# adds an iterable to the list

# a = [11,12,14,13,17]
# a.extend(["mohan"])
# print(a)

# ans:     [11, 12, 14, 13, 17, 'mohan']

# insert()
# ===========
# insert(index,value)

# a = [11,12,14,13,17]
# a.insert(1,"mohan")
# print(a)

# [11, 'mohan', 12, 14, 13, 17]

# to remove elements
# --------------------
# remove()
# =======

# a = [11,12,14,13,17,11,11,23]
# a.remove(11)
# print(a)
# ans:
# [12, 14, 13, 17, 11, 11, 23] it did not remove the every 11.it only remove the first 11

# pop() / pop(index) it will remove the last element
# ======

# a = [11,12,14,13,17,11,11,23]
# a.pop()
# print(a)
# ans:
# [11, 12, 14, 13, 17, 11, 11] it removed the last element

# if we use 2 pop it will remove 2 elements from the last

# a = [11,12,14,13,17,11,11,23]
# a.pop()
# a.pop()
# print(a)
# ans:
# [11, 12, 14, 13, 17, 11]

# with suitable index

# a = [11,12,14,13,17,11,11,23]
# a.pop(0)
# print(a)
# ans:
# [12, 14, 13, 17, 11, 11, 23]
# the zeroth index will be removed



# tuple
# ------
# collection of data 
# data = (1,2,4,6,"mohan")
# ordered
# indexed
# tuple is immutable

# a = (1,2,3,4)
# a[0] = 10
# print (a).     it would be error because tuple is immutable


# list mutable 
# tuple immutable

#iteration
# a = 4564
# count = 0
# while a > 0:
#     count = count + 1
#     a = a//10
# print(count)

# str
# list
# tuple
# set
# dict

# iterables

# a = [11,12,14,13,17,11,11,23]
# b = "mohan das"
# c = (100,200,300,400)

# for i in a:          direct iterable
#     print (i)


# a = "mohan"
# # print(len(a))

# for i in range(0,len(a)):
#     print(i,a[i]).                  index and name



# fruits = ["apple","orange","pineapple","watermelon","grapes"]
# for i in range(0,len(fruits)):
#     print(i,fruits[i])