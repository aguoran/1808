i = 1
sum_s = 0
sum_b = 0
while i <100:
	if i%2!=0:
		sum_s +=i
	else:
		sum_b -=i
	i+=1
print(sum_s+sum_b)
