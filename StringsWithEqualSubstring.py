Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	a=raw_input("string 1.. ")
	b=raw_input("string 2.. ")
	i=0
	j=0
	flag=0
	for i in range(len(a)):
		for j in range(len(b)):
			if(a[i] and a[i+1] == b[j] and b[j+1]):
				flag=1
	if(flag==1):
		print "yes"
	else:
		print "no"

		
>>> main()
string 1.. abcxyz
string 2.. hagsaabc

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    main()
  File "<pyshell#14>", line 9, in main
    if(a[i] and a[i+1] == b[j] and b[j+1]):
IndexError: string index out of range
>>> def main():
	a=raw_input("string 1.. ")
	b=raw_input("string 2.. ")
	i=0
	j=0
	flag=0
	for i in range(len(a)-1):
		for j in range(len(b)-1):
			if(a[i] and a[i+1] == b[j] and b[j+1]):
				flag=1
	if(flag==1):
		print "yes"
	else:
		print "no"

		
>>> main()
string 1.. abcxyz
string 2.. hagsaabc
yes
>>> main()
string 1.. abcd
string 2.. bcd
yes
>>> acbscdsa

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    acbscdsa
NameError: name 'acbscdsa' is not defined
>>> main()
string 1.. acbscdsa
string 2.. bsc
yes
>>> main()
string 1.. abc
string 2.. xy
no
>>> 
