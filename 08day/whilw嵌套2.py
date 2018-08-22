i = 1
while i <= 9:
	j = 1
	while j <= i:
		sum_w = i*j
		print("%d*%d=%d"%(i,j,sum_w),end="")	
		j+=1
	print("")
	i+=1
