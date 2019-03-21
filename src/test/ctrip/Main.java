package test.ctrip;

import java.util.Scanner;

public class Main {

    public static int[][] change(int[][] b) {
        int[][] temp = new int[b[0].length][b.length];
        for (int i = 0; i < b.length; i++) {
            for (int j = 0; j < b[i].length; j++) {
                temp[i][j]=b[b[i].length-j-1][i];
            }
        }
        return temp;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String ipt = sc.nextLine();
        String[] ipta = ipt.split(" ");
        int [][] a = new int[ipta.length][ipta.length];

        for (int i = 0; i < ipta.length; i++) {
            a[0][i] = Integer.valueOf(ipta[i]);
        }
        for (int i = 1; i < a.length; i++) {
            ipt = sc.nextLine();
            ipta = ipt.split(" ");
            for (int j = 0; j < a.length; j++) {
                a[i][j] = Integer.valueOf(ipta[j]);
            }
        }
        int [][]t=change(a);
        for(int i=0;i<t.length;i++){
            for(int j=0;j<t[0].length;j++){
                System.out.print(t[i][j]+" ");
            }
            System.out.println();
        }
        sc.close();
    }

}
