number = str(raw_input("enter the credit card number : "))

length = len(number)
print("length of the credit card number is "+str(length))
sumeven=0
sumodd=0
if length>=13 and length<=16 :
	for i in range(length-2,-1, -2):
		
		num = int(number[i])*2
		
		if num>9:
			strnum=str(num)
			num=eval(strnum[0]) + eval(strnum[1])
		sumeven+=num
	print(sumeven)
	for i in range(length-1,-1,-2):
		num1=int(number[i])
		sumodd+=num1
	print(sumodd)
	total_sum = sumodd+sumeven
	print(total_sum)
	t=total_sum%10
	print(t)
	if t == 0 :
		print("the card number is valid")
	else:
		print("invalid")
else:
	print("the card number is invalid")
		
		
