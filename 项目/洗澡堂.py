import time
print("欢迎来到永康澡堂".center(30,"*"))
ls = []
all_money =0
while True:
	print("1.入店")
	print("2.离店")
	print("3.统计")
	print("4.退出")
	num = int(input"请选择功能:")
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
				all_time = endtime

