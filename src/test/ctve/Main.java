package test.ctve;

import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        encrypt(new int[]{1,2,5,7,8});
    }

    public static void encrypt(int a[]) {
        Set countset = new HashSet();
        int flag = 0;
        for (int x:a) {
            if (! countset.add(x) )
                flag ++;
        }
        if (flag >=3) {
            System.out.println("您的密码不能同时出现4个一样的数字，请重新输入");
            return;
        }
        for (int i = 1; i < a.length-2 ; i++) {
            if (a[i]-1 == a[i-1] &&a[i]+1==a[i+1] && a[i+2] == a[i+2]) {
                System.out.println("您的密码存在超过三位是连续的数字，请重新输入");
                return;
            }
        }
        for (int i = 2; i < a.length-1 ; i++) {
            if (a[i]-1 == a[i-1] &&a[i]+1==a[i+1] && a[i-2] == a[i-2]) {
                System.out.println("您的密码存在超过三位是连续的数字，请重新输入");
                return;
            }
        }

        for (int i = 0; i < a.length; i++) {
            a[i]= (a[i]+4)%9;
        }
        int e;
        e = a[0];
        a[0] = a[4];
        a[4] = e;
        e = a[1];
        a[1] = a[3];
        a[3] = e;
        System.out.println(a);


    }


}
