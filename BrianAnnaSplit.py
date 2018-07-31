Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	i=0
	li=[]
	for i in range(n):
		li[i]=int(input())

		
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	share=int(input("Cost charged"))
	i=0
	li=[]
	tot=0
	for i in range(n):
		li[i]=int(input())
	li.remove(k)
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2
	
SyntaxError: invalid syntax
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	share=int(input("Cost charged"))
	i=0
	li=[]
	tot=0
	for i in range(n):
		li[i]=int(input())
	li.remove(k)
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2
	
SyntaxError: invalid syntax
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	share=int(input("Cost charged"))
	i=0
	li=[]
	tot=0
	for i in range(n):
		li[i]=int(input())
	li.remove(k)
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2:
		dif=share-tot/2
		print tot

		
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
Cost charged12
3

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    main()
  File "<pyshell#22>", line 9, in main
    li[i]=int(input())
IndexError: list assignment index out of range
>>>  def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	
	i=0
	li=[]
	tot=0
	for i in range(n-1):
		li[i]=int(input())
	li.remove(k)
	share=int(input("Cost charged.. "))
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2:
		dif=share-tot/2
		print tot

  File "<pyshell#24>", line 2
    def main():
    ^
IndentationError: unexpected indent
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	
	i=0
	li=[]
	tot=0
	for i in range(n-1):
		li[i]=int(input())
	li.remove(k)
	share=int(input("Cost charged.. "))
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2:
		dif=share-tot/2
		print tot

		
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
3

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    main()
  File "<pyshell#26>", line 9, in main
    li[i]=int(input())
IndexError: list assignment index out of range
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	
	i=0
	li=[]
	tot=0
	for i in range(n-1):
		li.append(int(input()))
	li.remove(k)
	share=int(input("Cost charged.. "))
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2:
		dif=share-tot/2
		print tot

		
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
3
10
2

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    main()
  File "<pyshell#29>", line 10, in main
    li.remove(k)
ValueError: list.remove(x): x not in list
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	i=0
	li=[]
	tot=0
	for i in range(n):
		li.append(int(input()))
	li.remove(li[k])
	share=int(input("Cost charged.. "))
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2:
		dif=share-tot/2
		print tot

		
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
3
10
2
9
Cost charged.. 12
[3, 2, 9]
14
14
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	i=0
	li=[]
	tot=0
	for i in range(n):
		li.append(int(input()))
	li.remove(li[k])
	share=int(input("Cost charged.. "))
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2:
		dif=share-tot/2
		print diff

		
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
3
10
2
9
Cost charged.. 12
[3, 2, 9]
14

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    main()
  File "<pyshell#35>", line 19, in main
    print diff
NameError: global name 'diff' is not defined
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	i=0
	li=[]
	tot=0
	diff=0
	for i in range(n):
		li.append(int(input()))
	li.remove(li[k])
	share=int(input("Cost charged.. "))
	print li
	for i in range(len(li)):
		tot+=li[i]
	print tot
	if share==tot/2:
		print "Bon Appetite"
	elif share!=tot/2:
		dif=share-tot/2
		print diff

		
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
3
10
2
9
Cost charged.. 12
[3, 2, 9]
14
0
>>> def main():
	n=int(input("The number of items ordered.. "))
	k=int(input("Index of element not consumed by anna.. "))
	i=0
	li=[]
	tot=0
	actual=0
	diff=0
	for i in range(n):
		li.append(int(input()))
	li.remove(li[k])
	share=int(input("Cost charged.. "))
	print li
	for i in range(len(li)):
		tot+=li[i]
	actual=tot/2
	print tot
	print actual
	if share==actual:
		print "Bon Appetite"
	elif share!=actual:
		dif=share-actual
		print dif

		
>>> main()
The number of items ordered.. 

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    main()
  File "<pyshell#41>", line 2, in main
    n=int(input("The number of items ordered.. "))
  File "F:\lib\idlelib\PyShell.py", line 1398, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
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
	print li
	for i in range(len(li)):
		tot+=li[i]
	actual=tot/2
	print tot
	print actual
	if share==actual:
		print "Bon Appetite"
	elif share!=actual:
		dif=share-actual
		print dif

		
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
3
10
2
9
Cost charged.. 12
[3, 2, 9]
14
7
5
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
3
10
4
9
Cost charged.. 8
[3, 4, 9]
16
8
Bon Appetite
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
	print li
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

		
>>> main()
The number of items ordered.. 4
Index of element not consumed by anna.. 1
3
10
4
9
Cost charged.. 8
[3, 4, 9]
Bon Appetite
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
