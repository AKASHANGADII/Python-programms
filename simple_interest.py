
def simple_interest(p,t,r):
	print('The principal is', p)
	print('The time period is', t)
	print('The rate of interest is',r)
	
	si = (p * t * r)/100
	
	print('The Simple Interest is', si)
	return si
	
p=int(input("Enter the principle amount>>"))
t=int(input("Enter the time>>"))
r=int(input("Enter the rate of interest>>"))
simple_interest(p, t, r)
