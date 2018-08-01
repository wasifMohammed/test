>>> def main():
	ep=int(input("Enter endpoint.. "))
	c=int(input("Enter capacity.. "))
	gs=int(input("Enter gas station.. "))
	noj=int(input("Enter the no. of journeys.. "))
	i=0
	fuel=c
	count=0
	while(i<noj):
		while(count<noj):
			if(gs<=c):
				if(c>=ep):
					fuel-=gs
				#on reaching fuel station.
				while(fuel<c):
					fuel+=1 #refill
				fuel-=(ep-gs)
				if(fuel>=0):
					count+=1
					#on completing journey towards endpoint
				else:
					count=count
				if(fuel>=ep-gs):
					#on reaching fuel station.
					while(fuel<c):
						fuel+=1 #refill

					fuel-=gs
					if(fuel>=0):
						count+=1
						#on completing journey back to the starting point
					else:
						count=count
		i+=1
	print count

	
>>> main()
Enter endpoint.. 6
Enter capacity.. 9
Enter gas station.. 2
Enter the no. of journeys.. 4
4
>>> 
