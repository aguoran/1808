import time
print("欢迎来到徐永康酒店".center(30,"*"))
ls = []
all_money = 0
while True:
	print("1. 入住")
	print("2. 离店")
	print("3. 统计")
	print("4. 退出")
	num = int(input("请选择功能"))
	if num == 1:
		print("入住")
		md = {}
		name = input("请输入入住姓名:")
		sf = input("请输入身份证号:")
		md["name"] = name
		md["time"] = int(time.time())#
		md["sj"] = True#
		md["sf"] = sf
		if len(sf) == 18:
			md["sf"]= sf
		else:
			print("输入不合法,全重输")
			continue
		ls.append(md)
		print(md)
		
	elif num == 2:
		print("离店")
		sf = input("请输入你的名字:")
		for md in ls:
			if md["name"] == name:
				md["sj"]= False#
				endtime = int(time.time())
				df_money = (endtime - md["time"])*10
				print("花了%.02f"%df_money)
				money = float(input("请付钱(注:不找零)"))
				all_money += df_money
				print("退店成功,欢迎下次光临")
			else:
				print("未找到名字")
				break
	elif num == 3:
		print("统计")
		account = input("请输入管理员账号:")
		pwd = input("请输入管理员密码:")
		if account =="123456"and pwd == "123456":
			print("欢迎老板使用")#
			num = input("请选择功能:")
			count = 0
			if num == "统计":
				print("今天住房%d"%len(ls))
				for md in ls:
					if md["sj"]==False:
						count +=1
				print("今天退房%d"%count)
				print("今天收益%0.2f"%all_money)			
	elif num == 4:
		print("退出")
		exit()
