li = []
for i in range(5):
	guess = input("请输入名字")
	li.append(guess)
li.pop(1)
print(li[3])
li[3] = "laowang"
for i in li:
	print(li)
