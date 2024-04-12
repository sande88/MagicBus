# print(1+1) #2
# print(1+'a') #error
# print('a'+'a') #aa

# var = "Santhosh"
# up_var =var.upper()
# print(up_var)
# print(up_var.lower())
# print(len(var))

# a=[]
# b=a.append()
# print(a)

# a="welcome to azure family"
# a='new'
# print(a)
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a[1:3])
# print(a[4:9])
# print(a[11:12])
# print(a[:3])
# print(a[4:])
# print(a[1:10:2])
# print(a[:10:3])
# strin=''
# print(strin[::-1])
# def prime(num):

#     flag = False

#     if num == 1:
#         print(num, "is not a prime number")
#     elif num > 1:
#     # check for factors
#         for i in range(2, num):
#             if (num % i) == 0:
#             # if factor is found, set flag to True
#                 flag = True
#             # break out of loop
#                 break

#         if flag:
#             print(num, "is not a prime number")
#         else:
#             print(num, "is a prime number")



# prime(5)

a=[]
n=int(input("enter a number"))
for i in range(n):
    username=input(f"username {i}")
    a.append(username)

print(a)




