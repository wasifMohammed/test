>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num>0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1
		else:
			print "no"
	if(num==0 and c2==c1):
		print "yes"
	else:
		print "no"

		
>>> main()

