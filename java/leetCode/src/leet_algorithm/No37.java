package leet_algorithm;

import java.util.HashSet;

public class No37 {
    
    public void solveSudoku(char[][] board) {
        
        // Initialize the hash tables
        HashSet[] rows, columns, cubes;
        rows = new HashSet[9]; columns = new HashSet[9]; cubes = new HashSet[9];
        for(int i = 0; i < 9; i++) {
            rows[i] = new HashSet<Character>();
            columns[i] = new HashSet<Character>();
            cubes[i] = new HashSet<Character>();
        }
        
        fillSets(board, rows, columns, cubes);
        backtrack(board, rows, columns, cubes, 0, 0);
        
    }
    
    public void fillSets(char[][] board, HashSet[] rows, HashSet[] columns, HashSet[] cubes) {
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                rows[i].add(board[i][j]);
                columns[j].add(board[i][j]);
                cubes[(i/3) * 3 + (j/3)].add(board[i][j]);
            }
        }
    }
    
    public boolean isFull(HashSet[] rows, HashSet[] columns, HashSet[] cubes) {
        int res = 0;
        for(int i = 0; i < 9; i++) {
            res += rows[i].size() + columns[i].size() + cubes[i].size();
        }
        return res == (27 * 9);
    }
    
    public void backtrack(char[][] board, HashSet[] rows, HashSet[] columns, HashSet[] cubes, int i, int j) {
        
        if( isFull(rows, columns, cubes) || (i>=9 || j>=9) ) {
            return;
        } 
        
        char curr = board[i][j];
        int n = (i/3) * 3 + (j/3);

        // start backtracking
        char temp;
        if(curr != '.') {
            // rows[i].add(curr);
            // columns[j].add(curr);
            // cubes[n].add(curr);
            
            backtrack(board, rows, columns, cubes, j==8? i+1:i, j==8? 0:j+1);
            
            
        } else {
            
            for(int k = 1; k <= 9; k++) {
                
                temp = (""+k).charAt(0);
                if(rows[i].contains(temp) || columns[j].contains(temp) || cubes[n].contains(temp)) {
                    continue;
                } 
                board[i][j] = temp;
                rows[i].add(temp);
                columns[j].add(temp);
                cubes[n].add(temp);
                
                backtrack(board, rows, columns, cubes, j==8? i+1:i, j==8? 0:j+1);
                
                rows[i].remove(temp);
                columns[j].remove(temp);
                cubes[n].remove(temp);
                board[i][j] = '.';
            }
            
        }

    }
    

    
}


