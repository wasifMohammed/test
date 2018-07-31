Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	newmax=0
	newmin=0
	new=[]
	for i in range(n):
		c=int(input("element.. "))
		li.append(c)
	for i in range(len(li)):
		newmax=max(li)
		newmin=min(li)
		new.append(newmax)
		new.append(newmin)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    main()
  File "<pyshell#14>", line 11, in main
    newmax=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	newmax=0
	newmin=0
	new=[]
	for i in range(n):
		c=int(input("element.. "))
		li.append(c)
	print li
	for i in range(len(li)):
		newmax=max(li)
		newmin=min(li)
		new.append(newmax)
		new.append(newmin)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 5
element.. 10
element.. 35
element.. 14
element.. 25
element.. 67
[10, 35, 14, 25, 67]

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    main()
  File "<pyshell#17>", line 17, in main
    li.remove(min(li))
ValueError: min() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	newmax=0
	newmin=0
	new=[]
	for i in range(0,n):
		c=int(input("element.. "))
		li.append(c)
	for i in range(0,len(li)):
		newmax=max(li)
		newmin=min(li)
		new.append(newmax)
		new.append(newmin)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(0,len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    main()
  File "<pyshell#20>", line 11, in main
    newmax=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	newmax=0
	newmin=0
	new=[]
	for i in range(0,n):
		li.append(input("element.. "))
	for i in range(0,len(li)):
		newmax=max(li)
		newmin=min(li)
		new.append(newmax)
		new.append(newmin)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(0,len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    main()
  File "<pyshell#23>", line 10, in main
    newmax=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	for i in range(0,n):
		li.append(input("element.. "))
	for i in range(0,len(li)):
		newmax=max(li)
		newmin=min(li)
		new.append(newmax)
		new.append(newmin)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(0,len(new)):
		print new[i]

		
>>> main()
No. of Elements.. main()7

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    main()
  File "<pyshell#26>", line 2, in main
    n=int(input("No. of Elements.. "))
  File "<string>", line 1
    main()7
          ^
SyntaxError: unexpected EOF while parsing
>>> main()
No. of Elements.. 7
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    main()
  File "<pyshell#26>", line 13, in main
    li.remove(min(li))
ValueError: min() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	newmin=0
	for i in range(0,n):
		li.append(input("element.. "))
	for i in range(0,len(li)):
		newmax=max(li)
		newmin=min(li)
		new.append(newmax)
		new.append(newmin)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(0,len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    main()
  File "<pyshell#30>", line 9, in main
    newmax=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	maxnew=[]
	minnew=[]
	for i in range(0,n):
		li.append(input("element.. "))
	for i in range(0,len(li)):
		maxnew=max(li)
		minnew=min(li)
		new.append(newmax)
		new.append(newmin)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(0,len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    main()
  File "<pyshell#33>", line 12, in main
    new.append(newmax)
NameError: global name 'newmax' is not defined
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	maxnew=[]
	minnew=[]
	for i in range(0,n):
		li.append(input("element.. "))
	for i in range(0,len(li)):
		maxnew=max(li)
		minnew=min(li)
		new.append(maxnew)
		new.append(minnew)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(0,len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    main()
  File "<pyshell#36>", line 10, in main
    maxnew=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=iter([])
	new=iter([])
	
	for i in range(0,n):
		li.append(input("element.. "))
	for i in range(0,len(li)):
		maxnew=max(li)
		minnew=min(li)
		new.append(newmax)
		new.append(newmin)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(0,len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 8

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    main()
  File "<pyshell#39>", line 7, in main
    li.append(input("element.. "))
AttributeError: 'listiterator' object has no attribute 'append'
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	maxnew=[]
	minnew=[]
	for i in range(0,n):
		li.append(input("element.. "))
	for i in range(0,len(li)):
		maxnew=max(li)
		minnew=min(li)
		new.append(maxnew)
		new.append(minnew)
		li.remove(max(li))
		li.remove(min(li))
	for i in range(0,len(new)):
		print new[i]

		
>>> main()
No. of Elements.. 

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    main()
  File "<pyshell#42>", line 2, in main
    n=int(input("No. of Elements.. "))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
8
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    main()
  File "<pyshell#42>", line 10, in main
    maxnew=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	maxnew=[]
	minnew=[]
	for i in range(0,n):
		li.append(input("element.. "))
	for i in range(0,len(li)):
		maxnew=max(li)
		minnew=min(li)
		new.append(maxnew)
		new.append(minnew)
		li.remove(max(li))
		li.remove(min(li))
	print new

	
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    main()
  File "<pyshell#46>", line 10, in main
    maxnew=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	i=0
	for i in range(n):
		li.append(input("element.. "))
	
	for i in range(len(li)):
		maxnew=max(li)
		minnew=min(li)
		new.append(maxnew)
		new.append(minnew)
		li.remove(max(li))
		li.remove(min(li))
	print new

	
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    main()
  File "<pyshell#49>", line 10, in main
    maxnew=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	i=0
	for i in range(n):
		li.append(input("element.. "))
	print max(li)
	print min(li)
	for i in range(len(li)):
		maxnew=max(li)
		minnew=min(li)
		new.append(maxnew)
		new.append(minnew)
		li.remove(max(li))
		li.remove(min(li))
	print new

	
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15
623
3

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    main()
  File "<pyshell#52>", line 11, in main
    maxnew=max(li)
ValueError: max() arg is an empty sequence
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	i=0
	for i in range(n):
		li.append(input("element.. "))

	while len(li)=0:
		maxnew=max(li)
		minnew=min(li)
		new.append(maxnew)
		new.append(minnew)
		li.remove(max(li))
		li.remove(min(li))
	print new
	
SyntaxError: invalid syntax
>>> 
>>> def main():
	n=int(input("No. of Elements.. "))
	li=[]
	new=[]
	i=0
	for i in range(n):
		li.append(input("element.. "))

	while len(li)!=0:
		maxnew=max(li)
		minnew=min(li)
		new.append(maxnew)
		new.append(minnew)
		li.remove(max(li))
		li.remove(min(li))
	print new

	
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15
[623, 3, 19, 7, 15, 9, 11, 10]
>>> main()
No. of Elements.. 5
element.. 5
element.. 5
element.. 3
element.. 3
element.. 1

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    main()
  File "<pyshell#57>", line 15, in main
    li.remove(min(li))
ValueError: min() arg is an empty sequence
>>> main()
No. of Elements.. 6
element.. 5
element.. 5
element.. 3
element.. 3
element.. 1
element.. 0
[5, 0, 5, 1, 3, 3]
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
		elif len(li)%2==0:
			maxnew=max(li)
			minnew=min(li)
			new.append(maxnew)
			new.append(minnew)
			li.remove(max(li))
			li.remove(min(li))
		else:
			maxnew=max(li)
			minnew=min(li)
			new.append(maxnew)
			new.append(minnew)
			li.remove(max(li))
			li.remove(min(li))
			
	print new

	
>>> main()
No. of Elements.. 5
element.. 5
element.. 5
element.. 3
element.. 3
element.. 1
[5, 1, 5, 3, 3]
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15
[623, 3, 19, 7, 15, 9, 11, 10]
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

	
>>> main()
No. of Elements.. 8
element.. 7
element.. 623
element.. 19
element.. 10
element.. 11
element.. 9
element.. 3
element.. 15
[623, 3, 19, 7, 15, 9, 11, 10]
>>> main()
No. of Elements.. 5
element.. 5
element.. 5
element.. 3
element.. 3
element.. 1
[5, 1, 5, 3, 3]
>>> 
