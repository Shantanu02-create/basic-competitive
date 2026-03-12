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
# per>80 and per<=90==>grade B
# per>70 and per<=80==>grade C
# per>60 and per<=70==>grade D  
# per<=60==>FAIL
per=float(input("Enter percentage: "))
if per>90:
    print("Grade A")
elif per>80 and per<=90:
    print("Grade B")
elif per>70 and per<=80:
    print("Grade C")
elif per>60 and per<=70:
    print("Grade D")
else:
    print("FAIL")