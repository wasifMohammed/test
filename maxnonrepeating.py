Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	str0=raw_input("Enter the string.. ")
	temp=""
	length=0
	i=0
	j=1
	while(i<len(str0)-1):
		if str0[i]!=str0[i+1]:
			if(str0[i] not in temp):
				temp+=str0[i]
			else:
				temp=temp
		elif str0[i]==str0[i+1]:
			if(str0[i]!=str0[i-1]):
				if str0[i] not in temp:
					temp+=str0[i]
				else:
					temp=temp
			else:
				temp=temp
		i+=1
	print temp
	print len(temp)

>>> main()
Enter the string.. abcddddd
abcd
4
>>> abcabcaaaa

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    abcabcaaaa
NameError: name 'abcabcaaaa' is not defined
>>> main()
Enter the string.. abcabcaaaaa
abc
3
>>> 
