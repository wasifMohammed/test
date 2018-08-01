Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	n=int(input("No. of elements"))
	i=0
	a=[]
	psum=0
	ssum=0
	for i in range(n):
		a[i]=int(input("element.. "))
	for i in range(n):
		print a[i]

		
>>> main()
No. of elements5
element.. 1

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    main()
  File "<pyshell#8>", line 8, in main
    a[i]=int(input("element.. "))
IndexError: list assignment index out of range
>>> def main():
	n=int(input("No. of elements"))
	i=0
	a=[]
	psum=0
	ssum=0
	for i in range(n-1):
		a[i]=int(input("element.. "))
	for i in range(n):
		print a[i]

		
>>> main()
No. of elements5
element.. 1

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    main()
  File "<pyshell#11>", line 8, in main
    a[i]=int(input("element.. "))
IndexError: list assignment index out of range
>>> def main():
	n=int(input("No. of elements"))
	i=0
	a=[]
	psum=0
	ssum=0
	for i in range(n-1):
		a[i]=int(input("element.. "))
	for i in range(n-1):
		print a[i]

		
>>> main()
No. of elements5
element.. 1

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    main()
  File "<pyshell#14>", line 8, in main
    a[i]=int(input("element.. "))
IndexError: list assignment index out of range
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	for i in range(n):
		a[i]=int(input("element.. "))
	print a

	
>>> main()
No. of elements.. 5
element.. 1

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    main()
  File "<pyshell#18>", line 8, in main
    a[i]=int(input("element.. "))
IndexError: list assignment index out of range
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	for i in range(n):
		a[i].append(input("element.. "))
	print a

	
>>> main()
No. of elements.. 5

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    main()
  File "<pyshell#21>", line 8, in main
    a[i].append(input("element.. "))
IndexError: list index out of range
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	for i in range(n-1):
		a[i].append(input("element.. "))
	print a

	
>>> main()
No. of elements.. 5

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    main()
  File "<pyshell#24>", line 8, in main
    a[i].append(input("element.. "))
IndexError: list index out of range
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	for i in range(n-1):
		a.append(input("element.. "))
	print a

	
>>> main()
No. of elements.. 5
element.. 1
element.. 2
element.. 3
element.. 

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    main()
  File "<pyshell#27>", line 8, in main
    a.append(input("element.. "))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	for i in range(n-1):
		a.append(input("element.. "))
	print a

	
>>> main()
No. of elements.. 5
element.. 1
element.. 2
element.. 3
element.. 4
[1, 2, 3, 4]
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	for i in range(n):
		a.append(input("element.. "))
	for i in range(n):
		if(i>0):
			while(j<i)
				psum=psum+a[j]
				
SyntaxError: invalid syntax
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	
	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			while(j>i):
				ssum=ssum+a[j]
				j+=1
			if psum==ssum:
				fl[i]=True
			else:
				fl[i]=False
	for i in range(n):
		if fl==True:
			print "yes"
		else:
			print "no"

			
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
no
no
no
no
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			while(j>i):
				ssum=ssum+a[j]
				j+=1
			if psum==ssum:
				fl[i]=True
			else:
				fl[i]=False
		else:
			print "no"
	for i in range(n):
		if fl==True:
			r=1
	if r=1:
		
SyntaxError: invalid syntax
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			while(j>i):
				ssum=ssum+a[j]
				j+=1
			if psum==ssum:
				fl[i]=True
			else:
				fl[i]=False
		else:
			print "no"
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
no
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			while(j>i):
				ssum=ssum+a[j]
				j+=1
			if psum==ssum:
				fl[i]=True
			else:
				fl[i]=False
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			j+=1
			while(j>i):
				ssum=ssum+a[j]
				j+=1
			if psum==ssum:
				fl[i]=True
			else:
				fl[i]=False
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    main()
  File "<pyshell#64>", line 22, in main
    ssum=ssum+a[j]
IndexError: list index out of range
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			if j==i:
				j+=1
			while(j>i):
				ssum=ssum+a[j]
				j+=1
			if psum==ssum:
				fl[i]=True
			else:
				fl[i]=False
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    main()
  File "<pyshell#67>", line 23, in main
    ssum=ssum+a[j]
IndexError: list index out of range
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			if j==i:
				j+=1
			if(j>i):
				while(j<n):
					ssum=ssum+a[j]
					j+=1
			if psum==ssum:
				fl[i]=True
			else:
				fl[i]=False
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			if j==i:
				j+=1
			if(j>i):
				while(j<n):
					ssum=ssum+a[j]
					j+=1
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
yes
>>> main()
No. of elements.. 5
element.. 1
element.. 1
element.. 1
element.. 10
element.. 0
yes
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	for i in range(n):
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			if j==i:
				j+=1
			if(j>i):
				while(j<n):
					ssum=ssum+a[j]
					j+=1
		print psum
		print ssum
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
0
0
1
13
1
13
1
13
1
13
yes
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			if j==i:
				j+=1
			if(j>i):
				while(j<n):
					ssum=ssum+a[j]
					j+=1
		i+=1
		print psum
		print ssum
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
12
0
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			while(j<i):
				psum=psum+a[j]
				j+=1
			if j==i:
				j+=1
			if(j>i):
				while(j<n):
					ssum=ssum+a[j]
					j+=1
		
		print psum
		print ssum
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
12
0
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0 and i<n):
			while(j<i):
				psum=psum+a[j]
				j+=1
			if j==i:
				j+=1
			if(j>i):
				while(j<n):
					ssum=ssum+a[j]
					j+=1

		print psum
		print ssum
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
12
0
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0 and i<n):
			while(j<i):
				psum=psum+a[j]
				j+=1
				print psum
			if j==i:
				j+=1
			if(j>i):
				while(j<n):
					ssum=ssum+a[j]
					j+=1
					print ssum

		
		
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0 and i<n):
			for j in range(i):
				if(j<i):
					psum=psum+a[j]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					j+=1
					print ssum
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 1
element.. 5
yes
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(i):
				if(j<i):
					psum=psum+a[j]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					j+=1
					print ssum
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(i):
				if(j<i):
					psum=psum+a[j]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					print ssum
		if psum==ssum:
			fl[i]=True
		else:
			fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    main()
  File "<pyshell#100>", line 11, in main
    a.append(input("element.. "))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> main()
No. of elements.. 1
element.. 5
yes
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> main()
No. of elements.. 5
element.. 1
element.. 1
element.. 1
element.. 1
element.. 1
1
2
3
4
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(i):
				if(j<i):
					psum=psum+a[j]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					print ssum
			if psum==ssum:
				fl[i]=True
			else:
				fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(i):
				if(j<i):
					psum=psum+a[j]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					print ssum
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:
		
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(i):
				if(j<i):
					psum=psum+a[j]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					print ssum
					print "hey"
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(n):
				if(j<i):
					psum=psum+a[j]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					print ssum
					print "hey"
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(n):
				while(j<i):
					psum=psum+a[j]
					j+=1
					print psum
				while(j>i):
					ssum=ssum+a[j]
					j+=1
					print ssum
					print "hey"
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
17
18
23
24
29
34
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(n):
				psum=psum+a[0:j:]
				print psum
				ssum=ssum+a[j+1:n]
				print ssum
				print "hey"
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7

Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    main()
  File "<pyshell#122>", line 18, in main
    psum=psum+a[0:j:]
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(n):
				psum=psum+a[0:j:]
				print psum
				ssum=ssum+a[j+1:n:]
				print ssum
				print "hey"
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(n):
				psum=psum+a[0:j]
				print psum
				ssum=ssum+a[j+1:n]
				print ssum
				print "hey"
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7

Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    main()
  File "<pyshell#127>", line 18, in main
    psum=psum+a[0:j]
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(n):
				if(j<i):
					psum=psum+a[j]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					print ssum
					print "hey"
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(n):
				if(j<i):
					psum=psum+a[j]
					k=j
					for k in range(n):
						ssum=ssum+a[k]
					print psum
				elif(j>i):
					ssum=ssum+a[j]
					k=0
					for k in range(j):
						psum=psum+a[k]
					print ssum
					print "hey"
				if psum==ssum:
					fl[i]=True
				else:
					fl[i]=False
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
6
7
12
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	psum=0
	ssum=0
	j=0
	r=0

	for i in range(n):
		a.append(input("element.. "))
	fl=[n]
	for i in range(n):
		fl.append(False)
	while i<n:
		if(i>0):
			for j in range(n):
				if(j<i):
					psum=psum+a[j]
					k=j
					for k in range(n):
						ssum=ssum+a[k]
					print psum
					print ssum
					if psum==ssum:
						fl[i]=True
					else:
						fl[i]=False
				elif(j>i):
					ssum=ssum+a[j]
					k=0
					for k in range(j):
						psum=psum+a[k]
					print psum
					print ssum
					if psum==ssum:
						fl[i]=True
					else:
						fl[i]=False
					print "hey"
				
		i+=1
	for i in fl:
		if i==True:
			r=1
	if r==1:
		print "yes"
	else:

		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
1
19
6
38
7
57
12
76
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	j=0
	fl=0
	for i in range(n):
		a.append(input("element.. "))
	for i in range(n):
		psum=0
		ssum=0
		for j in range(0,i):
			psum=psum+a[j]
		for k in range(i,n):
			ssum=ssum+a[k]
		if(psum==ssum):
			fl=1
			print "yes"
	if fl==0:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 1
element.. 1
element.. 1
element.. 1
no
>>> def main():
	n=int(input("No. of elements.. "))
	i=0
	a=[]
	j=0
	fl=0
	for i in range(n):
		a.append(input("element.. "))
	for i in range(n):
		psum=0
		ssum=0
		for j in range(0,i):
			psum=psum+a[j]
		for k in range(i+1,n):
			ssum=ssum+a[k]
		if(psum==ssum):
			fl=1
			print "yes"
	if fl==0:
		print "no"

		
>>> main()
No. of elements.. 5
element.. 1
element.. 1
element.. 1
element.. 1
element.. 1
yes
>>> main()
No. of elements.. 5
element.. 1
element.. 5
element.. 1
element.. 5
element.. 7
yes
>>> main()
No. of elements.. 5
element.. 1
element.. 1
element.. 1
element.. 10
element.. 0
no
>>> 
