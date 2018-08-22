lise = []
for i in range(2):
	d = {}
	name = input("请输入你的名字:")
	year = int(input("请输入你的年龄:"))
	sex = input("请输入你的性别:")
	d["name"] = name
	d["year"] = year
	d["sex"]= sex
   	print(d)
	lise.append(d)
print(lise)
for i in lise:
	for j in i.valuse():
		print(j)
