count = int(input("请输入一个数字"))
evenNumberSum = 0
oddNumberSum = 0
allSum = 0
x = 0
while x < count:
	print("当前数字:%d"%x)
	x+=1
	if x%2 ==0:
		evenNumberSum = evenNumberSum + x
	elif x %2 !=0:
		oddNumberSum = oddNumberSum +x
print("偶数和为:%d"%evenNumberSum)
print("奇数和为:%d"%oddNumberSum)
print("总和为:%d"%(evenNumberSum+oddNumberSum))
