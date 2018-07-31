>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	i=0
	for i in range(n):
		li.append(input("element.. "))

	while len(li)!=0:
		if len(li)==1:
			maxnew=max(li)
			new.append(maxnew)
			li.remove(max(li))
		
		else:
			maxnew=max(li)
			minnew=min(li)
			new.append(maxnew)
			new.append(minnew)
			li.remove(max(li))
			li.remove(min(li))
			
	print new
