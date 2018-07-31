Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	st=int(input("Enter the number of stairs.."))
	i=0
	for i in range
	
SyntaxError: invalid syntax
>>> def main():
	st=int(input("Enter the number of stairs.. "))
	i=0
	j=0
	no=[]
	su=0
	for i in range(st):
		no[i]=int(input("Enter the numbers.. "))
	for i in range(len(no)):
		for j in range(i):
			su=su+no[j]
	print su

	
>>> main()
Enter the number of stairs.. 5
Enter the numbers.. 1

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    main()
  File "<pyshell#12>", line 8, in main
    no[i]=int(input("Enter the numbers.. "))
IndexError: list assignment index out of range
>>> def main():
	st=int(input("Enter the number of stairs.. "))
	i=0
	j=0
	no=[]
	su=0
	for i in range(st):
		c=int(input("Enter the numbers.. "))
		no.append(c)
	for i in range(len(no)):
		for j in range(i):
			su=su+no[j]
	print su

	
>>> main()
Enter the number of stairs.. 5
Enter the numbers.. 1
Enter the numbers.. 2
Enter the numbers.. 3
Enter the numbers.. 4
Enter the numbers.. 5
20
>>> main()
Enter the number of stairs.. 3
Enter the numbers.. 1
Enter the numbers.. 1
Enter the numbers.. 1
3
>>> main()
Enter the number of stairs.. 3
Enter the numbers.. 1
Enter the numbers.. 2
Enter the numbers.. 3
4
>>> def main():
	st=int(input("Enter the number of stairs.. "))
	i=0
	j=0
	no=[]
	su=0
	for i in range(st):
		c=int(input("Enter the numbers.. "))
		no.append(c)
	for i in range(len(no)):
		for j in range(i):
			su=su+no[j]
	print su
