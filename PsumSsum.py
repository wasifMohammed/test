>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	j=0
	fl=0
	for i in range(n):
		a.append(input("element.. "))
	for i in range(n):
		psum=0
		ssum=0
		for j in range(0,i):
			psum=psum+a[j]
		for k in range(i+1,n):
			ssum=ssum+a[k]
		if(psum==ssum):
			fl=1
			print "yes"
	if fl==0:
		print "no"
