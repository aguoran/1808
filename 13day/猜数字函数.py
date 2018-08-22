def caishuzi():
	import random
	computer = random.randint(1,100)
	player = int(input("请输入数字"))
	if player > computer:
		print("太大啦")
	elif player < computer:
		print("太小了")
	elif player == computer:
		print("猜中了")

for i in range(5):
	caishuzi()
		
