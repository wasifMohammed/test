def gcd(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			return gcd(n-m,m)
		else:
			return gcd(n,m-n)
def main():
	s=int(input("Enter size of array.."))
	q=int(input("Enter no. of queries.."))
	arr=[]
	a=[]
	b=[]
	i=1
	j=0
	for i in range(s):
		arr.append(input("Element "))
	for i in range((q*2)):
		a.append(input("Query "))
	
	
	for i in range(len(a)/2):
		for j in range(i):
			p=a[j]
			q=a[j+1]
			y=arr[p-1]
			z=arr[q-1]
			if(y not in arr or z not in arr):
				fl=1
			else:

				b.append(gcd(y,z))
				fl=0
			
	if(fl==1):
		print "One of the elements isn't in the array.."
	else:
		for i in range((len(a)/2)):
			print b[i]

main()