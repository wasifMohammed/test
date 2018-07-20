/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package swapchar;
import java.lang.*;
import java.io.*;
import java.util.*;

/**
 *
 * @author DELL
 */
public class SwapChar {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String s;
        char temp;
        int i;
        Scanner read=new Scanner(System.in);
        s=read.next();
        char str[]=s.toCharArray();
        if(s.length()%2==0){
        for(i=0;i<str.length-1;i=i+2){
            temp=str[i];
            str[i]=str[i+1];
            str[i+1]=temp;
        }
        System.out.println(str);
        }else{
            for(i=0;i<str.length-1;i=i+2){
            temp=str[i];
            str[i]=str[i+1];
            str[i+1]=temp;
        }
        System.out.println(str);
        }
        
        // TODO code application logic here
    }
    
}
