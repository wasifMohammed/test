/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication20;
import java.io.*;
import java.util.*;

/**
 *
 * @author DELL
 */
public class JavaApplication20 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
       int i,flag = 0;
       String str0  = new String();
       Scanner read = new Scanner(System.in);
       System.out.println("Enter the String ..");
       str0=read.nextLine();
       char[] chars = new char[20];
       char[] temp  = new char[20];
        
       chars=str0.toCharArray();
        
       if(str0.length() <= 100000){
           for(i=0;i<str0.length()-1;++i){
                
               if(chars[i] == chars[i+1]){
                   System.out.println("NO..");
                   flag = 1;
               }else if(chars[i]!=chars[i+1]){
                   temp[i]    =  chars[i];
                   chars[i]   =  chars[i+1];
                   chars[i+1] =  temp[i];
                }
           }
       }
       if(flag != 1){
           System.out.println("YES..");       
       }
    }
    
}
