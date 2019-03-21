package test.QUnaer;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static int max;
    public static int current_s = 0;
    public static int best = 0;
    public static Queue<HeapNode> queue;

    static class HeapNode {
        int level;
        int seat;
        int maxbound;

        public HeapNode(int level, int maxbound, int seat) {
            this.level = level;
            this.maxbound = maxbound;
            this.seat = seat;
        }
    }

    public static void main(String[] args) {
//        int num = 5;
//        int seats = 100;
//        int[] a = {10,20,30,40,50};


        Scanner sc = new Scanner(System.in);
        String ipt = sc.nextLine();
        int num = Integer.valueOf(ipt.split(" ")[0]);
        int seats = Integer.valueOf(ipt.split(" ")[1]);
        max = seats;
        String[] bagg = sc.nextLine().split(" ");
        int[] a = new int[bagg.length];
        for (int i = 0; i < bagg.length; i++) {
            a[i] = Integer.valueOf(bagg[i]);
        }
        Arrays.sort(a);
        queue = new LinkedList<>();
        if(seats!=0)
            allocate(num,seats,a);
        else {
            if (Arrays.asList(a).contains(0) || num == 0)
                System.out.println("perfect");
            else
                System.out.println("good");
        }

    }

    public static int maxBound(int level, int[] bag ) {
        int left = max - current_s;
        int bound = current_s;
        while (level <= bag.length-1 && left >= bag[level]) {
            left -= bag[level];
            bound+=bag[level];
            level++;
        }
        return bound;
    }

    public static void addCurrentLiveNode (int level,int maxbound, int seat) {
        HeapNode heapNode = new Main.HeapNode(level,maxbound,seat);
        queue.add(heapNode);
    }

    public static void allocate(int num, int seats, int[] bag ) {
        int i = 0;
        int maxbound = maxBound(0,bag);
        while (i!=num) {
            int st = current_s + bag[i];
            if (st == seats) {
                best = st;
                break;
            }

            if (st < max) {
                best = current_s+bag[i]>best?current_s+bag[i]:best;
                addCurrentLiveNode(i+1,maxbound,st);
            }
            maxbound = maxBound(i+1,bag);
            if (best <= maxbound) {
                addCurrentLiveNode(i+1,maxbound,current_s);
            }
            if (queue.isEmpty())
                break;
            HeapNode heapNode = queue.poll();
            current_s = heapNode.seat;
            maxbound = heapNode.maxbound;
            i = heapNode.level;
        }
        if (best == max)
            System.out.println("perfect");
        else
            System.out.println("good");
    }

}
