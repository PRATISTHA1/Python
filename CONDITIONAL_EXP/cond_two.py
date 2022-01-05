num1 = int(input("enter number1"))
num2 = int(input("enter number2"))
num3 = int(input("enter number3"))
if num1 < 33 or num2 < 33 or num3 < 33:
    print("fail")
elif (num1 + num2 + num3) / 3 < 40:
    print("fail")
else:
    print("pass")
