print("_" * 50)
print("   yinNEN python program BMI计算器   ")
print("     program version 1.00    ")
print("_" * 50)

a = input("键入体重(kg):")
b = float(a)
c = input("键入身高(m):")
d = float(c)
e = d * d
bmi = b / e
print("你的BMI是", b / e)
if bmi < 0:
    print("您的数据有问题.")
    input("按任意键退出...")
    exit()
elif bmi < 18.5:
    print("您的体重太低了")
    input("按任意键退出...")
    exit()
elif bmi < 24.0:
    print("您的体重适中")
    input("按任意键退出...")
    exit()
elif bmi < 30.0:
    print("您的体重偏高")
    input("按任意键退出...")
    exit()
elif bmi >=30.0:
    print("您的数据可能有问题，或者你真的太重了。")
    input("按任意键退出...")
    exit()
