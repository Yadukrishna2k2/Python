def is_palindrome(n):
	n_str=str(n)
	n_rev=n_str[::-1]
	if n_str==n_rev:
		return True
	else:
		return False
n=input("enter a value\n")
result=is_palindrome(n);
if result==True:
	print("The value is palindrome")
else:
	print("The value is not palindrome")
	
