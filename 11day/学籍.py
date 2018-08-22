print("欢迎来到学籍管理系统".center(30,"*"))
box = []
while True:
	print("1,录入")
	print("2,修改")
	print("3,查找")
	print("4,删除")
	print("5,退出")
	num = int(input("请选择功能"))
	if num == 1:
		xjb = {}
		name = input("请输入名字")
		age = int(input("请输入年龄"))
		sex = input("请输入性别")
		phone = input("请输入手机号")
		xjb["name"]= name
		xjb["age"]= age
		xjb["sex"]= sex
		if phone.startswith("1")and len(phone)==11:
			xjb["phone"]= phone
		else:
			print("输入不合法,从新输入")
			continue
		box.append(xjb)
		print("录入")
		print(box)
	elif num == 2:
		print("修改")
		name = input("请输入要修改的名字")
		for xjb in box:
			if  xjb["name"] == name:
				print(xjb)
				print("1. 修改名字")
				print("2. 修改年龄")
				print("3. 修改性别")
				print("4. 修改手机号")
				num = int(input("请选择新的功能"))
				if num == 1:
					name = input("请输入新名字")
					xjb["name"] = name
				elif num == 2:
					age = int(input("请输入新年龄"))
					xjb["age"] = age
				elif num == 3:
					sex = input("请输入新性别")
					xjb["sex"] = sex
				elif num == 4:
					phone = input("请输入新手机号")
					if phone.startswith("1")and len(phone)==11:
						xjb["phone"] = phone
					else:
						print("修改失败")
				
	
				break
	
	elif num == 3:
		print("查找")
		for xjb in box:
			name = input("请输入要查找的名字")
			flag = Flase
			for xjb in box:
				if xjb["name"] == name:
					print("姓名\t年龄\t性别\t手机号")
					print("%s\t%s\t%s\t%s"%(xjb["name"],xjb["age"],xjb["sex"],xjb["phone"]))
					flag = True
					break
				if flag == False:
					print("查无此人")
				
		
		
	elif num == 4:
		name = input("请输入删除的名字")
		for xjb in box:
			if xjb ["name"]==name:
				num = int(input("是否要删除 1.Yes 2.No"))
				if num == 1:
					box.remove(xjb)
				break

		print("删除")
	elif num == 5:
		print("退出")
		exit()
