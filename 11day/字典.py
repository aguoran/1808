c = {"name":"郭冉","sex":"男","mz":"汉","age":"17"}
#c["adderss"] = "邯郸"#添加
#print(c)
#c["sex"]= "女"#则上边有就不是添加，而是改
#print(c)
#c.pop("age")#删除
#print(c)
#print(c["age"])#查找，上边没有会报错
#print(c.get("age"))#查找，上边没有键会返回None
for i in c:
	print(c[i])
