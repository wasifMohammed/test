>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	i=0
	li=[]
	tot=0
	actual=0
	dif=0
	for i in range(n):
		li.append(int(input()))
	li.remove(li[k])
	share=int(input("Cost charged.. "))
	#print li
	for i in range(len(li)):
		tot+=li[i]
	actual=tot/2
	#print tot
	#print actual
	if share==actual:
		print "Bon Appetite"
	elif share!=actual:
		dif=share-actual
		print dif
