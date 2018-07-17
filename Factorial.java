/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package factorial;
import java.io.*;
import java.util.*;

/**
 *
 * @author DELL
 */
public class Factorial {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       int n,result,i=0;
       Scanner read = new Scanner(System.in);
       n=read.nextInt();
       result=n;
       if(n<=20){
           for(i=1;i<n;++i){
           result=result*(n-i);
           }
           System.out.println(result);
           }else{
           System.out.println("Invalid input..");
       
       }
       // TODO code application logic here
    }
    
}
