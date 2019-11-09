//
//  DynamicProgramming.cpp
//  Algorithms
//
//  Created by Kylin on 5/27/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

class LongestCommonSubsequence {
    
    static const int N = 1000;
    
    int lcs(string s1, string s2)
    {
        int res[N+1][N+1];
        
        int m = (int) s1.size();
        int n = (int) s2.size();
        
        s1 = ' ' + s1;
        s2 = ' ' + s2;
        
        int maxv = 0;
        
        for (int i = 0; i <= m; i++) {
            res[i][0] = 0;
        }
        for (int j = 0; j <= n; j++) {
            res[0][j] = 0;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i] == s2[j]) {
                    res[i][j] = res[i-1][j-1] + 1;
                }
                else {
                    res[i][j] = max(res[i-1][j], res[i][j-1]);
                }
                maxv = max(maxv, res[i][j]);
            }
        }
        return maxv;
    }
    
public:
    
    int main()
    {
        string s1, s2;
        int n;
        cin>>n;
        
        for (int i = 0; i < n; i++) {
            cin>>s1>>s2;
            cout<<lcs(s1, s2)<<endl;
        }
        
        return 0;
    }
};


class MatrixChainMultiplication {
    
    
};
