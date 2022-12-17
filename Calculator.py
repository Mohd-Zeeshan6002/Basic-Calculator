num1=int(input("Enter 1st number= "))
num2=int(input("Enter 2nd number= "))
operator=input("Enter any operator (+,-,*,/)= ")
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/": 
    result=num1/num2
else:
    print(" Invalid operator, error!")
print("Result=", result)
