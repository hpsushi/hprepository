
for mei in range(1,100//5):
	for yiban in range(1,100//3):
		for chou in range(100):
			if mei+yiban+chou == 100 and mei*5+yiban*3+chou*1/3 ==100:
				print(mei,chou,yiban)
