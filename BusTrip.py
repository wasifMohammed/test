Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main()
SyntaxError: invalid syntax
>>> def main():
	ep=int(input("Enter endpoint.. "))
	c=int(input("Enter capacity.. "))
	gs=int(input("Enter gas station.. "))
	noj=int(input("Enter the no. of journeys.. "))
	i=0
	fuel=c
	count=0
	while(i<noj):
		if(gs<=c):
			if(c>=ep):
				fuel-=gs
			while(fuel<c):
				fuel+=1
			fuel-=(ep-gs)
			if(fuel>=0):
				count+=1
			else:
				count=count
			if(fuel>=ep=gs):
				
SyntaxError: invalid syntax
>>> def main():
	ep=int(input("Enter endpoint.. "))
	c=int(input("Enter capacity.. "))
	gs=int(input("Enter gas station.. "))
	noj=int(input("Enter the no. of journeys.. "))
	i=0
	fuel=c
	count=0
	while(i<noj):
		if(gs<=c):
			if(c>=ep):
				fuel-=gs
			while(fuel<c):
				fuel+=1
			fuel-=(ep-gs)
			if(fuel>=0):
				count+=1
			else:
				count=count
			if(fuel>=ep-gs):
				while(fuel<c):
					fuel+=1
				fuel-=gs
				if(fuel>=0):
					count+=1
				else:
					count=count
		i+=1
	print count

	
>>> main()
Enter endpoint.. 6
Enter capacity.. 9
Enter gas station.. 2
Enter the no. of journeys.. 4
8
>>> main()
Enter endpoint.. 10
Enter capacity.. 4
Enter gas station.. 6
Enter the no. of journeys.. 10
0
>>> def main():
	ep=int(input("Enter endpoint.. "))
	c=int(input("Enter capacity.. "))
	gs=int(input("Enter gas station.. "))
	noj=int(input("Enter the no. of journeys.. "))
	i=0
	fuel=c
	count=0
	while(i<noj):
		while(i<count):
			if(gs<=c):
				if(c>=ep):
					fuel-=gs
				#on reaching fuel station.
				while(fuel<c):
					fuel+=1 #refill
				fuel-=(ep-gs)
				if(fuel>=0):
					count+=1 
				else:
					count=count
				if(fuel>=ep-gs):
					#on reaching fuel station.
					while(fuel<c):
						fuel+=1 #refill
						
					fuel-=gs
					if(fuel>=0):
						count+=1
					else:
						count=count
		i+=1
	print count

	
>>> main()
Enter endpoint.. 6
Enter capacity.. 9
Enter gas station.. 2
Enter the no. of journeys.. 4
0
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
				else:
					count=count
				if(fuel>=ep-gs):
					#on reaching fuel station.
					while(fuel<c):
						fuel+=1 #refill

					fuel-=gs
					if(fuel>=0):
						count+=1
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
