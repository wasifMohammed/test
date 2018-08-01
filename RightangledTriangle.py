Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n):
			print "1"
		n-=1

		
>>> main()
3
1
1
1
1
1
1
>>> def main():
	n=int(input())
	i=0
	a=[]
	while(n>0):
		for i in range(n):
			a.append("1")
			print a
		n-=1

		
>>> main()
3
['1']
['1', '1']
['1', '1', '1']
['1', '1', '1', '1']
['1', '1', '1', '1', '1']
['1', '1', '1', '1', '1', '1']
>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n):
			print "1",
		n-=1

		
>>> main()
3
1 1 1 1 1 1
>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n):
			print "1", print "\n"
		n-=1
		
SyntaxError: invalid syntax
>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n):
			print "1", print "/n"
		n-=1
		
SyntaxError: invalid syntax
>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n):
			print "1", print \n
		n-=1
		
SyntaxError: invalid syntax
>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n):
			print "1",
			print "\n"
		n-=1

		
>>> main()
3
1 

1 

1 

1 

1 

1 

>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n,-1):
			print "1",
			print "\n"
		n-=1

		
>>> main()
3
>>> 
>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n):
			print "1",
			print "\n"
		n-=1

		
>>> main()
3
1 

1 

1 

1 

1 

1 

>>> def main():
	n=int(input())
	i=0
	while(n>0):
		for i in range(n):
			print "1",
		print "\n"
		n-=1

		
>>> main()
3
1 1 1 

1 1 

1 

>>> main()
5
1 1 1 1 1 

1 1 1 1 

1 1 1 

1 1 

1 

>>> 
