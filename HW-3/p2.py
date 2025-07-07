print("This program is a calculator")
print("Enter (1) to add two values")
print("Enter (2) to subtract two values")
print("Enter (3) to multiply two values")
print("Enter (4) to divide two values")

types = int(input("Enter a number: "))

if types == 1:
    print("덧셈이 선택되었습니다")
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print(num1+num2)    
elif types == 2:
    print("뺄셈이 선택되었습니다")
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print(num1-num2)
elif types == 3:
    print("곱셈이 선택되었습니다")
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print(num1*num2)
elif types == 4:
    print("나눗셈이 선택되었습니다")
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print("%.2f" %(num1/num2))
else:
    print("잘못된 입력입니다")