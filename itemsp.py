items=int(input("enter total items: "))
price=int(input("enter total price: "))

p10=price*0.10
p20=price*0.20
p30=price*0.30
p50=price*0.50

if items<=15:
	print("final price is: ",price-p10)
elif items<=30:
	print("final price is: ",price-p20)
elif items<=50:
	print("final price is: ",price-p30)
elif items<=100:
	print("final price is: ",price-p50)
