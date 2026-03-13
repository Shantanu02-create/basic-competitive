# for i in range(1,5):
#     if i==3:
#         break
#     print(i)

# for i in range(1,5):
#     if i==3:
#         continue
#     print(i)

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i,j)

#Syntax of while loop:
# while condition:
#     #code
# i=1
# while i<=5:
#     print(i)
#     i+=1

# user_n=input("Enter username: ")
# passw=int(input("enter password:"))
# while user_n!="admin" or passw!=1234:
#     print("Invalid username or password. Please try again.")
#     user_n=input("Enter username: ")
#     passw=int(input("enter password:"))
# print("Login successfull!")

# n=int(input("Enter a number: "))
# s=0
# i=1
# while i<=n:
#     s+=i
#     i+=1
# print("Sum of first ",n," numbers is: ",s)

#Duplicate character removal
# name='Shantanu'
# new_name=""
# for i in name:
#     if i not in new_name:
#         new_name+=i
# print(name)
# print(new_name)

# reverse a string using loop
# name='Shantanu'
# reversed_name = ""
# for i in range(len(name)-1, -1, -1):
#     reversed_name += name[i]
# print(reversed_name)

mycart=[100,200,300,400,500,800,900,1000]
print("Items in cart: ")
for i in mycart:
    if i>400:
        continue
    
    print(i)


