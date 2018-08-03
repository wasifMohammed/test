>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	c=[]
	fl=[]
	minin=0
	k=(int(input("Enter the quantity of magic powder in grams.. ")))
	for i in range(n):
		fl.append("0")
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ",n
	print re
	print av
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
	print c
	print re
	print av
	minin=c.index(min(c))
	ch=av[minin]%re[minin]
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(ch<=re[minin]):
		c[minin]+=k
		#c[minin]=c[minin]/re[minin]
	print c[minin]
