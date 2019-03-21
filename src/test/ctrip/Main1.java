package test.ctrip;

import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);

        int l = sc.nextInt();
        int [] a = new int[l];
        for (int i = 0; i < l; i++) {
            a[i] = sc.nextInt();
        }
        moveZeroes(a);

    }

    public static void moveZeroes(int[] a) {
        int k = 0;
        for(int i = 0;i < a.length;i++){ 
            if(a[i] == 0){
                k=i+1;
                for(int j = k;j < a.length;j++){ //与后最近非零元素调换  
                    if(a[j] != 0){
                        a[i] = a[j];
                        a[j] = 0;
                        break;
                    }
                }
            }
        }
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }

    }
}
