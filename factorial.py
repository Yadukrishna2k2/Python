def factorial(x):
	if x==0 or x==1:
		return x
	else:
		r=factorial(x-1)*x
		return r
n=int(input("enter the number:"))
v=factorial(n)
print("factorial of the number",n,"is =",v)

