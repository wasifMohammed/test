Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def cop(int a,int b):
	
SyntaxError: invalid syntax
>>> def cop(a,b):
	if(a==0||b==0):
		
SyntaxError: invalid syntax
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0||m==0):
			
SyntaxError: invalid syntax
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0||m==0):return 0
		
SyntaxError: invalid syntax
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			cop(n-m,m)
		elif(m>n):
			cop(n,m-n)
		else:
			return 0
	if(cop(n,m)==1):
		print "YES"
	else:
		print "NO"

		
>>> main()
Enter n..2
Enter m..3
NO
>>> main()
Enter n..2
Enter m..4
NO
>>> main()
Enter n..109
Enter m..2
NO
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			cop(n-m,m)
		else:
			cop(n,m-n)
	if(cop(n,m)==1):
		print "YES"
	else:
		print "NO"

		
>>> main()
Enter n..2
Enter m..3
NO
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			cop(n-m,m)
		elif(m>n):
			cop(n,m-n)
		else:
			return 0
    if(cop(n,m)==1):
		print "YES"
    else:
		print "NO"
		
  File "<pyshell#31>", line 16
    if(cop(n,m)==1):
                   ^
IndentationError: unindent does not match any outer indentation level
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			cop(n-m,m)
		elif(m>n):
			cop(n,m-n)
		else:
			return 0
    if(cop(n,m)==1):
	    
  File "<pyshell#34>", line 16
    if(cop(n,m)==1):
                   ^
IndentationError: unindent does not match any outer indentation level
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			cop(n-m,m)
		elif(m>n):
			cop(n,m-n)
		else:
			return 0


	
>>> main()
Enter n..2
Enter m..3
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			cop(n-m,m)
		elif(m>n):
			cop(n,m-n)
		else:
			return 0
    if(cop(n,m)==1):
	print "YES"
    else:
	print "NO"
	
  File "<pyshell#37>", line 16
    if(cop(n,m)==1):
                   ^
IndentationError: unindent does not match any outer indentation level
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			cop(n-m,m)
		elif(m>n):
			cop(n,m-n)
		else:
			return 0
	if(cop(n,m)==1):
		print "YES"

		
>>> def main():
	n=int(input("Enter n.."))
	m=int(input("Enter m.."))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			cop(n-m,m)
		elif(m>n):
			cop(n,m-n)
		else:
			return 0
	if(cop(n,m)==1):
		print "YES"
	else:
		print "NO"

		
>>> main()
Enter n..2
Enter m..3
NO
>>> def main():
...   n=int(input("ENter n.."))
...   m=int(input("Enter m.."))
...   def cop(n,m):
...     if(n==0 or m==0):
...       return 0
...     elif(n==m):
...       return n
...     elif(n>m):
...       return cop(n-m,m)
...     else:
...       return cop(n,m-n)
...   if(cop(n,m)==1):
...     print "YES"
...   else:
...     print "NO"
  File "<pyshell#46>", line 3
    ...   n=int(input("ENter n.."))
    ^
IndentationError: expected an indented block
>>> def main():
...   n=int(input("ENter n.."))
...   m=int(input("Enter m.."))
...   def cop(n,m):
...     if(n==0 or m==0):
...       return 0
...     elif(n==m):
...       return n
...     elif(n>m):
...       return cop(n-m,m)
...     else:
...       return cop(n,m-n)
...   if(cop(n,m)==1):
...     print "YES"
...   else:
...     print "NO"
  File "<pyshell#47>", line 3
    ...   n=int(input("ENter n.."))
    ^
IndentationError: expected an indented block
>>> def main():
	n=int(input("Enter n.. "))
	m=int(input("ENter m.. "))
	def cop(n,m):
		if(n==0 or m==0):
			return 0
		elif(n==m):
			return n
		elif(n>m):
			return cop(n-m,m)
		else:
			return cop(n,m-n)
	if(cop(n,m)==1):
		print "YES"
	else:
		print "NO"

		
>>> main()
Enter n.. 2
ENter m.. 3
YES
>>> main()
Enter n.. 2
ENter m.. 4
NO
>>> 
