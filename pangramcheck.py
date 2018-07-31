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


