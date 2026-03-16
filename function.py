# #function
# def msg():

#     n1=int(input("Enter the first number: "))
#     n2=int(input("enter second number:"))
#     print("Add:",n1+n2)
# msg()

def add():
    n1=int(input("Enter the first number: "))
    n2=int(input("enter second number:"))
    s=n1+n2
    m=n1*n2
    sub=n1-n2
    div=n1/n2
    return s,m,sub,div
result=add()
print(result)