# num=int(input("enter a number"))
# if num%2==0:
#         print("even")
# else:
#         print("odd")
# n=int(input("enter a number"))
# for i in range(1,11):
#     # if n%2==0:
#         print(n,'x',i,'=',n*i)  
# n=int(input("enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("fact=",fact)
# str=input("enter a character")
# rev=""
# for ch in str:
#     rev=ch+rev
# # print(rev) 
# str=input("enter a character")
# rev=" "
# for ch in str:
#     rev = ch + rev
# if str == rev:
#     print("palindrome")
# else:
#     print("not palindrome")
# str=input("enter a string")
# vowel="aeiou"
# count=0
# for ch in str:
#     if ch in vowel:
#        count=count+1
# print(count)
# n=input("enter anumber")
# lst=[]
# for x in n.split():
#     lst.append(int(x))
# largest=lst[0]
# for n in lst:
#     if n>largest:
#         largest=n
# # print("largest",largest)

# n=input("enter anumber")
# lst=[]
# for x in n.split():
#     lst.append(int(x))
#     largest=lst[0]
# for n in lst:
#     if n<largest:
#         largest=n
# print(largest)
# n=int(input("enter a number"))
# f=0
# for i in range(1,n+1):
#     if n%i==0:
#         f=f+1
# if f==2:
#     print("prime")
# else:
#     print("not prime")
# n=int(input("enter a number"))
# a=0
# b=1
# print("fibonacci")
# for _ in range(n):
#     print(a,end="")
#     a,b=b,a+b
# n=int(input("enter a number"))
# digits=0
# while n>0:
#     digits+=n%10
#     n=n//10
# print(digits)
# n=input("enter a number")
# lst=[]
# for x in n.split():
#     lst.append(int(x))
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]>lst[j]:
#             temp=lst[i]
#             lst[i]=lst[j]
#             lst[j]=temp
# print(lst)
# n=input("enter a number")
# for x in n.split():
#    lst=[]
#    for i in n:
#     if i not in lst:
#       lst.append(i)
# print(lst)
# n1=input("enter n1")
# lst1=[]
# for x in n1.split():
#     lst1.append(int(x))
# n2=input("enter n2 number")
# lst2=[]
# for x in n2.split():
#         lst2.append(int(x))
# common=[]
# for i in lst1:
#   for j in lst2:
#     if i==j and i not in common:
#         common.append(i)
# print(common)
# a=int(input('enter a number'))
# b=int(input('enter a number'))
# a,b=b,a
# print("after swpping:a=",a,",b=",b)

