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

user_n=input("Enter username: ")
passw=int(input("enter password:"))
while user_n!="admin" or passw!=1234:
    print("Invalid username or password. Please try again.")
    user_n=input("Enter username: ")
    passw=int(input("enter password:"))
print("Login successful!")