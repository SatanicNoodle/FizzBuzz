def capba(num):
	for number in range(1,num+1):
		if number %3 != 0 and number %5 != 0:
			print(number)
		elif number %3 == 0 and number %5 == 0:
			print("FizzBuzz")
		elif number %5 == 0:
			print("Buzz")
		elif number %3 == 0:
			print("Fizz")
capba(15)

