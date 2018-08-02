/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package capitalizefirst;
import java.io.*;
import java.util.*;
/**
 *
 * @author DELL
 */
public class Capitalizefirst {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        int i = 0,j,flag = 0;
        String str0  = new String();
        Scanner read = new Scanner(System.in);
        System.out.println("Enter the String..");
        str0 = read.nextLine();
        String newstr = new String();
        newstr = "";
        char[] chars = new char[20];
       
        chars  = str0.toCharArray();
        
        if(str0.length() <= 100000){
            for(i = 0; i < str0.length(); ++i){
                if (i >= 0 && i < str0.length()){
                    if(chars[i] != ' '){
                        if(i%2 == 0){
                            newstr = newstr + Character.toUpperCase(chars[i]);
                        }else if(i%2 != 0){
                            newstr = newstr + Character.toLowerCase(chars[i]);
                        }
                    }else if(chars[i] == ' '){
                        /*i++;
                         *newstr=newstr+' ';
                         *i++;*/
                        if(i%2 != 0){
                            newstr = newstr + Character.toUpperCase(chars[i]);
                        }else if(i%2 == 0){
                            newstr = newstr + Character.toLowerCase(chars[i]);
                        }
                        i--;
                        i++;
                    }
                }
            }
        }
        System.out.println(newstr);
    }
}
