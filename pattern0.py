a=int(input("Enter value: "))
for i in range(1,a+1):
	print(' ' * (a-i), end="")
	print('* ' * i)
