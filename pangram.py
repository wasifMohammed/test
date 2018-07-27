Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	str0=raw_input("Enter  string.. ")
	i=0
	fl=[]
	for i in range(26):
		fl.append(False)
	for c in str0.lower():
		if not c == " ":
			fl[ord(c) - ord('a')]=True
	for j in fl:
		if j==False:
			return False
	return True

>>> main()
Enter  string.. A quick brown fox jumps over the lazy dog
True
>>> main()
Enter  string.. crack
False
>>> 
