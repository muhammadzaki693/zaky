import math

Pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

def Add(*a):
	total = a[0]
	for num in a:
		total += num
	return total

def Sub(*a):
	total = a[0]
	for num in a:
		total -= num
	return total

def Mul(*a):
	total = a[0]
	for num in a:
		total *= num
	return total

def Div(*a):
	total = a[0]
	for num in a:
		total /= num
	return total

def Pow(a,b):
	return a**b

def FlDiv(*a):
	total = a[0]
	for num in a:
		total /= num
	return math.floor(total)