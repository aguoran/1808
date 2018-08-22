import time
print("欢迎来到麒麟网咖".center(30,"*"))
list_ = []
while True:
	print("1 上机")
	print("2 下机")
	num =int(input("请选择功能:"))
	if num == 1:
		d = {}
		card = input("请输入身份证")
		money = float(input("请输入金额"))
		d["card"] = card
		d["money"]= money
		d["time"]= int(time.time())
		list_.append(d)
		print(list_)
		print("上机")
	elif num == 2:
		print("下机")
		card = input("请输入身份证号")
		for i in list_:
			if i["card"]==card:
				endtime = int(time.time())
				diff_money = (endtime-i["time"])*10
				diff = i["money"] - diff_money
				if diff < 0:
					money = float(input("请输入金额"))
				print("上网花了%0.2f元,还剩%0.2f元"%(diff_money,diff))
			break

	 
