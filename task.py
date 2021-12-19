num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
op =input("Enter any operation +,-: ")

if op=='+':
    result=num1+num2
    print (num1, "+" , num2, "=", result)
else:
    print ("Input character is not recognized!")