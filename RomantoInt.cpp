#include <cstdlib>

#include <iostream>


int
main ()
{

  char inp[10];
 
  int n=0, value;

  int size;

  int z;

  
  std::cout << "Enter the roman numeral..";

    std::cin >> inp;

    while (inp[z] != '\0')
{

	
	size=z;
	++z;
  
               }
  /*int length (char const *inp);
 
                   {
    //int z=0;
    
    
  }*/

   size = z;

   for (int i = 0; i<size; ++i)
 
    {
      if (inp[i] == 'I')
	{

	  //value = 1;

	  if(inp[i+1] == 'V'||inp[i+1]=='X'){

	      value= -1;

	  }else {

	      value=1;

	  }

	}
 
     else if (inp[i] == 'V')
	{

	  value = 5;
	}

      else if (inp[i] == 'X')
	{

	    if(inp[i+1] == 'L'||inp[i+1]=='C'){

	      value= -10;

	  }else {

	      value=10;

	  }
	  
  
	}
   
   else if (inp[i] == 'L')

	{
	  value = 50;

	}
      else if (inp[i] == 'C')

	{
	  //value = 100;

	  if(inp[i+1] == 'D'||inp[i+1]=='M'){

	      value= -100;

	  }else {

	      value=100;

	  }

	}
    
   else if (inp[i] == 'D')
	{

	  value = 500;

	}
   
   else if (inp[i] == 'M') {

	  value = 1000;

	}
  
    // else {

      //  std::cout<<"Invalid input.";

      //}

      n = n + value;


    }

  std::cout << "The entered value is  ";

  std::cout << n;

 
 return z;


}

