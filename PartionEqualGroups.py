Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num!=0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1

		
>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num!=0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1
	if(num==0 and c2==c1)
	
SyntaxError: invalid syntax
>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num!=0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1
	if(num==0 and c2==c1):
		print "yes"
	else:
		print "no"

		
>>> main()
Enter the number..10
a = 2
b = 3
yes
>>> main()
Enter the number..20
a = 2
b = 3
yes
>>> main()
Enter the number..20
a = 5
b = 4

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    main()
  File "<pyshell#19>", line 13, in main
    c2+=1
KeyboardInterrupt

h
rd
>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num!=0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1
		else:
			return c2
	if(num==0 and c2==c1):
		print "yes"
	else:
		print "no"

		
>>> main()
Enter the number..20
a = 5
b = 4

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    main()
  File "<pyshell#24>", line 9, in main
    num=num-a
KeyboardInterrupt
>>> main()
Enter the number..2
a = 1
b = 1
yes
>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num!=0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1
		else:
			c2=c2
	if(num==0 and c2==c1):
		print "yes"
	else:
		print "no"

		
>>> main()
Enter the number..20
a = 5
b = 4

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    main()
  File "<pyshell#28>", line 13, in main
    c2+=1
KeyboardInterrupt
5
4
3
3
4
5
>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num!=0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1
		else:
			print "no"
	if(num==0 and c2==c1):
		print "yes"
	else:
		print "no"

		
>>> main()
Enter the number..20
a = 5
b = 4

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    main()
  File "<pyshell#31>", line 12, in main
    num=num-b
KeyboardInterrupt

>>> main()
Enter the number..20
a = 2
b = 3
yes
>>> main()
Enter the number..20
a = 5
b = 4

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    main()
  File "<pyshell#31>", line 9, in main
    num=num-a
KeyboardInterrupt
>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num>=0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1
		else:
			print "no"
	if(num==0 and c2==c1):
		print "yes"
	else:
		print "no"

		
>>> def main():
	num=int(input("Enter the number.."))
	a=int(input("a = "))
	b=int(input("b = "))
	i=0
	c1=0
	c2=0
	while num>0:
		num=num-a
		c1+=1
		if(num!=0):
			num=num-b
			c2+=1
		else:
			print "no"
	if(num==0 and c2==c1):
		print "yes"
	else:
		print "no"

		
>>> main()
Enter the number..20
a = 2
b = 3
yes
>>> main()
Enter the number..20
a = 5
b = 4
no
>>> 
