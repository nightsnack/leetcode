package demo.algorithm.branchandbound;

public class HeapNode {
    int level;
    double maxBound;
    int c_value;
    int c_weight;

    public HeapNode(int level, double maxBound, int c_value, int c_weight) {
        this.level = level;
        this.maxBound = maxBound;
        this.c_value = c_value;
        this.c_weight = c_weight;
    }
}
