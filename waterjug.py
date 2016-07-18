from fractions import gcd

cont = 0
m = 1
n = 1
d = 1

def redo():
	global m
	global n
	global d
	m = int(input("Enter larger bucket"))
	n = int(input("Enter smaller bucket"))
	d = int(input("Enter desired water"))


redo()

s = gcd(m,n)



if d % s == 0:
	print("Great Inputs!")
	cont = 1

if cont == 0:
	print("Hmmmmm.... Try harder")
	redo()


if cont == 1:
	k = 0
	while k<m:
		k+=n
		print ('Add {} litres'.format(n))
		if k == d:
			print("Got desired water")
		
	print ('Have {} litres'.format(k))
	k -= m
	print ('Remove {} litres'.format(m))
	if k == d:
		print("Done")

	
	
	
	
	
	
	
	
	
	
	
	
	
