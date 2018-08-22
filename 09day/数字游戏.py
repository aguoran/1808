import random
computer = random.randint(1,100)
for i in range(1,10):
	player = int(input("请输入1-100内任何一个数:"))
	if player > computer:
		print("太大了")
	elif player < computer:
		print("太小了")
	elif player == computer:
		print("猜中了")
		break

		

