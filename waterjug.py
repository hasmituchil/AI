m = 0
n = 0
d = 0
gcd = 0
continue = 0
def gcd(x, y):
	for i==1 and i <= x and i <= y:
		if (x%i == 0 and y%i ==0):
			gcd = i
			return i 

def redo():
	m = input("Enter smaller bucket")
	n = input("Enter larger bucket")
	d = input("Enter desired water")

redo()
s = gcd(m,n)
if d % gcd == 0:
	print("Great Inputs!")
	continue = 1

if continue == 0:
	redo()

if continue == 1:
	k = 0
	while k<m:
		k+=n
		print ("Add" +m+ "litres")
	print("You have" + k + "litres")
	
