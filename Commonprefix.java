/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package commonprefix;
import java.util.*;
/**
 *
 * @author DELL
 */
public class Commonprefix {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int n,i,j,len0,len1;
        //String str0=new String();
        StringBuilder strb=new StringBuilder();
        System.out.println("Enter the number of strings..");
        Scanner read=new Scanner(System.in);
        n=read.nextInt();
        String[] str1=new String[n];
        char[] temp0=new char[20];
        char[] temp1=new char[20];
        char[] result=new char[20];
        for(i=0;i<n;++i){
            str1[i]=read.next();  
            }
        for(j=0;j<n-1;++j){
            temp0=str1[j].toCharArray();
            temp1=str1[j+1].toCharArray();
            len0=temp0.length;
            len1=temp1.length;
            if(len0<len1){
                for(i=0;i<len0;++i){
                    if(temp0[i]==temp1[i]){
                        result[i]=temp0[i];
                    } 
                }
                //System.out.print(result);
            }else if(len0>len1){
                for(i=0;i<len1;++i){
                    if(temp0[i]==temp1[i]){
                        result[i]=temp0[i];
                    }
                   // System.out.print(result);
            }
              
                    
            //System.out.print(str1[i]+" ");  
            }else {
                    for(i=0;i<len1;++i){
                    if(temp0[i]==temp1[i]){
                        result[i]=temp0[i];
                    }
            }
                    //System.out.print(result);
            }
    }
        System.out.print(result);
    
}
}