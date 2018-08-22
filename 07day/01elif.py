
pwd = 123456
account = "123"
money = 9999

pw =int(input("请输入密码"))
acc =input("请输入账户")
if pw == pwd and acc == account:
	print("登录成功")
	mo = float(input("请输入取款金额"))
	if mo > money:
		print("余额不足")
	elif mo < money:
		print("取款成功")
else:
	print("登录失败") 
		
