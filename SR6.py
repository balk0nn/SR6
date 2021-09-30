a = input("Введите последовательность натуральных чисел через пробел  " )
array = [int(i) for i in a.split (" ") if i.isdigit () ]
print (array)
print ("Введите DELTA(должно быть натуральным числом)")
try:
	delta = int(input())
except ValueError:
	print ("Введенное вами DELTA не удовлетворяет требованиям")
	exit()
	
if delta < 0:
	print ("Введенное вами DELTA не удовлетворяет требованиям")
	exit()

b = min (array)
print(b)



