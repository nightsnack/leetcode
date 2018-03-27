package demo.algorithm.branchandbound;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

public class Knapsack01 {

    int[] weight;
    int[] value;

    public int max;
    int current_w;
    int current_v;
    int best_v;

    Queue<HeapNode> saveNode;

    public Knapsack01() {
        max = 30;
        weight = new int[] {20,15,15,0};
        value = new int[] {40,25,25,0};
        current_v = 0;
        current_w = 0;
        best_v = 0;

        saveNode = new PriorityQueue<>(weight.length, new Comparator<HeapNode>() {
            @Override
            public int compare(HeapNode o1, HeapNode o2) {
                return (int)((double)o2.c_value/o2.c_weight - (double)o1.c_value/o1.c_weight);
            }
        });
    }

    public double maxBound(int i) {
        int left = max - current_w;
        double bound = current_v;
        while (i<=weight.length-1 && left >=weight[i] ) {
            left-=weight[i];
            bound+=value[i];
            i++;
        }
        if (i<weight.length-1) {
            bound+= (double)value[i]/(double)weight[i] * left;
        }

        return bound;
    }

    public void addCurrentLiveNode (int i, double bound, int current_w,int current_v) {
        HeapNode heapNode = new HeapNode(i,bound,current_v,current_w);
        saveNode.add(heapNode);
    }

    public  int solve() {
        int i = 0;
        double maxbound = maxBound(0);
        while (i!=weight.length) {

            int wt = current_w+weight[i];
            if (wt<=max) {  //左节点（1）可行
                best_v = current_v+value[i]>best_v?current_v+value[i]:best_v;
                addCurrentLiveNode(i+1,maxbound,current_w+weight[i],current_v+value[i]);
            }
            maxbound = maxBound(i+1);//计算右节点的的上界是否可取
            if (best_v<=maxbound) {
                addCurrentLiveNode(i+1,maxbound,current_w,current_v);
            }
            if (saveNode.isEmpty())
                break;
            HeapNode heapNode = saveNode.poll();
            current_w = heapNode.c_weight;
            current_v = heapNode.c_value;
            maxbound = heapNode.maxBound;
            i = heapNode.level;
        }
        return best_v;
    }

    public static void main(String[] args) {
        Knapsack01 knapsack01 = new Knapsack01();
        System.out.println(knapsack01.solve());
    }
}
