#leap year
# year=int(input("enter any year:"))

# if year%4==0:
	# if year%100==0:
		# if year%400==0:
			# print("enter year is a leap year")
		# else:
			# ("enter year is not a leap year")
	# else:
		# print("enter year is not a leap year")
# else:
	# print("enter year is not a leap year")
	
   

# x=int(input("enter length of square "))
# y=int(input("enter breadth of sqaure"))
# if x==y:
	# print("it is a square")
# else:
	# print("it is a rectangle")
	
	
# x=1
# y=2
# z=3

# if x>y:
	# if x>z:
		# print(x,"is oldest")
	# else:
		# print(z,"is oldest")
# else:
	# if y>z:
		# print(y,"is oldest")
	# else:
		# print(z,"is oldest")
# if x<y:
	# if x<z:
		# print(x,"is youngest")
	# else:
		# print(z,"is youngest")
# else:
	# if y<z:
		# print(y,"is youngest")
	# else:
		# print(z,"is youngest")
		
		
# point=int(input("enter your point between 1 to 200"))
# if point<=50:
	# print("sorry! no prize this time ")
# elif point>=51 and point<=150:
	# print("congratulation! you won a wooden dog")
# elif point>=151 and point<=180:
	# print("congratulation! you have won a book")
# elif point>=151 and point<=200:
	# print("congratulation! you won a chocolate")
# else:
	# print("please enter the point between 1to 200")
	
	
print("price of 1 unit=100")
unit=int(input("enter the units you want to purchase"))	
price=unit*100
if price>1000:
	print("you have to pay:",price/10)
else:
	print("you have to pay", price)