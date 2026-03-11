mylist=["apple","banana","cherry","orange","kiwi","melon","mango",54,60.52]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])
# print(mylist[2:5])
# print(mylist[:4])
# print(mylist[2:])
# print(mylist[-4:-1])
# print(mylist[::2])  
# print(mylist[1:8:2])
# print(mylist[::-1])
# print(mylist[::])

# mylist.append("grapes")
# mylist.append(100)
# print(mylist)

# mylist.insert(2,"watermelon")
# print(mylist)

# mylist.remove("banana")
# print(mylist)

# newlist=mylist.copy()
# print(newlist)
# print(mylist)

# mylist1=[["apple","banana"],[54,60.52],["orange","kiwi"]]

# print(mylist1)
# print(mylist1[0][0])
# print(mylist1[0][1])
# print(mylist1[1][0])
# print(mylist1[1][1])
# print(mylist1[2][0])
# print(mylist1[2][1])

# list1=["Shantanu",'b']
# print(list1*2)
# list2=[50.62,25]
# print(list1+list2)

# del mylist[1]
# print(mylist)

# list2=["car","bike","bus",55]
# list.clear()
# print(list2)

# name="shantanu"
# print(name)
# myname=list(name)
# print(myname)

# mynum=[33,90,45,67,12]
# mynum.sort() #default sorting order for numbers is ascending. deefault sorting order for strings is alphabetical.
# print(mynum)

# math=10
# print(id(math))#id function is used to get the memory address of the variable. it returns a unique identifier for the object. it is used to check if two variables are pointing to the same object in memory.
# math=50
# print(id(math))
# phy=50
# print(id(phy))
# eng=40
# print(id(eng))
#In Python, small integers (from -5 to 256) are cached by the interpreter, which means that they point to the same memory location. Therefore, when we assign the value 50 to both `math` and `phy`, they point to the same memory address, resulting in the same id. However, when we assign a different value (like 40) to `eng`, it points to a different memory address, resulting in a different id.

# mylist3=[1,2,3,4,5]
# newlist=mylist3
# print(id(mylist3))
# print(id(newlist))

# membership operator= 1.in 2. not in
# name1='Shantanu'
# # print('z' in name1)
# for i in range(5,0,-1):
#     print(i)

# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
# print("---------------------------------")
# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)

# no=int(input("Enter a number: "))
# if no>0:
#     print("The number is positive.")
# if no<0:
#     print("The number is negative.")

# day=input("Enter a day: ")
# if day=="Saturday" or"Sunday" or "SATURDAY" or "SUNDAY":
#     print("The day is a weekend.")
# else:
#     print("The day is a weekday.")

#Accept three  paper marks from user and calculate percentage and if percentage is greater than equal to 60 then he/she is eligible for placement
# marks1=float(input("Enter marks for paper 1: "))
# marks2=float(input("Enter marks for paper 2: "))
# marks3=float(input("Enter marks for paper 3: "))
# total_marks=marks1+marks2+marks3
# percentage=(total_marks/300)*100
# if percentage>=60:
#     print("Congratulations! You are eligible for placement.")   

# else:    print("Sorry! You are not eligible for placement.")

#WAP to accept five different value in 5 different variable and check max value and print by using "simple if st"
a=int(input("Enter value for a: "))
b=int(input("Enter value for b: "))
c=int(input("Enter value for c: "))
d=int(input("Enter value for d: "))
e=int(input("Enter value for e: "))
if a>b and a>c and a>d and a>e:
    print("The maximum value is: ",a)
if b>a and b>c and b>d and b>e:
    print("The maximum value is: ",b)
if c>a and c>b and c>d and c>e:
    print("The maximum value is: ",c)
if d>a and d>b and d>c and d>e:
    print("The maximum value is: ",d)
if e>a and e>b and e>c and e>d:
    print("The maximum value is: ",e)
   