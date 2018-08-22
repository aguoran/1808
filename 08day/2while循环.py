oushu_num_sum = 0
jishu_num_sum = 0
mun = 100
while num > 0:
	if num % 2 == 0:
		oushu_num_sum = oush_sum + num
	else:
		jushu_num_sum += num
	num -= 1
print("偶数总和是:%d"%oushu_num_sum)
print("奇数总和是:%d"%jishu_num_sum)


