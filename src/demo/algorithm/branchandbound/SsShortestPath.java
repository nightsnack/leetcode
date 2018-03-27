package demo.algorithm.branchandbound;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Stack;

public class SsShortestPath {

    public static AdjacencyGraph graph;

    public static class QueueNode {
        int length;
        int vertex;

        public QueueNode(int length, int vertex) {
            this.length = length;
            this.vertex = vertex;
        }
    }

    public static class distEdge {
        int frontVertex;
        int length;

        public distEdge(int frontVertex, int length) {
            this.frontVertex = frontVertex;
            this.length = length;
        }
    }

    public static Queue<SsShortestPath.QueueNode> pq;

    public static void main(String[] args) {
        graph = new AdjacencyGraph(11, 3);
        int[][] a = {{0, 1, 2}, {0, 2, 3}, {0, 3, 4}
                , {1, 2, 3}
                , {1, 5, 2}
                , {1, 4, 7}
                , {2, 5, 9}
                , {2, 6, 2}
                , {3, 6, 2}
                , {4, 7, 3}
                , {4, 8, 3}
                , {5, 6, 1}
                , {5, 8, 3}
                , {6, 9, 1}
                , {6, 8, 5}
                , {7, 10, 3}
                , {8, 10, 2}
                , {9, 8, 2}
                , {9, 10, 2}};
        EdgeElement[] edgeElements = new EdgeElement[a.length];
        for (int i = 0; i < edgeElements.length; i++) {
            edgeElements[i] = new EdgeElement(a[i][0],a[i][1], a[i][2]);
        }
        if (graph.createGraph(edgeElements)) {
            System.out.println("created");
        }

        pq = new PriorityQueue<>(11, new Comparator<SsShortestPath.QueueNode>() {
            @Override
            public int compare(SsShortestPath.QueueNode o1, SsShortestPath.QueueNode o2) {
                return o1.length-o2.length;
            }
        });

        shortestPath(0,10);

    }


    public static void shortestPath(int fromVertex, int toVertex) {
        int shortestPath = 0;
        int[][] a = graph.getA();
        pq.add(new SsShortestPath.QueueNode(shortestPath,0 ));
        SsShortestPath.distEdge[] dist = new SsShortestPath.distEdge [graph.n];
        for (int i = 0; i < dist.length; i++) {
            dist[i] = new SsShortestPath.distEdge(-1,Integer.MAX_VALUE);
//            dist[i].length = Integer.MAX_VALUE;
        }
        while (true)  {
            SsShortestPath.QueueNode queueNode = pq.poll();
            int nowVertex = queueNode.vertex;
            int currentLength = queueNode.length;
            for (int j = 0; j < graph.n; j++) {
                if (a[nowVertex][j]!=Integer.MAX_VALUE && currentLength + a[nowVertex][j] < dist[j].length)
                {
                    pq.add(new SsShortestPath.QueueNode(a[nowVertex][j]+ currentLength , j));
                    dist[j].length = currentLength + a[nowVertex][j];
                    dist[j].frontVertex = nowVertex;
                }
            }
            if (pq.isEmpty()) {
                break;
            }

        }
        shortestPath = dist[dist.length-1].length;
        int frontVertex = dist[dist.length-1].frontVertex;
        Stack <Integer> s = new Stack<>();
        s.push(dist.length-1);
        while (frontVertex != 0) {
            s.push(frontVertex);
            frontVertex = dist[frontVertex].frontVertex;
        }
        s.push(0);
        while (!s.isEmpty()) {
            System.out.print(s.pop()+" ");
        }
        System.out.println();
        System.out.println(shortestPath);
    }
}
