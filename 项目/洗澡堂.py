import time
print("欢迎来到永康澡堂".center(30,"*"))
ls = []
all_money =0
while True:
	print("1.入店")
	print("2.离店")
	print("3.统计")
	print("4.退出")
	num = int(input("请选择功能:"))
	if num == 1:
		print("入店")
		md = {}
		name = input("请输入用户姓名:")
		sf = input("请输入用户身份证号:")
		md["name"]= name
		md["time"] = int(time.time())
		md["sj"]=True
		md["sf"]= sf
		if len(sf)== 18:
			md["sf"]=sf
		else:
			print("输入格式不对，请重输:")
			continue
		ls.append(md)
		print(md)
	elif num == 2:
		print("离店")
		name = input("请输入你的名字")
		for md in ls:
			if md["name"]== name:
				md["sj"] = False
				endtime =int(time.time())
				df_money = (endtime - md["time"])*10
				print("花了%.02f"%df_money)
				money = float(input("请付钱(注:不找零)"))
				print("离店成功,欢迎下次欢迎:")
			else:
				print("未找到该用户")
				break
	elif num == 3:
		print("统计")
		acount = input("请输入管理员账号:")
		pwd = input("请输入管理员密码:")
		if acount == "123456" and pwd == "123456":
			print("欢迎使用")
			num = input("请选择功能")
			count = 0
			if num =="统计":
				print("今天洗澡%d"%len(ls))
				for md in ls:
					if md["sj"]==False:
						count +=1
						print("今天离店%d"%count)
						print("今天收益%0.2f"%all_money)
	elif num ==4:
		print("退出")
		exit()

