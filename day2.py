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

m1=float(input("Enter marks for paper 1: "))
m2=float(input("Enter marks for paper 2: "))
m3=float(input("Enter marks for paper 3: "))
if m1>m2:
    if m1>m3:
        print("Maximum marks is: ",m1)
    else:
        print("Maximum marks is: ",m3)
else:    
    if m2>m3:
        print("Maximum marks is: ",m2)
    else:
        print("Maximum marks is: ",m3)
