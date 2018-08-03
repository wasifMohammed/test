Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main()
SyntaxError: invalid syntax
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[n]
	av=[n]
	for i in range(n):
		re[i].append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av[i].append(input("Enter the available quantity in grams.. "))
	print "n = ", n
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    main()
  File "<pyshell#13>", line 6, in main
    re[i].append(input("Enter the required quantity in grams.. "))
AttributeError: 'int' object has no attribute 'append'
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[n]
	av=[n]
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ", n
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[3, 2, 1, 4]
[3, 11, 3, 16]
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ",n
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ",n
	print re
	print av
	for i in range(n):
		if(av[i]>0 and re[i]>0)
		
SyntaxError: invalid syntax
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	count=0
	k=(int(input("Enter the quantity of magic powder in grams.. ")))
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ",n
	print re
	print av
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			while(av[i]>0):
				av[i]-=re[i]
				print av[i]

				
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
9
7
5
3
1
-1
2
1
0
12
8
4
0
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	count=0
	k=(int(input("Enter the quantity of magic powder in grams.. ")))
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ",n
	print re
	print av
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>0 and av[i]>=re[i]):
				av[i]-=re[i]
				print av[i]

				
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
9
2
12
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	count=0
	k=(int(input("Enter the quantity of magic powder in grams.. ")))
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ",n
	print re
	print av
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			while(av[i]>=re[i]):
				av[i]-=re[i]
				print av[i]

				
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
9
7
5
3
1
2
1
0
12
8
4
0
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	count=0
	k=(int(input("Enter the quantity of magic powder in grams.. ")))
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ",n
	print re
	print av
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			while(av[i]>=re[i]):
				av[i]-=re[i]
				print av[i]
		if i in av != 0:
			count+=1
			print "count = ",count

			
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
9
7
5
3
1
2
1
0
count =  1
12
8
4
0
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	count=0
	k=(int(input("Enter the quantity of magic powder in grams.. ")))
	for i in range(n):
		re.append(input("Enter the required quantity in grams.. "))
	for i in range(n):
		av.append(input("Enter the available quantity in grams.. "))
	print "n = ",n
	print re
	print av
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			while(av[i]>=re[i]):
				av[i]-=re[i]
				print av[i]
	if i in av != 0:
		count+=1
		print "count = ",count

		
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
9
7
5
3
1
2
1
0
12
8
4
0
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	c=0
	fl=[]
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
				av[i]%=re[i]
				print av[i]

				
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	c=0
	fl=[]
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
				av[i]%=re[i]
				c=av[i]/re[i]
				print av[i]
				print c

				
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
0
0
0
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	c=0
	fl=[]
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
				c=av[i]/re[i]
				av[i]%=re[i]
				
				print av[i]
				print c

				
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
5
0
3
0
4
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	c=[]
	fl=[]
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

				
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	c=[]
	fl=[]
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
				print min(c)

				
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
5
0
3
0
3
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	c=[]
	fl=[]
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
	print min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
3
>>> def main():
	n=(int(input("Enter the number of ingredients.. ")))
	re=[]
	av=[]
	c=[]
	fl=[]
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
	print min(c)
	print c.index(min(c))

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
3
1
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
	minin=c.index(min(c))
	
	print "minin ", minin		
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
minin  1
min(c) 3
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
	minin=c.index(min(c))
	print "av[c] ", av[c]
	print "re[c]", re[c]
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
av[c] 

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    main()
  File "<pyshell#75>", line 26, in main
    print "av[c] ", av[c]
TypeError: list indices must be integers, not list
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
	minin=c.index(min(c))
	print "av[minin] ", av[minin]
	print "re[minin]", re[minin]
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
av[minin]  0
re[minin] 1
min(c) 3
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
	minin=c.index(min(c))
	if(av[minin]<=re[minin]):
		if(k >= re[minin]):
			while(av[minin]<re[minin]):
				av[minin]+=1
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
0
[5, 3, 4, 1]
min(c) 1
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
	minin=c.index(min(c))
	if(av[minin]<=re[minin]):
		if(k >= re[minin]):
			while(av[minin]<re[minin]):
				av[minin]+=1
	print av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
1
0
[5, 3, 4, 1]
min(c) 1
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
	minin=c.index(min(c))
	print "av[minin]", av[minin]
	print "av[i] ",av[1]
	if(av[minin]<=re[minin]):
		if(k >= re[minin]):
			while(av[minin]<re[minin]):
				av[minin]+=1
	print av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
av[minin] 0
av[i]  0
1
0
[5, 3, 4, 1]
min(c) 1
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
	minin=c.index(min(c))
	print minin
	print "av[minin]", av[minin]
	print "av[i] ",av[1]
	if(av[minin]<=re[minin]):
		if(k >= re[minin]):
			while(av[minin]<re[minin]):
				av[minin]+=1
	print av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
1
av[minin] 0
av[i]  0
1
0
[5, 3, 4, 1]
min(c) 1
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
			minin=c.index(min(c))
			print minin
			print "av[minin]", av[minin]
			print "av[i] ",av[i]
	if(av[minin]<=re[minin]):
		if(k >= re[minin]):
			while(av[minin]<re[minin]):
				av[minin]+=1
	print av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
av[minin] 1
av[i]  1
0
[5, 3]
1
av[minin] 0
av[i]  0
0
[5, 3, 4]
1
av[minin] 0
av[i]  0
1
0
[5, 3, 4, 1]
min(c) 1
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
		minin=c.index(min(c))
		print minin
		print "av[minin]", av[minin]
		print "av[i] ",av[i]
	if(av[minin]<=re[minin]):
		if(k >= re[minin]):
			while(av[minin]<re[minin]):
				av[minin]+=1
	print av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
av[minin] 1
av[i]  1
0
[5, 3]
1
av[minin] 0
av[i]  0
0
[5, 3, 4]
1
av[minin] 0
av[i]  0
1
0
[5, 3, 4, 1]
min(c) 1
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
	minin=c.index(min(c))
	print minin
	print "av[minin]", av[minin]
	print "av[i] ",av[i]
	if(av[minin]<=re[minin]):
		if(k >= re[minin]):
			while(av[minin]<re[minin]):
				av[minin]+=1
	print av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
1
av[minin] 0
av[i]  0
1
0
[5, 3, 4, 1]
min(c) 1
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
	minin=c.index(min(c))
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(av[minin]<=re[minin]):
		if(k >= re[minin]):
			while(av[minin]<re[minin]):
				av[minin]+=1
	print av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
1
av[minin] 0
re[minin]  1
1
0
[5, 3, 4, 1]
min(c) 1
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
	minin=c.index(min(c))
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
1
av[minin] 0
re[minin]  1
1
0
[5, 3, 4, 1]
min(c) 1
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
	minin=c.index(min(c))
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
1
av[minin] 0
re[minin]  1
av[minin] after adding required..  1
0
[5, 3, 4, 1]
min(c) 1
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
	minin=c.index(min(c))
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print av
	print re

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
1
av[minin] 0
re[minin]  1
av[minin] after adding required..  1
0
[5, 3, 4, 1]
min(c) 1
[1, 0, 0]
[2, 1, 4]
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
	minin=c.index(min(c))
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
1
av[minin] 0
re[minin]  1
av[minin] after adding required..  1
0
[5, 3, 4, 1]
min(c) 1
[2, 1, 4]
[1, 0, 0]
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
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
av[minin] after adding required..  1
0
[5, 3, 4, 1]
min(c) 1
[2, 1, 4]
[1, 0, 0]
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
	while(min(av)>0):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print re
	print av
	d=min(c)
	minin=c.index(d)
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
0
[4]
[2, 1, 4]
[11, 3, 0]
0
av[minin] 11
re[minin]  2
av[minin] after adding required..  11
1
[4, 5]
0
[4, 5, 3]
min(c) 3
[2, 1, 4]
[1, 0, 0]
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
	while(min(av)>0):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/(min(av)/re[av.index(min(av))]))
				av[i]%=re[i]
				print av[i]
				print c
	print re
	print av
	d=min(c)
	minin=c.index(d)
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	while(av[minin]<re[minin]):
		av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
0
[5]
[2, 1, 4]
[11, 3, 0]
0
av[minin] 11
re[minin]  2
av[minin] after adding required..  11
1
[5, 5]
0
[5, 5, 3]
min(c) 3
[2, 1, 4]
[1, 0, 0]
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
	while(min(av)>0):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print re
	print av
	d=min(c)
	minin=c.index(d)
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
0
[4]
[2, 1, 4]
[11, 3, 0]
0
av[minin] 11
re[minin]  2
av[minin] after adding required..  11
1
[4, 5]
0
[4, 5, 3]
min(c) 3
[2, 1, 4]
[1, 0, 0]
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
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
[5]
0
[5, 3]
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
av[minin] after adding required..  1
0
[5, 3, 4, 1]
min(c) 1
[2, 1, 4]
[1, 0, 0]
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
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(k >= re[minin]):
		while(av[minin]<re[minin]):
			av[minin]+=1
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
av[minin] after adding required..  1
0
[5, 3, 4, 1]
min(c) 1
[2, 1, 4]
[1, 0, 0]
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
	ch=av[minin]%=re[minin]
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(ch==0):
		while(av[minin]<re[minin]):
			av[minin]+=k
	print c
	print re
	print av
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av
	
SyntaxError: invalid syntax
>>> 
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
	ch=av[minin]%=re[minin]
	print minin
	print "av[minin]", av[minin]
	print "re[minin] ",re[minin]
	if(ch==0):
		while(av[minin]<re[minin]):
			av[minin]+=k
	print c
	print re
	print av
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av
	
SyntaxError: invalid syntax
>>> 
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
	if(ch==0):
		while(av[minin]<re[minin]):
			av[minin]+=k
	print c
	print re
	print av
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
[5, 3, 4]
[2, 1, 4]
[1, 1, 0]
av[minin] after adding required..  1
0
[5, 3, 4, 1]
min(c) 1
[2, 1, 4]
[1, 0, 0]
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
	if(ch==0):
		while(av[minin]<re[minin]):
			av[minin]+=k
	print c
	print re
	print av
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				#c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
[5, 3, 4]
[2, 1, 4]
[1, 1, 0]
av[minin] after adding required..  1
0
[5, 3, 4]
min(c) 3
[2, 1, 4]
[1, 0, 0]
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
		while(av[minin]<re[minin]):
			av[minin]+=k
	print c
	print re
	print av
	print "av[minin] after adding required.. ",av[minin]
	for i in range(n):
		if(av[i]>0 and re[i]>0):
			if(av[i]>=re[i]):
				#c.append(av[i]/re[i])
				av[i]%=re[i]
				print av[i]
				print c
	print "min(c)", min(c)
	print re
	print av

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
[5, 3, 4]
[2, 1, 4]
[1, 1, 0]
av[minin] after adding required..  1
0
[5, 3, 4]
min(c) 3
[2, 1, 4]
[1, 0, 0]
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
		while(av[minin]<re[minin]):
			av[minin]+=k
		av[minin]=av[minin]/re[minin]
	print c
	print re
	print av
	print av[minin]

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
[5, 3, 4]
[2, 1, 4]
[1, 1, 0]
1
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
		for i in c:
			while(c[i]<re[minin]):
				c[i]+=k
			c[i]=c[i]/re[minin]
	print c
	print re
	print av
	print c[minin]

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1

Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    main()
  File "<pyshell#153>", line 34, in main
    while(c[i]<re[minin]):
IndexError: list index out of range
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
		for i in range (c):
			while(c[i]<re[minin]):
				c[i]+=k
			c[i]=c[i]/re[minin]
	print c
	print re
	print av
	print c[minin]

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1

Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    main()
  File "<pyshell#156>", line 33, in main
    for i in range (c):
TypeError: range() integer end argument expected, got list.
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
		for i in range (len(c)):
			while(c[i]<re[minin]):
				c[i]+=k
			c[i]=c[i]/re[minin]
	print c
	print re
	print av
	print c[minin]

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
3
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
		while(c[minin]<re[minin]):
			c[minin]+=k
			#c[minin]=c[minin]/re[minin]
	print c
	print re
	print av
	print c[minin]

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
3
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
	print c
	print re
	print av
	print c[minin]

	
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 

Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    main()
  File "<pyshell#165>", line 12, in main
    re.append(input("Enter the required quantity in grams.. "))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> main()
Enter the number of ingredients.. 3
Enter the quantity of magic powder in grams.. 1
Enter the required quantity in grams.. 2
Enter the required quantity in grams.. 1
Enter the required quantity in grams.. 4
Enter the available quantity in grams.. 11
Enter the available quantity in grams.. 3
Enter the available quantity in grams.. 16
n =  3
[2, 1, 4]
[11, 3, 16]
1
0
0
[5, 3, 4]
[2, 1, 4]
[1, 0, 0]
1
av[minin] 0
re[minin]  1
[5, 4, 4]
[2, 1, 4]
[1, 0, 0]
4
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
