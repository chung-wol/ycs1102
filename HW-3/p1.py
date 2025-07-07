income = int(input("연봉 소득: "))

tax = 0

if income <= 2000:
    tax = (income) * 0.01
elif (income > 2000 and income <= 4000):
    tax = 200 + (income - 200) * 0.03
elif (income > 4000 and income <= 8000):
    tax = 500 + (income - 500) * 0.08
else:
    tax = 800 + (income - 800) * 0.15

aftertax = income - tax

print("세후 소득금액: %.2f" %aftertax)