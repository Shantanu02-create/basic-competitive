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

# mycart=[100,200,300,400,500,800,900,1000]
# print("Items in cart: ")
# for i in mycart:
#     if i>400:
#         continue
    
#     print(i)

# write a program to chaech if given string is palindrome or not using loop:
# s=input("Enter a string: ")
# reversed_s=""
# for i in range(len(s)-1,-1,-1):
#     reversed_s+=s[i]
# if s==reversed_s:
#     print("The string is a palindrome.")
#     print("Original string: ",s)
#     print("Reversed string: ",reversed_s)
# else:    
#     print("The string is not a palindrome.")  
#     print("Original string: ",s)
#     print("Reversed string: ",reversed_s) 

# # write a program to check two strings are anagrams or not using loop:
# s1=input("Enter first string: ")
# s2=input("Enter second string: ")
# s11=s1.split()
# s22=s2.split()
# if (len(s11)!=len(s22)) or s11.sort()!=s22.sort():
#     print("The strings are not anagrams.")
# else:
#     print("The strings are anagrams.")

# # # Add key value pair in dictionary:
# my_dict = {"Name": "Shantanu", "Age": 20, "Sid": 4849}
# my_dict["Mobile"] = 1234567890
# # print(my_dict)

# # remove key value pair from dictionary:
# del my_dict["Mobile"]
# print(my_dict)

# # Check if key is present in dictionary:
# if "Name" in my_dict:
#     print("Key is present in dictionary.") 

# # remove key value pairs from dictionary:
# # my_dict.clear("Name") 
# print(my_dict)

# # iterate over dictionary key value pairs:
# for key, value in my_dict.items():
#     print(key, ":", value)

# # nested for loop:
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i,end=" ")
#     print()
        
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()

n=int(input("Enter number:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print('@',end=" ")
    print()