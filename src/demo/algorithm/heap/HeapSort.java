package demo.algorithm.heap;

import java.util.Arrays;
import java.util.Random;

public class HeapSort {

    public static void main(String[] args) {
        Integer [] a = new Integer[10];
        a[0] = 0;
        int i=1;
        Random r = new Random();
        while (i<=9) {
            a[i] = r.nextInt(100);
            i++;
        }
        System.out.println(Arrays.toString(a));
        heapSort(a);
        System.out.println(Arrays.toString(a));

    }

    public static void heapSort (Comparable[] pq) {
        buildHeap(pq);
        int N = pq.length-1;
        while (N>1) {
            swap(pq,1,N);
            sink(pq,1,--N);
        }

    }

    public static void buildHeap(Comparable[] pq) {
        int N = pq.length-1;
        for (int i = N/2; i >=1 ; i--) {
            sink(pq,i,N);
        }
    }

    public static void sink(Comparable[] pq, int t,int N) {
        while (2*t<=N) {
            int j = 2*t;
            if (j<N && less(pq,j,j+1)) {
                j+=1;
            }
            if (less(pq,t,j))
                swap(pq,t,j);
            else
                break;
            t = j;
        }
    }

    public static void swap (Comparable[] pq, int a,int b) {
        Comparable temp = pq[a];
        pq[a] = pq[b];
        pq[b] = temp;
    }

    public static boolean less (Comparable[] pq, int a, int b) {
        if (pq[a].compareTo(pq[b]) < 0 )
            return true;
        else
            return false;
    }
}
