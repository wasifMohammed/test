def main():
	n=int(input("Enter n.. "))
	m=int(input("ENter m.. "))
	if(n<=100000 and m<=100000):
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
