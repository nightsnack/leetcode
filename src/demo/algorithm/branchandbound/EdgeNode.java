package demo.algorithm.branchandbound;

public class EdgeNode {

	public int adjvex;	//adjvex
	public int weight; //weight of edge as for graph
	public EdgeNode next;
	/**
	 * without weight
	 * @param adjvex
	 * @param next
	 */
	public EdgeNode(int adjvex, EdgeNode next) {
		super();
		this.adjvex = adjvex;
		this.next = next;
		this.weight = 1;
	}
	
	/**
	 * 有权图
	 * @param adjvex
	 * @param weight
	 * @param next
	 */
	public EdgeNode(int adjvex, int weight, EdgeNode next) {
		super();
		this.adjvex = adjvex;
		this.weight = weight;
		this.next = next;
	}
	
	
	
	
}
