/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integerreverse;
import java.io.*;
import java.util.*;
/**
 *
 * @author DELL
 */
public class IntegerReverse {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       int n,m,i,len,result=0,c=0;
       Scanner read= new Scanner(System.in);
       n=read.nextInt();
       while(n>0){
       /*n=n%10;
       c++;
       n=n/10;*/
        m=n%10;
           n=n/10;
        result=(result*10)+m;
        
       
       }
      
       System.out.println(result);
       
    }
    
}
