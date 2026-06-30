# find vowels and posituons in a string

# name = input("enter your name")
# for i in range(0,len(name)):
#     if name[i] == "a" or name[i] == "e" or name[i] == "i" or name[i] == "o" or name[i] == "u":

#         print(i,name[i])


# in operator.  membership operator

# a = "hari"
# if a in a:
#     print("yes")

# b = [1,2,4,55,"mohan"]
# if "mohan" in b:
#     print("yes")

# name = input("enter a number")
# for i in range(0,len(name)):
#     if name [i] in "aeiou":
#         print(i,name[i])

# list the first 100 numbers into even and odd list
# num = []
# odd = []
# even = []

# for i in range(1,101):
#     num.append(i)
# for i in num:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)
    

# # remove duplicate from the list
# c = [1,2,3,4,1,3,4,2,7,8,9,3,4,5]
# b =[]
# for i in c :
#     if i not in b :
#         b.append(i)
# print(b)

# break continue pass

# break , countinue.  use in loops
# pass
# ====
# age = 19
# if age >= 18:
#     pass
# b = 10
# print(b)
#
# continue
# =========
# for i in range(1,11):
#     if i == 6:
#         continue
#     print(i)

# break
# ======

# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

# prime or not
# 2,3,5,7,11

num = int(input("enter your number"))
prime = True
if num == 1:
    prime = False
else:
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
if prime == True:
    print("prime number")
else:
    print("not a prime" )