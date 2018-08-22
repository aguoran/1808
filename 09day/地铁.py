di = 7
al = 0
for i in range(60):
	if di <= 6:
		price = 3
	elif di > 6 and di <=12:
		price = 4
	elif di > 12 and  di <=22:
		price = 5
	elif di > 22 and di <=32:
		price = 6
	elif di > 32:
		if (di-32)%20 == 0:
			price=6+(di-32)/20
		else:
			price = 6 + int((di-32)/20)+1
	if al >= 100 and al <=150:
		price = price*0.8
	elif al >150 and al <=400:
		price = price*0.5
	al+=price
print("一共花了%.2f"%al) 
		

