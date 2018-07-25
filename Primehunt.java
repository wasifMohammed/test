/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package primehunt;
import java.util.*;
/**
 *
 * @author DELL
 */
public class Primehunt {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int n,i,p;
        Scanner read= new Scanner(System.in);
        System.out.println("Enter the number..");
        n=read.nextInt();
        boolean prime[]=new boolean[n+1];
        if(n<=100000){
          
            for(i=2;i<=n;++i){
            prime[i]=true;
        }
        for(p=2;p*p<=n;p++){
            if(prime[p]==true){
                for(i=p*2;i<=n;i+=p){
                    prime[i]=false;
                }
            }
        }
        for(i=2;i<=n;++i){
            if(prime[i]==true){
                System.out.print(i+" ");
            }
        
        }
        }
        

    }
    
}
