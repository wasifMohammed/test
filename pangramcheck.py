Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	str0=raw_input("Enter  string.. ")
	i=0
	fl=[]
	c=0
	for i in range(26):
		fl.append(False)
	for c in str0.lower():
		if not c == " ":
			fl[ord(c) - ord('a')]=True
	for j in fl:
		if j==False:
			c=1
		else:
			c=0;
	if c=1:
		
SyntaxError: invalid syntax
>>> def main():
	str0=raw_input("Enter  string.. ")
	i=0
	fl=[]
	c=0
	for i in range(26):
		fl.append(False)
	for c in str0.lower():
		if not c == " ":
			fl[ord(c) - ord('a')]=True
	for j in fl:
		if j==False:
			c=1
		else:
			c=0;
	if c==1:
		print no
	else:
		print yes

		
>>> main()
Enter  string.. abcde

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    main()
  File "<pyshell#8>", line 17, in main
    print no
NameError: global name 'no' is not defined
>>> def main():
	str0=raw_input("Enter  string.. ")
	i=0
	fl=[]
	c=0
	for i in range(26):
		fl.append(False)
	for c in str0.lower():
		if not c == " ":
			fl[ord(c) - ord('a')]=True
	for j in fl:
		if j==False:
			c=1
		else:
			c=0;
	if c==1:
		print "no"
	else:
		print "yes"

		
>>> main()
Enter  string.. abcde
no
>>> main()
Enter  string.. A QUICK BROWN FOX JUMPS OVER THE LAZY DOG
yes
>>> main()
Enter  string.. abcdefghijklmnopqrstuvwxyz
yes
>>> abcdefghijklmnopqrstuvwxyw

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    abcdefghijklmnopqrstuvwxyw
NameError: name 'abcdefghijklmnopqrstuvwxyw' is not defined
>>> main()
Enter  string.. abcdefghijklmnopqrstuvwxyw
no
>>> 
