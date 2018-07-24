/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package reversingeachstring;
import java.io.*;
import java.util.*;
import java.lang.*;
/**
 *
 * @author DELL
 */
public class Reversingeachstring {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args){
        int i;
        String str0=new String();
        String str1=new String();
        String str2=new String();
        String[] str3= new String[10];
        String temp= new String();
        temp=" ";
        Scanner read=new Scanner(System.in);
        System.out.println("Enter the string..");
        str0=read.nextLine();
        if(str0.length()<=100000){
        for(i=str0.length()-1;i>=0;--i){
            str1=str1+str0.charAt(i);
        }
        str3=str1.split(" ");
        for(int j=str3.length-1;j>=0;j--){
             temp=temp+str3[j];
             temp=temp+" ";
             
        }
        System.out.println(temp);
        }
        
      
    }
}
