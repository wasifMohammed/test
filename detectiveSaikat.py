>>> def main():
	st=int(input("Enter the number of stairs.. "))
	i=0
	j=0
	no=[]
	su=0
	for i in range(st):
		c=int(input("Enter the numbers.. "))
		no.append(c)
	for i in range(len(no)):
		for j in range(i):
			su=su+no[j]
	print su
