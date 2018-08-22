x = float(input("请输入一个值:"))
y = float(input("请输入一个值:"))
fuHao = int(input("请选择运算符 1,加 2,减 3,乘 4,除: "))
if fuHao == 1:
	print(x+y)
elif fuHao == 2:
	print(x-y)
elif fuHao == 3:
	print(x*y)
elif fuHao == 4:
	print(x/y)
else:
	print("您输入的有误")


