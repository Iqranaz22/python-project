print("mini calculator")
num1=float(input("enter first number"))
num2=float(input("enter second number"))
print("press 1 for add /n, press 2 for difference n/, press 3 for product n/,press 4 for divisionn/")

choice =int(input("enter your choice  from 1 - 4:"))
if choice ==1:
    print("the addition of given two number",num1+ num2)
elif choice ==2:
    print("the subtraction of given two number",num1-num2)
elif choice ==3:
    print("the product of given two number",num1*num2)
elif choice ==4:
    print("the division of given two number",num1/num2)
else:
    print("invalid input")
 