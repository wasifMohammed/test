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

