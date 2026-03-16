# #function
# def msg():

#     n1=int(input("Enter the first number: "))
#     n2=int(input("enter second number:"))
#     print("Add:",n1+n2)
# msg()

# def add():
#     n1=int(input("Enter the first number: "))
#     n2=int(input("enter second number:"))
#     s=n1+n2
#     m=n1*n2
#     sub=n1-n2
#     div=n1/n2
#     return s,m,sub,div
# result=add()
# print(result)

# positional argument
# keyword argument
# default argument
# variable length argument/ variable number of argument

# def personalInfo(fname,lname):
#     print("First name:",fname)
#     print("Last name:",lname)
# personalInfo("Shantanu","Bhaduri") #positional argument

# def cityName(city="Nagpur"):
#     print(city)
# cityName("Mumbai")
# cityName("Delhi")
# cityName() 

# variable length
def studentNames(*name):
    print(name)
studentNames("Shantanu","Satyarth","Satyam","Satyarth","Satyarth")