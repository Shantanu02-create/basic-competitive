#NESTED IF ELSE:

# if condition-1:
#     if condition-2:
#         #code
#     else:
#         #code
# else:
#     if condition-2:
#         #code
#     else:
#         #code
# WAP to accept three paper marks and check maximum marks using nested if else:

# m1=float(input("Enter marks for paper 1: "))
# m2=float(input("Enter marks for paper 2: "))
# m3=float(input("Enter marks for paper 3: "))
# if m1>m2:
#     if m1>m3:
#         print("Maximum marks is m1: ",m1)
#     else:
#         print("Maximum marks is m3: ",m3)
# else:    
#     if m2>m3:
#         print("Maximum marks is m2: ",m2)
#     else:
#         print("Maximum marks is m3: ",m3)

# WAP to accept three paper marks and check minimum marks using nested if else:
# m1=int(input("Enter marks for paper 1: "))
# m2=int(input("Enter marks for paper 2: "))
# m3=int(input("Enter marks for paper 3: "))
# if m1<m2:
#     if m1<m3:
#         print("Minimum marks is m1: ",m1)
#     else:
#         print("Minimum marks is m3: ",m3)
# else:    
#     if m2<m3:
#         print("Minimum marks is m2: ",m2)
#     else:
#         print("Minimum marks is m3: ",m3)
# else if ladder:
# if condition-1:
#     #code 
# elif condition-2:
#     #code 
# elif condition-3:
#     #code
# else:
#     #code

# WAP to accept percentage and if per 
# per>90==>grade A
# per>80 and per<=90 ==>grade B
# per>70 and per<=80 ==>grade C
# per>60 and per<=70 ==>grade D  
# per<=60==>FAIL
# per=float(input("Enter percentage: "))
# if per>90:
#     print("Grade A")
# elif per>80 and per<=90:
#     print("Grade B")
# elif per>70 and per<=80:
#     print("Grade C")
# elif per>60 and per<=70:
#     print("Grade D")
# else:
#     print("FAIL")

# mydict={"Name":"Shantanu","Age":20,"Sid":4849}
# print(mydict)
# print(type(mydict))
# print(id(mydict))

# myd={101:"Shantanu",102:"Satyarth",'102':"Satyam",104:"Shivam",104:"Shivaji",106:"Adam"}
# # print(myd)
# # # a=myd[102]
# # # print(a)
# myd[104]="Prem"
# # print(myd)
# # for x in myd:
# #     print(x)
# # for y in myd.values():
# #     print(y)
# # items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
# # for x,y in myd.items():  
# #     print(x," ",y)

# myd["Mobile"]=1234567890
# # print(myd)

# name="Shantanu_B"
# #Inndexing and slicing in string:
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])#slicing
# print(name[0:])#slicing
# print(name[:5])#slicing
# print(name[:])#slicing
# print(name[0:10:2])#slicing with step
# print(name[::2])#slicing with step
# print(name[::-1])

# st="help4code is a best platform for practicing programming"
# print(st.find("help4code"))
# print(st.find("best"))
# print(st.find("platform"))
# print(st.find("Python"))#find() method returns the lowest index of the substring if it is found in the given string. If it is not found then it returns -1.

# sa="Shantanu","Ashish","prem"
# m='+'.join(sa)
# print(m)

# print(st.lower())#lower() method returns a copy of the string in which all the case-based characters have been converted to lowercase.
# print(st.upper())#upper() method returns a copy of the string in which all the case-based characters have been converted to uppercase.
# print(st.title())#title() method returns a copy of the string in which the first character of each word is converted to uppercase and the rest are lowercase.
# print(st.capitalize())#capitalize() method returns a copy of the string with its first character capital
# print(st.swapcase())#swapcase() method returns a copy of the string in which the case of each character is swapped. Uppercase characters are converted to lowercase and vice versa.

# print("Subject marks:")
# phy=50
# chem=60
# math=70
# print("Physics={} chemistry={} math={}".format(phy,chem,math))
# print("Physics={0} chemistry={1} math={2}".format(phy,chem,math))
# # print("Physics={x} chemistry={y} math={z}".format(phy,chem,math))
# total=phy+chem+math
# print("Total marks: ",f"{total}")
# print("roll No=","7".zfill(4))

# print('Shantanu_B'.isalpha())#isalpha() method returns True if all the characters in the string are alphabets. If not, it returns False.
# print('Shantanu888'.isalnum())
# print('12345'.isdigit())#isdigit() method returns True if all the characters in the string are digits. If not, it returns False.
# print(' '.islower())#islower() method returns True if all the characters in the string are lowercase. If not, it returns False.
# print('SHANTANU'.isupper())#isupper() method returns True if all the characters in the string are uppercase. If not, it returns False.
# print("Hello".startswith("H"))#startswith() method returns True if the string starts with the specified prefix. If not, it returns False.
# print("Hello".endswith("o"))#endswith() method returns True if the string ends with the specified suffix. If not, it returns False.
# print(''.istitle())#istitle() method returns True if the string is a titlecased string. If not, it returns False. A titlecased string is a string in which the first character of each word is uppercase and the rest are lowercase.
# print(' '.isspace())#isspace() method returns True if all the characters in the string are whitespace. If not, it returns False.

# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x=['a','b','c','d','e']
# y=['a','b','c','d','e']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

# name="Shantanu"
# for i in name:
#     print(i)

# name="shantanu" 
# set=["A","E",'I','O','U','a','e','i','o','u']
# vowels=0
# cons=0
# for i in name:
#     if i in set:
#         vowels+=1
#     else:
#         cons+=1
# print("VOWELS=",vowels)
# print("CONSONANTS=",cons)
# name="shantanu" 
# set=["A","E",'I','O','U','a','e','i','o','u']
# vowels=0
# cons=0
# for i in name:
#     if i in set:
#         vowels+=1
#     else:
#         cons+=1
# print("VOWELS=",vowels)
# print("CONSONANTS=",cons)


# def demo_dictionary():
#     myd = {
#         101: "Shantanu",
#         102: "Satyarth",
#         "102": "Satyam",
#         104: "Shivam",
#         104: "Shivaji",  # duplicate key: last assignment wins
#         106: "Adam",
#     }

#     print("Initial dict:", myd)
#     print("myd[102] (int key):", myd[102])
#     print("myd['102'] (str key):", myd["102"])
#     print("myd[104] (last value assigned):", myd[104])

#     # Update an existing key and add a new key
#     myd[104] = "Prem"
#     myd["Mobile"] = 1234567890

#     print("Updated dict:", myd)

#     # Iterate through the dict items
#     for k, v in myd.items():
#         print(f"{k!r} -> {v!r}")


# if __name__ == "__main__":
#     demo_dictionary()