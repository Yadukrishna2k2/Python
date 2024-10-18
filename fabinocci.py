def fibonacci(x):
	if x==0 or x==1:
		return x
	else:
		r=fibonacci(x-1)+fibonacci(x-2)
		return r
n=int(input("enter a number: "))
for i in range(0,n-1):
	r=fibonacci(i)
	print(r)
	
