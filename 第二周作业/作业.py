li = []
for i in range(5):
	guess = input("请输入五个成绩")
	li.append(guess)
for i in li:
	li.sort()
print(li)
