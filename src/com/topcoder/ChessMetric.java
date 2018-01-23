package com.topcoder;

/**
 * Problem Statements
 * <p>
 * Suppose you had an n by n chess board and a super piece called a kingknight. Using only one move the kingknight denoted 'K'
 * below can reach any of the spaces denoted 'X' or 'L' below:
 * .......
 * ..L.L..
 * .LXXXL.
 * ..XKX..
 * .LXXXL.
 * ..L.L..
 * .......
 * In other words, the kingknight can move either one space in any direction (vertical, horizontal or diagonally) or can make an
 * 'L' shaped move. An 'L' shaped move involves moving 2 spaces horizontally then 1 space vertically or 2 spaces vertically then 1
 * space horizontally. In the drawing above, the 'L' shaped moves are marked with 'L's whereas the one space moves are marked with 'X's.
 * In addition, a kingknight may never jump off the board.
 * Given the size of the board, the start position of the kingknight and the end position of the kingknight, your method will return
 * how many possible ways there are of getting from start to end in exactly numMoves moves. start and finish are int[]s each containing
 * 2 elements. The first element will be the (0-based) row position and the second will be the (0-based) column position.
 * Rows and columns will increment down and to the right respectively. The board itself will have rows and columns ranging from 0 to
 * size-1 inclusive.
 * Note, two ways of getting from start to end are distinct if their respective move sequences differ in any way. In addition, you are
 * allowed to use spaces on the board (including start and finish) repeatedly during a particular path from start to finish. We will
 * ensure that the total number of paths is less than or equal to 2^63-1 (the upper bound for a long).
 * <p>
 * Constraints
 * -	size will be between 3 and 100 inclusive
 * -	start will contain exactly 2 elements
 * -	finish will contain exactly 2 elements
 * -	Each element of start and finish will be between 1 and size-1 inclusive
 * -	numMoves will be between 1 and 50 inclusive
 * -	The total number of paths will be at most 2^63-1.
 */

/**
 * .......
 * ..L.L..
 * .LXXXL.
 * ..XKX..
 * .LXXXL.
 * ..L.L..
 * .......
 */
public class ChessMetric {
    public static void main(String[] args) {
        int[] start = {0, 0}, end = {0, 99};
        long x = howMany(100, start, end, 50);
        System.out.println("x:" + x);
    }

    public static long howMany(int size, int[] start, int[] end, int numMoves) {
        int[][] nextstep = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}, {-1, 1}, {-1, -1}, {1, -1}, {1, 1}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}, {1, 2}, {1, -2}, {-1, 2}, {-1, -2}};
        long[][][] distinct = new long[size][size][numMoves + 1];
        distinct[start[0]][start[1]][0] = 1;
        for (int k = 1; k <= numMoves; k++)
            for (int i = 0; i < size; i++)
                for (int j = 0; j < size; j++)
                    a:for (int l = 0; l < nextstep.length; l++) {
                        int rc = i + nextstep[l][0];
                        int rr = j + nextstep[l][1];
                        if (rr < 0 || rc < 0 || rr >= size || rc >= size)
                            continue a;
                        distinct[rc][rr][k] += distinct[i][j][k - 1];
                    }


        return distinct[end[0]][end[1]][numMoves];
    }


}
